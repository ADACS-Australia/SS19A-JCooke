"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

import logging

from psycopg2 import sql
from psycopg2.extras import RealDictCursor

from .dwfdb import DWFDB

logger = logging.getLogger(__name__)


def search(query_parts, search_columns, limit, offset):
    ra = float(query_parts.get('ra'))
    dec = float(query_parts.get('dec'))
    radius = float(query_parts.get('radius')) / 3600
    target_name = query_parts.get('target_name', None)
    mary_run = query_parts.get('mary_id', None)

    order_by_field = 'id'
    order_by_direction = 'ASC'

    print(ra, dec, radius)

    if mary_run:
        mary_run_min = int(mary_run)
        mary_run_max = int(mary_run)
    else:
        mary_run_min = -2147483648
        mary_run_max = 2147483647

    search_results = None
    total = 0
    with DWFDB() as db_connection:
        with db_connection.cursor(cursor_factory=RealDictCursor) as cursor:
            try:
                sql_str = sql.SQL(
                    "SELECT {} "
                    "FROM dwf "
                    "WHERE "
                    "(spoint(radians(dwf.ra),radians(dwf.dec)) @ scircle(spoint(radians({}),radians({})),radians({}))) "
                    "AND mary_run BETWEEN {} AND {} "
                    "AND sci_path LIKE {} "
                    "ORDER BY {} "
                    "LIMIT {} "
                    "OFFSET {} "
                ).format(
                    sql.SQL(",").join(map(sql.Identifier, search_columns)),
                    sql.Placeholder(),
                    sql.Placeholder(),
                    sql.Placeholder(),
                    sql.Placeholder(),
                    sql.Placeholder(),
                    sql.Placeholder(),
                    sql.SQL(" ").join([sql.Identifier(order_by_field), sql.SQL(order_by_direction)]),
                    sql.Placeholder(),
                    sql.Placeholder(),
                )

                cursor.execute(
                    sql_str,
                    [
                        ra,
                        dec,
                        radius,
                        mary_run_min,
                        mary_run_max,
                        '%{}%'.format(target_name),
                        limit,
                        offset
                    ]
                )
                search_results = cursor.fetchall()

            except Exception as ex:
                logger.log("Exception: ", ex)

            try:
                total_str = sql.SQL(
                    "SELECT COUNT(*) total "
                    "FROM dwf "
                    "WHERE "
                    "(spoint(radians(dwf.ra),radians(dwf.dec)) @ scircle(spoint(radians({}),radians({})),radians({}))) "
                    "AND mary_run BETWEEN {} AND {} "
                    "AND sci_path LIKE {} "
                ).format(
                    sql.Placeholder(),
                    sql.Placeholder(),
                    sql.Placeholder(),
                    sql.Placeholder(),
                    sql.Placeholder(),
                    sql.Placeholder(),
                )

                cursor.execute(
                    total_str,
                    [
                        ra,
                        dec,
                        radius,
                        mary_run_min,
                        mary_run_max,
                        '%{}%'.format(target_name),
                    ]
                )

                total = cursor.fetchone().get('total', 0)

            except Exception as ex:
                logger.log("Exception: ", ex)

    return search_results, total
