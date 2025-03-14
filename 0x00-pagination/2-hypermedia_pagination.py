#!/usr/bin/env python3
"""simple paging method"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int):
    """return start and end indexes to a page"""
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """gets a page with paging method"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        st, end = index_range(page, page_size)
        data = self.dataset()
        if end > len(data):
            return []
        return data[st:end]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """using a hypermedia method"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        st, end = index_range(page, page_size)
        data = self.dataset()
        dataLen = len(data)
        div = int(dataLen / page_size)
        tp = div + 1 if (dataLen % page_size) != 0 else div
        return {
                'page_size': page_size if end <= dataLen else 0,
                'page': page,
                'data': data[st:end] if end <= dataLen else [],
                'next_page': page + 1 if dataLen >= end else None,
                'prev_page': None if st == 0 else page - 1,
                'total_pages': tp
                }
