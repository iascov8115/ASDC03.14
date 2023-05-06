class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data <= node.data:
            if node.left:
                self._insert(node.left, data)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._insert(node.right, data)
            else:
                node.right = Node(data)

    def search(self, data):
        return self._search(self.root, data, None)

    def _search(self, node, data, parent):
        if not node:
            return None, None
        if data == node.data:
            return node, parent
        elif data < node.data:
            return self._search(node.left, data, node)
        else:
            return self._search(node.right, data, node)

    def remove(self, data):
        node, parent = self.search(data)
        if not node:
            return
        self._remove(node, parent)

    def _remove(self, node, parent):
        if node.left and node.right:
            successor, parent_of_successor = self._find_min(node.right, node)
            node.data = successor.data

            if parent_of_successor.left == successor:
                parent_of_successor.left = successor.right
            else:
                parent_of_successor.right = successor.right

        elif node.left or node.right:
            child = node.left if node.left else node.right

            if parent is not None:
                if parent.left == node:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child

        else:
            if parent is not None:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None

    def _find_min(self, node, parent):
        while node.left:
            parent = node
            node = node.left
        return node, parent

    def preorder_traversal(self):
        return self._preorder_traversal(self.root, [])

    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])

    def postorder_traversal(self):
        return self._postorder_traversal(self.root, [])

    def _preorder_traversal(self, node, result):
        if node:
            result.append(node.data)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.data)
            self._inorder_traversal(node.right, result)
        return result

    def _postorder_traversal(self, node, result):
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.data)
        return result
