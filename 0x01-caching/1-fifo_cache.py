#!/usr/bin/python3
""" fifo caching """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ fifo cache system """
    fifoArr = []

    def put(self, key, item):
        """ put item in cache """

        if key is not None and item is not None:
            if len(self.fifoArr) >= self.MAX_ITEMS and \
                    key not in self.cache_data:
                removed_item = self.fifoArr.pop(0)
                print('DISCARD: {}'.format(removed_item))
                del self.cache_data[removed_item]
            self.cache_data[key] = item
            self.fifoArr.append(key)

    def get(self, key):
        """ gets item """

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
