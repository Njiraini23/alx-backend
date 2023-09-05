#!/usr/bin/env python3
"""A function that takes two integers page and size
returnd a tuple of size two"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ returns a tuple of size 2 """
    if page < 1 or page_size <= 0:
        pass

    start_index = (page - 1) * page_size
    end_index = (page * page_size)

    return (start_index, end_index)
