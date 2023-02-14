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
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)
        self.tail = SLNode(None)
        self._head.next = self.tail

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
        if self._head.next != self.tail:
            cur = self._head.next.next
            out = out + str(self._head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self._head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    def recursive_add(self, n, value):
        if (n.next == self.tail):
            n.next = SLNode(value)
            n.next.next = self.tail
            return
        return self.recursive_add(n.next, value)

    def add_back(self, value: object) -> None:
        self.recursive_add(self._head, value)

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        primaryNode = SLNode(value)
        primaryNode.next = self._head.next
        self._head.next = primaryNode
        return

        pass

    def insert_back(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        newinput = SLNode(value)
        newinput.next = self.tail

        x = self._head
        while x.next != self.tail:
            x = x.next
        x.next = newinput
        return

        pass

    def insert_at_index(self, index: int, value: object) -> None:
        """
        TODO: Write this implementation
        """
        tmp = self.head

        while index != 0:
            tmp = tmp.next
            if tmp ==self.tail:
                raise SLLException()
            index -= 1
        if tmp == None:
            raise SLLException()

        x = SLNode(value)

        pass

    def remove_at_index(self, index: int) -> None:
        """
        TODO: Write this implementation
        """
        # if index is less than 0 or List is empty then raise Exception
        if index < 0 or self._head.next == self.tail:
            raise SLLException

        prev = self._head
        curr = self._head.next

        # counter
        counter = 0
        # iterate counter times
        while counter < index and curr.next != self.tail:
            counter += 1
            prev = curr
            curr = curr.next

        # check counter is equal to index
        # if not equal then index is out of range
        if counter != index:
            raise SLLException

        # remove the item by assigning new next
        prev.next = curr.next
        return
        pass

    def remove(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        if self._head.next == self.tail:
            raise SLLException()

        self._head.next = self._head.next.next
        pass

    def count(self, value: object) -> int:
        """
        TODO: Write this implementation
        """
        count = 0
        node = self._head.next
        while node:
            if node.value == value:
                count += 1
            node = node.next
        return count
        pass

    def find(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        node = self._head.next
        while node:
            if node.value == value:
                return True
            node = node.next
        return False
        pass

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        TODO: Write this implementation
        """
        new_list = LinkedList()
        node = self._head.next
        index = 0
        while node and index < start_index:
            node = node.next
            index += 1
        while node and size > 0:
            new_list.insert_back(node.value)
            node = node.next
            size -= 1
        return new_list
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
