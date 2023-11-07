
class Node:
    def __init__(self, data, next_element, prev):
        self.data = data
        self.next = next_element
        self.prev = prev


class DoubleLinkedlist:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        last = self.get_last_node()
        itr = last
        list_str = ''
        while itr:
            list_str += str(itr.data) + '-->'
            itr = itr.prev
        print(list_str)


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def insert_at_begining(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('No valid index range')

        if index == 0:
            self.insert_at_begining(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count+=1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_value_index(self, index):
        if self.head is None:
            raise Exception('Empty list can\'t be indexed')

        if index < 0 or index >= self.get_length():
            raise Exception('Index out of range')
        count = 0
        itr = self.head
        while itr:
            if count == index:
                val = itr.data
                break
            itr = itr.next
            count+=1
        return val






l1 = DoubleLinkedlist()
l1.insert_values([1, 2, 3, 4])
# l1.print_backward()
# l1.remove_by_value(3)
print(l1.get_value_index(3))
