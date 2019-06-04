"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""
import json


def get_data(query_parts, search_columns):
    search_results = [
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
