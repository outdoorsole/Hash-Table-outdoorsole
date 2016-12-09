#!python

from __future__ import print_function

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        counter = 0
        current_node = self.head
        while current_node != None:
            counter += 1
            current_node = current_node.next
        return counter

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        if self.head == None:
            self.head = self.tail = Node(item)
        else:
            new_node = Node(item)
            self.tail.next = new_node
            self.tail = self.tail.next          
        return self

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        if self.head == None:
            self.head = self.tail = Node(item)
        else:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node
        return self

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # TODO: find given item and delete if found
        current_node = self.head
        # Case 1.a: Find the item in the first node
        if current_node is not None and current_node.data == item:
            self.head = current_node.next
            # Case 1.b: The list contains only one node
            if current_node.next is None:
                self.tail = current_node.next
            return True
        # Case 2.a: Find the item in the second node and onward
        while current_node is not None and current_node.next != None:
            if current_node.next.data == item:
                # Case 2.b: The target node is the last node in the list
                if current_node.next == self.tail:
                    self.tail = current_node
                current_node.next = current_node.next.next
                return True
            # Move on to the next node
            current_node = current_node.next
        raise ValueError("item was not found in list")


    def __findNode(self, quality):
        """this is a private function: will only use this within the class"""
        current_node = self.head
        while current_node != None:
            if quality(current_node.data):
                return current_node
            else: 
                current_node = current_node.next
        return None

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        found_node = self.__findNode(quality)
        return found_node.data if found_node else None

    def set(self, quality, value):
        found_node = self.__findNode(quality)
        """ Node does not exist, did not find it in the list"""
        if found_node is None:
            self.append(value)
            return None
        """ Update a node"""
        found_node.data = value
        return self


def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())


if __name__ == '__main__':
    test_linked_list()