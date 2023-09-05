#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """returns the dictionary"""
        indexed_data = self.indexed_dataset()
        total_data = len(indexed_data)
        assert 0 <= index < total_data, "Invalid index"

        response = {
                'index': index,
                'page_size': page_size,
                'data': [],
                'next_index': None
        }
        data = []
        for i in range(page_size):
            while True:
                current_row = indexed_data.get(index)
                index += 1
                if current_row is not None:
                    break
                data.append(current_row)

        response['data'] = data
        if indexed_data.get(index):
            response['next_index'] = index
        return response
