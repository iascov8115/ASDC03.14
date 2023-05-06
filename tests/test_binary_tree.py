import unittest

from src.classes.binary_tree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.tree = BinarySearchTree()

    def test_insert(self):
        test_array = [1, 2, 3, 4, 5]
        [self.tree.insert(el) for el in test_array]
        self.assertEqual(self.tree.inorder_traversal(), test_array)

    def test_remove_root(self):
        test_array = [1, 2, 3, 4, 5]
        [self.tree.insert(el) for el in test_array]
        self.tree.remove(1)
        self.assertEqual(self.tree.inorder_traversal(), test_array[1:])

    def test_remove_single_node_tree(self):
        self.tree.insert(5)
        self.tree.remove(5)
        self.assertEqual(self.tree.inorder_traversal(), [])

    def test_remove_leaf(self):
        test_array = [5, 3, 7]
        [self.tree.insert(el) for el in test_array]
        self.tree.remove(3)
        self.assertEqual(self.tree.inorder_traversal(), [5, 7])

    def test_remove_node_with_one_child(self):
        test_array = [5, 3, 7, 6]
        [self.tree.insert(el) for el in test_array]
        self.tree.remove(7)
        self.assertEqual(self.tree.inorder_traversal(), [3, 5, 6])

    def test_remove_node_with_two_children(self):
        test_array = [5, 3, 7, 6]
        [self.tree.insert(el) for el in test_array]
        self.tree.remove(5)
        self.assertEqual(self.tree.inorder_traversal(), [3, 6, 7])

    def test_search(self):
        test_array = [5, 3, 7]
        [self.tree.insert(el) for el in test_array]
        node, parent = self.tree.search(7)
        self.assertEqual(node.data, 7)
        self.assertEqual(parent.data, 5)

    def test_inorder_traversal(self):
        test_array = [10, 5, 4, 1, 8, 30, 40]
        [self.tree.insert(el) for el in test_array]
        self.assertEqual(self.tree.inorder_traversal(), [1, 4, 5, 8, 10, 30, 40])

    def test_preorder_traversal(self):
        test_array = [10, 5, 4, 1, 8, 30, 40]
        [self.tree.insert(el) for el in test_array]
        self.assertEqual(self.tree.preorder_traversal(), test_array)

    def test_postorder_traversal(self):
        test_array = [10, 5, 4, 1, 8, 30, 40]
        [self.tree.insert(el) for el in test_array]
        self.assertEqual(self.tree.postorder_traversal(), [1, 4, 8, 5, 40, 30, 10])


if __name__ == '__main__':
    unittest.main()
