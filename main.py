import csv

from src.classes.binary_tree import BinarySearchTree
from src.classes.singly_linked_list import SinglyLinkedList
from src.classes.student import Student


def prepare_data() -> list[Student]:
    reader = csv.DictReader
    data = Student.read_from_stream(filename='data/students_data.csv', reader=reader)
    return data


if __name__ == '__main__':
    students = prepare_data()

    l = SinglyLinkedList()
    [l.insert_at_end(student) for student in students[:50]]

    st = l[5].data

    print(l.traversal())
    print(len(l))
    search = l.search(st)
    print(search.data)
    l.delete(st)
    print(len(l))
    search = l.search(st)
    print(search)

    t = BinarySearchTree()
    [t.insert(student) for student in students[:50]]
    print(list(map(str, t.preorder_traversal())))
    print(list(map(str, t.inorder_traversal())))
    print(list(map(str, t.postorder_traversal())))
    search, _ = t.search(st)
    print(search.data)
    t.remove(search.data)
    search, _ = t.search(st)
    print(search)
