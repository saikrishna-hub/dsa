
class Node:
    def __init__(self, data, next_element):
        self.data = data
        self.next = next_element


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list): # 1 2 3 4 5
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self): # 1 2 3 4 5
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at_index(self, index): # 1 2 3 4 5
        if index < 0 or index >= self.get_length():

            raise Exception('Invalid Index')
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at_index(self, index, data): # 1 2 3 4 5
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')
        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, value_after, data): # 1 2 3 4 5
        if self.head is None:
            return
        iter = self.head
        while iter:
            if iter.data == value_after:
                iter.next = Node(data, iter.next)
                break
            iter = iter.next
        else:
            raise Exception("No specified value")

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        iter = self.head
        while iter.next:
            if iter.next.data == data:
                iter.next = iter.next.next
                break
            iter = iter.next
        else:
            raise Exception("No value to delete")

    def print_list(self):
        if not self.head:
            print('Empty Linked List')
            return
        itr = self.head
        my_list = ''

        while itr:
            my_list += str(itr.data) + '--->'
            itr = itr.next
        print(my_list)


#
# l1 = Linkedlist()
# l1.insert_values([1, 2, 3, 4])
# l1.print_list()
# l1.remove_by_value(3)
# l1.print_list()
