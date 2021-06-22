"""
Node class used to build nodes
"""


class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    # Property used to set the return next node
    @property
    def next(self):
        return self.__next

    # Property used to set the next node reference, so it keeps private
    @next.setter
    def next(self, node):
        self.__next = node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


"""
Class used to create the LinkedList
"""


class LinkedList:
    def __init__(self):
        self.__head = None

    # append(data) is used to add a new node in the end os the LL
    def append(self, data):
        # Creating a new node with the data passed to the funciton
        new_node = Node(data)
        # Checking that the list is not empty, so we check the head, if it is the first Node
        # then we insert it as the head
        if self.__head is None:
            self.__head = new_node
            return
        # if the list is not empty it means the head node has a value, we store it into the last_node variable
        last_node = self.__head

        # we return the last node pointer until it is None that means the new node should be inserted
        # after the last node pointing to a None pointer
        while last_node.next():
            # we get the pointer part, not the data Node(data, pointer)
            last_node = last_node.next()
        # We do set the last node pointer to the new node
        last_node.next(new_node)

    def print_list(self):
        cur_node = self.__head
        while cur_node:
            print(cur_node.data())
            cur_node = cur_node.next()


Lista = LinkedList()
Lista.append(34)
Lista.print_list()
