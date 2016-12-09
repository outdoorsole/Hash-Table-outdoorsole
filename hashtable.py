#!/usr/bin/python2

from linkedlist import LinkedList, Node


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]
        """Will keep track of the length of the hash table"""
        self.counter = 0

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(self.length())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        # TODO 4: Count number of key-value entries in each of the buckets
        return self.counter

    def contains(self):
        """Return True if this hash table contains the given key, or False"""
        # TODO 3: Check if the given key exists in a bucket
        pass

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # TODO 2: Check if the given key exists and return its associated value
        hash_table_index = self._bucket_index(key)
        print('This is hash_table_index:', hash_table_index)
        for index in self.buckets:
            print('This is index:', index)
            print('This is self.buckets:', self.buckets)
            # if hash_table_index:

            # value = self.buckets[hash_table_index].data
            # return value
        # else:
            # raise KeyError('Key does not exist!', key)

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        index = self._bucket_index(key)
        data = (key, value)

        updated = self.buckets[index].set(lambda x: x[0] == key, data)
        if not updated:
            self.counter += 1

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        # TODO (last): Find the given key and delete its entry if found
        pass

    def keys(self):
        """Return a list of all keys in this hash table"""
        # TODO: Collect all keys in each of the buckets
        pass

    def values(self):
        """Return a list of all values in this hash table"""
        # TODO: Collect all values in each of the buckets
        pass