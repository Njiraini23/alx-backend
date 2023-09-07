#!/usr/bin/env python3
"""containing LRUCache module"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """defining the class"""
    def __init__(self):
        """
        initializing class by calling the constructor
            of the parent class BaseCaching using super
        initializing empty list self.usage to keep track of the
            usage order of keys
        """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """To store a key-value pair in the cache"""
        if key is None or item is None:
            pass
        else:
            cache_length = len(self.cache_data)
            base_items = BaseCaching.MAX_ITEMS
            if cache_length >= base_items and key not in self.cache_data:
                evicted_key = self.usage.pop(0)
                self.cache_data.pop(evicted_key)
                print('DISCARD: {}'.format(evicted_key))

            if key in self.usage:
                """
                key moved to the end of the list
                (indicating it's the most recently used)
                from where its removed
                """
                self.usage.remove(key)
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """return value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.usage.remove(key)
        self.usage.append(key)
        return self.cache_data[key]
