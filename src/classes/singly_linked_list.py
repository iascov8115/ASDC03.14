class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def is_empty(self):
        return self.head is None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.last = new_node
            return

        self.last.next = new_node
        self.last = new_node

    def search(self, data):
        current = self.head
        while current and current.data != data:
            current = current.next
        return current if current and current.data == data else None

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def __str__(self):
        """__str__ method overloading for traverse and output

        :return: output string
        """
        if self.is_empty():
            return 'Empty'
        output = ''
        current = self.head
        while current:
            output += f"{current.data} "
            current = current.next
        return output

    def __len__(self):
        if self.is_empty():
            return 0
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next
        return counter

    def __getitem__(self, index: int):
        if self.is_empty():
            return None
        current = self.head
        for i in range(index):
            current = current.next
            if not current:
                return None
        return current

    def traversal(self):
        array = []
        current = self.head
        while current:
            array.append(current.data)
            current = current.next
        return array
