#!/usr/bin/python3
""" Basic Cache that will inherit from the BaseCaching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ class that inherits from BaseCaching"""
    def __init__(self):
        """Initialize the class BasicCache"""
        BaseCaching.__init__(self)

    def put(self, key, item):
        """assigns a dictionary self.cache_data for
        the key"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """A method that returns self.cache_data"""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
