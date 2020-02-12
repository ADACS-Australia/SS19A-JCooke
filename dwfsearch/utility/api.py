"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""
import json
import logging
import astropy.units as u

from astropy.coordinates import SkyCoord
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

from .dwfdb import DWFDB

logger = logging.getLogger(__name__)


def search(query_parts, search_columns):
    ra = query_parts.get('ra').split(':')
    dec = float(query_parts.get('dec'))
    radius = query_parts.get('radius')
    target_name = query_parts.get('target_name', None)
    mary_run = query_parts.get('mary_id', None)

    c = SkyCoord(
        '{}h{}m{}s'.format(ra[0], ra[1], ra[2]),
        dec*u.degree,
        frame='icrs',
    )

    if mary_run:
        mary_run_min = int(mary_run)
        mary_run_max = int(mary_run)
    else:
        mary_run_min = -2147483648
        mary_run_max = 2147483647

    search_results = None
    with DWFDB() as db_connection:
        with db_connection.cursor(cursor_factory=RealDictCursor) as cursor:
            try:
                sql_str = sql.SQL(
                    "SELECT {} "
                    "FROM dwf "
                    "WHERE "
                    "(spoint(radians(dwf.ra),radians(dwf.dec)) @ scircle(spoint(radians({}),radians({})),radians({}))) "
                    "AND mary_run BETWEEN {} AND {} "
                    "AND sci_path LIKE {}"
                ).format(
                    sql.SQL(",").join(map(sql.Identifier, search_columns)),
                    sql.Placeholder(),
                    sql.Placeholder(),
                    sql.Placeholder(),
                    sql.Placeholder(),
                    sql.Placeholder(),
                    sql.Placeholder(),
                    sql.Placeholder(),
                )

                cursor.execute(
                    sql_str,
                    [
                        c.ra.deg,
                        c.dec.deg,
                        radius,
                        mary_run_min,
                        mary_run_max,
                        '%{}%'.format(target_name),
                    ]
                )
                search_results = cursor.fetchall()

            except Exception as ex:
                logger.log("Exception: ", ex)

    data = {
        'total': len(search_results),
        'search_results': search_results,
    }

    json_response = json.dumps(data)
    json_data = json.loads(json_response)
    return json_data.get('search_results'), json_data.get('total')
