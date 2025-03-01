#!/usr/bin/python3
""" basic dictionary """
BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """ basic cache """
    def put(self, key, item):
        """ puts item in the cache """

        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """ gets item """

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
