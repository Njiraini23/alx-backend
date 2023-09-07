#!/usr/bin/env python3
"""A class LIFOCache that inherits from BaseCaching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ The LIFOCache that inherits from BaseCaching"""
    def __init__(self):
        """Initializes the LIFO cache"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key"""
        if key is None or item is None:
            pass
        else:
            cache_length = len(self.cache_data)
            base_items = BaseCaching.MAX_ITEMS
            if cache_length >= base_items and key not in self.cache_data:
                newest_key = self.queue.pop()
                self.cache_data.pop(newest_key)
                print('DISCARD: {}'.format(newest_key))

            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """returns the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
