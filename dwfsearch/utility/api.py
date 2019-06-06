"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""
import json


def search(query_parts, search_columns):
    search_results = [
        {
            'id': '1',
            'name': 'name 1',
            'ra': '01:01:01',
            'dec': '1',
        },
        {
            'id': '2',
            'name': 'name 2',
            'ra': '02:02:02',
            'dec': '2',
        },
        {
            'id': '3',
            'name': 'name 3',
            'ra': '03:03:03',
            'dec': '3',
        },
        {
            'id': '4',
            'name': 'name 4',
            'ra': '04:04:04',
            'dec': '4',
        },
        {
            'id': '5',
            'name': 'name 5',
            'ra': '05:05:05',
            'dec': '5',
        },
        {
            'id': '6',
            'name': 'name 6',
            'ra': '06:06:06',
            'dec': '6',
        },
        {
            'id': '7',
            'name': 'name 7',
            'ra': '07:07:07',
            'dec': '7',
        },
        {
            'id': '8',
            'name': 'name 8',
            'ra': '08:08:08',
            'dec': '8',
        },
        {
            'id': '9',
            'name': 'name 9',
            'ra': '09:09:09',
            'dec': '9',
        },
        {
            'id': '10',
            'name': 'name 10',
            'ra': '10:10:10',
            'dec': '10',
        },
        {
            'id': '11',
            'name': 'name 11',
            'ra': '11:11:11',
            'dec': '11',
        },
        {
            'id': '12',
            'name': 'name 12',
            'ra': '12:12:12',
            'dec': '12',
        }
    ]

    data = {
        'total': len(search_results),
        'search_results': search_results,
    }

    # this will come from the api
    json_response = json.dumps(data)

    json_data = json.loads(json_response)

    return json_data.get('search_results'), json_data.get('total')
