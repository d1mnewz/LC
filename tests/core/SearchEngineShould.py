import unittest

from typing import List

from project.core.DataFetcherBase import DataFetcherBase
from project.core.SearchEngine import SearchEngine


class DataFetcherMock(DataFetcherBase):

    def __init__(self):
        self.data = ["Mario Party", "Dummy Party", "The Blue Mario"]

    def get_data(self) -> List[str]:
        return self.data


class SearchServiceShould(unittest.TestCase):
    sut: SearchEngine

    def setUp(self) -> None:
        self.sut = SearchEngine(data_fetcher=DataFetcherMock())

    def test_return_non_empty_list_for_correct_param(self):
        correct_param = "mario"
        self.sut.index_data()
        assert len(self.sut.get_search_result(correct_param)) is 2

    def test_be_empty_for_wrong_param(self):
        assert len(self.sut.get_search_result("test")) is 0

    def test_index(self):
        self.sut.index_data()
        assert len(self.sut.invertedIndex.items()) is not 0


if __name__ == '__main__':
    unittest.main()
