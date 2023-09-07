#!/usr/bin/env python3
"""A class LRU that inherits from BaseCaching and
is  a caching system"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """The class LRUCache that inherits from BaseCaching"""
    def __init__(self):
        """initializes the class"""
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """assigns the item value of the key"""
        if key is None and item is None:
            pass
        else:
            cache_length = len(self.cache_data)
            base_items = BaseCaching.MAX_ITEMS
            if cache_length >= base_items and key not in self.cache_data:
                evicted_key = self.usage.pop(0)
                self.cache_data.pop(evicted_key)
                print('DISCARD: {}'.format(evicted_key))

            if key in self.usage:
                """the key at the end of the list is the
                most recently used"""
                self.usage.remove
            self.usage.append(key)
            self.cache_data[key] = item

        def get(self, key):
            """returns the value in the cache_data linked to key"""
            if key is None or key not in self.cache_data.keys():
                return None
            self.usage.remove(key)
            self.usage.append(key)
            return self.cache_data[key]
