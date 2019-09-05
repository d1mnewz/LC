from abcplus import ABCMeta, abstractmethod
from typing import List


class DataFetcherBase(metaclass=ABCMeta):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_data(self) -> List[str]:
        pass
