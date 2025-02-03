#!/usr/bin/env python3
"""a helper function for paging"""


def index_range(page: int, page_size: int):
    """return start and end indexes to a page"""
    return ((page - 1) * page_size, page * page_size)
