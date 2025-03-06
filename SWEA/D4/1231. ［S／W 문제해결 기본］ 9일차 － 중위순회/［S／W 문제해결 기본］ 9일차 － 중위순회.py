class Node:
    def __init__(self, key, height, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value
        self.height = h


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key, height, value):
        if self.root is None:
            self.root = Node(key, height, value)
        else:
            self._insert(key, height, value)

    def _insert(self, key, height, value):
        node = self.search(key, height)
        if node.key * 2 == key:
            node.left = Node(key, height, value)
        else:
            node.right = Node(key, height, value)

    def search(self, key, height):
        if self.root == key:
            return self.root
        else:
            return self._search(self.root, key, height)

    def _search(self, node, key, height):
        if h > node.height + 1:
            temp_h = h
            temp_key = key
            while temp_h > node.height + 1:
                temp_h -= 1
                temp_key = temp_key // 2
            if node.key * 2 == temp_key:
                return self._search(node.left, key, h)
            else:
                return self._search(node.right, key, h)
        else:
            return node

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.value, end='')
            self._inorder(node.right)

for test_case in range(1, 11):
    N = int(input())
    tree = Tree()
    h = 0
    for i in range(1, N+1):
        char = list(input().split())
        if i >= 1 << h+1:
            h += 1
        tree.insert(i, h, char[1])
    print(f'#{test_case}', end=' ')
    tree.inorder()
