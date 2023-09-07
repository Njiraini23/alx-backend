#!/usr/bin/env python3
"""Class that inherits form BaseCaching
the class is a caching system."""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO class inherits from BaseCaching"""
    def __init__(self):
        """initializing the class"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Assigns to the dictionary self.cache_data"""
        if key is None or item is None:
            pass
        else:
            cache_length = len(self.cache_data)
            base_items = BaseCaching.MAX_ITEMS
            if cache_length >= base_items and key not in self.cache_data:
                oldest_key = self.queue.pop(0)
                self.cache_data.pop(oldest_key)
                print('DISCARD: {}'.format(oldest_key))

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """Returns the value in self.cache_data"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
