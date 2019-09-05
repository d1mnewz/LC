from project.core.DataFetcherApi import DataFetcherApi
from project.core.SearchEngine import SearchEngine

search_engine = SearchEngine(DataFetcherApi())
search_engine.index_data()

while True:
    cmd: str = input('Enter keyword\n')
    print(search_engine.get_search_result(cmd), '')
