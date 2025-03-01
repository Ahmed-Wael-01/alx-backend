#!/usr/bin/python3
""" fifo caching """
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ fifo cache system """
    LFU_dict = {}

    def put(self, key, item):
        """ put item in cache """

        if key is not None and item is not None:
            if len(self.LFU_dict) >= self.MAX_ITEMS and \
                    key not in self.cache_data:
                removed_item = min(self.LFU_dict, key=self.LFU_dict.get)
                del self.LFU_dict[removed_item]
                print('DISCARD: {}'.format(removed_item))
                del self.cache_data[removed_item]
            if key in self.cache_data:
                self.LFU_dict[key] += 1
            else:
                self.LFU_dict[key] = 1
            self.cache_data[key] = item

    def get(self, key):
        """ gets item """

        if key is None or key not in self.cache_data:
            return None
        self.LFU_dict[key] += 1
        return self.cache_data[key]
