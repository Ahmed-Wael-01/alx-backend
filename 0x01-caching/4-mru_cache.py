#!/usr/bin/python3
""" fifo caching """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ fifo cache system """
    mruArr = []

    def put(self, key, item):
        """ put item in cache """

        if key is not None and item is not None:
            if len(self.mruArr) >= self.MAX_ITEMS and \
                    key not in self.cache_data:
                removed_item = self.mruArr.pop()
                print('DISCARD: {}'.format(removed_item))
                del self.cache_data[removed_item]
            if key in self.cache_data:
                self.mruArr.append(self.mruArr.pop(self.mruArr.index(key)))
            else:
                self.mruArr.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ gets item """

        if key is None or key not in self.cache_data:
            return None
        self.mruArr.append(self.mruArr.pop(self.mruArr.index(key)))
        return self.cache_data[key]
