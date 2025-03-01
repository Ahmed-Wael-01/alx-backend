#!/usr/bin/python3
""" fifo caching """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ fifo cache system """
    lifoArr = []

    def put(self, key, item):
        """ put item in cache """

        if key is not None and item is not None:
            if len(self.lifoArr) >= self.MAX_ITEMS and \
                    key not in self.cache_data:
                removed_item = self.lifoArr.pop()
                print('DISCARD: {}'.format(removed_item))
                del self.cache_data[removed_item]
            self.cache_data[key] = item
            self.lifoArr.append(key)

    def get(self, key):
        """ gets item """

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
