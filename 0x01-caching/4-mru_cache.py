#!/usr/bin/env python3
"""A class MRUCache that inherits from BaseCaching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """inherits from the baseCaching"""
    def __init__(self):
        """initialize the class"""
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """assigns a dictionary self.cache_data"""
        if key is None or item is None:
            pass
        else:
            cache_length = len(self.cache_data)
            base_items = BaseCaching.MAX_ITEMS
            if cache_length >= base_items and key not in self.cache_data:
                evicted_key = self.usage.pop()
                self.cache_data.pop(evicted_key)
                print('DISCARD: {}'.format(evicted_key))

            if key in self.usage:
                """
                move the key to the end of the list showing that it is
                the most recently used from where it is removed
                """
                self.usage.remove(key)
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """returns the values in self.cache_data linked in key"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.usage.remove(key)
        self.usage.append(key)
        return self.cache_data[key]
