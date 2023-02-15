# Name:Brendan Cahill
# OSU Email: cahillbr@oregonstae.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 2/14/23
# Description:


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass

class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self.nxt = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)
        self.tail = SLNode(None)
        self._head.nxt = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self._head.nxt != self.tail:
            cur = self._head.nxt.nxt
            out = out + str(self._head.nxt.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.nxt
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self._head
        while cur.nxt != self.tail:
            cur = cur.nxt
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.nxt

    def recursive_add(self, n, value):
        if (n.nxt == self.tail):
            n.nxt = SLNode(value)
            n.nxt.nxt = self.tail
            return
        return self.recursive_add(n.nxt, value)

    def add_back(self, value: object) -> None:
        self.recursive_add(self._head, value)

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        p_node = SLNode(value)
        p_node.nxt = self._head.nxt
        self._head.nxt = p_node
        return

        pass

    def insert_back(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        newinput = SLNode(value)
        newinput.nxt = self.tail

        x = self._head
        while x.nxt != self.tail:
            x = x.nxt
        x.nxt = newinput
        return

        pass

    def insert_at_index(self, index: int, value: object) -> None:
        """
        TODO: Write this implementation
        """
        if index < 0:
            raise SLLException
        new_node = SLNode(value)
        node = self._head
        for i in range(index):
            if node.nxt is None and i + 1 < index:
                raise SLLException
            node = node.nxt
        new_node.nxt = node.nxt
        node.nxt = new_node

        pass

    def remove_at_index(self, index: int) -> None:
        """
        TODO: Write this implementation
        """
        # in the scenario that index < 0 or List is empty then raise Exception
        if index < 0 or self._head.nxt == self.tail:
            raise SLLException
        current = self._head.nxt
        previous = self._head

        counter = 0
        # iterate counter times
        while counter < index and current.nxt != self.tail:
            counter += 1
            previous = current
            current = current.nxt

        # check counter is equal to index or out of range
        if counter != index:
            raise SLLException

        previous.nxt = current.nxt
        return
        pass

    def remove(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        curr = self._head.nxt  #
        prev = self._head
        while curr:
            if curr.value == value:
                prev.nxt = curr.nxt
                # self._size -= 1
                return True
            prev = curr
            curr = curr.nxt
        return False
        pass

    def count(self, value: object) -> int:
        """
        TODO: Write this implementation
        """
        count = 0  # returns the quanttiy of overlapping substring
        node = self._head.nxt
        while node:
            if node.value == value:
                count += 1
            node = node.nxt
        return count
        pass

    def find(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        node = self._head.nxt  # returns quantity lowest index in position of substring and alternatively returns value -1
        while node:
            if node.value == value:
                return True
            node = node.nxt
        return False
        pass

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        TODO: Write this implementation
        """
        index = 0   # returns slice of string of argument from start to end, returns new string without modifying original
        new_lst = LinkedList()
        node = self._head.nxt
        while node and index < start_index:
            node = node.nxt
            index += 1
        while node and size > 0:
            new_lst.insert_back(node.value)
            node = node.nxt
            size -= 1
        return new_lst
        pass


if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
