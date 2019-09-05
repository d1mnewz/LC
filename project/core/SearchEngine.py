from typing import Dict, List

from project.core import DataFetcherBase


class SearchEngine:
    x: int
    dataFetcher: DataFetcherBase

    invertedIndex: Dict[str, List[str]] = {}

    def __init__(self, data_fetcher: DataFetcherBase):
        self.invertedIndex = {}
        self.dataFetcher = data_fetcher

    def index_data(self) -> None:
        data: List[str] = self.dataFetcher.get_data()
        stop_words: List[str] = ["the", "a", "an"]
        item: str
        for item in data:
            item_lowercase = item.lower()
            words_list = item_lowercase.split()
            clean_words_list = [x for x in words_list if x not in stop_words]
            for word in clean_words_list:
                if word in self.invertedIndex:
                    self.invertedIndex[word].append(item_lowercase)
                else:
                    self.invertedIndex[word] = [item_lowercase]

    def get_search_result(self, search_query: str) -> List[str]:
        if search_query in self.invertedIndex:
            return self.invertedIndex[search_query]
        else:
            return list()
