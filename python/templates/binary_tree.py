class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, data: int):
        self.root = Node(data)

    def insert(self, data):
        self.root = self._insert_helper(self.root, data)
        
    def inorder_traversal(self):
        result = []
        self._inorder_helper(self.root, result)
        return result

    def preorder_traversal(self):
        result = []
        self._preorder_helper(self.root, result)
        return result

    def postorder_traversal(self):
        result = []
        self._postorder_helper(self.root, result)
        return result
    
    def search(self, data):
        return self._search_helper(self.root, data)
    
    def height(self):
        return self._height_helper(self.root, 0)
    
    def _height_helper(self, node: Node, depth: int):
        left_depth = depth
        right_depth = depth
        if node is None:
            return depth
        
        if node.left != None:
            left_depth = left_depth + 1
            left_depth = self._height_helper(node.left, left_depth)

        if node.right != None:
            right_depth = right_depth + 1
            right_depth = self._height_helper(node.right, right_depth)

        return left_depth if left_depth > right_depth else right_depth
    
    def _search_helper(self, node: Node, data: int):
        if node is None: 
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_helper(node.left, data)
        elif data > node.data:
            return self._search_helper(node.right, data)

    def _insert_helper(self, node: Node, data: int):
        if node is None:
            return Node(data)
        
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_helper(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_helper(node.right, data)
        
        return node

    def _inorder_helper(self, node: Node, result: list):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.data)
            self._inorder_helper(node.right, result)

    def _preorder_helper(self, node: Node, result: list):
        if node:
            result.append(node.data)
            self._inorder_helper(node.left, result)
            self._inorder_helper(node.right, result)

    def _postorder_helper(self, node: Node, result: list):
        if node:
            self._inorder_helper(node.left, result)
            self._inorder_helper(node.right, result)    
            result.append(node.data)
