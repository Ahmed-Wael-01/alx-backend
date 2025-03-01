#!/usr/bin/python3
""" fifo caching """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ fifo cache system """
    lruArr = []

    def put(self, key, item):
        """ put item in cache """

        if key is not None and item is not None:
            if len(self.lruArr) >= self.MAX_ITEMS and \
                    key not in self.cache_data:
                removed_item = self.lruArr.pop(0)
                print('DISCARD: {}'.format(removed_item))
                del self.cache_data[removed_item]
            if key in self.cache_data:
                self.lruArr.insert(-1, self.lruArr.pop(self.lruArr.index(key)))
            else:
                self.lruArr.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ gets item """

        if key is None or key not in self.cache_data:
            return None
        self.lruArr.insert(-1, self.lruArr.pop(self.lruArr.index(key)))
        return self.cache_data[key]
