import requests
from typing import List

from project.core.DataFetcherBase import DataFetcherBase


class DataFetcherApi(DataFetcherBase):
    data: List[str] = []
    platformsToFetch: List[int] = [21, 9, 43]

    def get_data(self) -> List[str]:
        base_url = 'http://www.giantbomb.com/api/games/'
        api_key = '84e4fdf8957ddf84247c3ea012a4773ffead8156'
        for i in self.platformsToFetch:
            self.__fetch_data_from_api(api_key, base_url, i)

        return self.data

    def __fetch_data_from_api(self, api_key: str, base_url: str, platform_id: int) -> None:
        total_results = 1
        offset = 0
        count = 0
        while offset < total_results:
            params = {
                'api_key': api_key,
                'format': 'json',
                'offset': offset,
                'platforms': platform_id,
                'field_list': 'name'
            }
            headers = {
                'User-Agent': "Dummy Dmytro"
            }
            r = requests.get(base_url, params=params, headers=headers)
            json_response = r.json()
            total_results: int = json_response['number_of_total_results']
            self.data.extend([i['name'] for i in json_response['results']])
            count += 1
            offset = json_response['limit'] * count
