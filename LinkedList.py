class Node:
    """
    A node class
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Linked list implementation using single nodes
    """
    def __init__(self):
        self.head = None

    def print_list(self):
        """
        Prints the single linked list content
        :return:
        """
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        """
        Adds a new node to the linked list
        :param data: the data to be hold by the new node
        :return:
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.print_list()