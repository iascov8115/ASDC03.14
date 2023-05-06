import unittest

from src.classes.singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = SinglyLinkedList()

    def test_insert(self):
        test_array = [1, 2, 3]
        [self.list.insert_at_end(el) for el in test_array]
        self.assertEqual(self.list.traversal(), test_array)

    def test_search(self):
        test_array = [1, 2, 3]
        [self.list.insert_at_end(el) for el in test_array]

        node = self.list.search(2)
        self.assertEqual(node.data, 2)

    def test_delete(self):
        test_array = [1, 2, 3]
        [self.list.insert_at_end(el) for el in test_array]

        self.list.delete(2)
        self.assertEqual(self.list.traversal(), [1, 3])

    def test_delete_head(self):
        test_array = [1, 2, 3]
        [self.list.insert_at_end(el) for el in test_array]
        self.list.delete(1)
        self.assertEqual(self.list.traversal(), [2, 3])

    def test_delete_tail(self):
        test_array = [1, 2, 3]
        [self.list.insert_at_end(el) for el in test_array]
        self.list.delete(3)
        self.assertEqual(self.list.traversal(), [1, 2])

    def test_traversal(self):
        test_array = [1, 2, 3, 4, 5]
        [self.list.insert_at_end(el) for el in test_array]
        self.assertEqual(self.list.traversal(), test_array)

    def test_traversal_for_empty_list(self):
        self.assertEqual(self.list.traversal(), [])


if __name__ == '__main__':
    unittest.main()
