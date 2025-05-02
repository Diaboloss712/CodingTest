class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.nodes = dict()
        self.root = None

    def insert(self, key, value, left=None, right=None):
        if key not in self.nodes:
            self.nodes[key] = Node(key, value)
        else:
            self.nodes[key].value = value

        if left:
            if left not in self.nodes:
                self.nodes[left] = Node(left, '')
            self.nodes[key].left = self.nodes[left]

        if right:
            if right not in self.nodes:
                self.nodes[right] = Node(right, '')
            self.nodes[key].right = self.nodes[right]

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end='')
            self.inorder(node.right)

for test_case in range(1, 11):
    N = int(input())
    tree = Tree()

    for _ in range(N):
        data = input().split()
        key = int(data[0])
        value = data[1]
        left = int(data[2]) if len(data) >= 3 else None
        right = int(data[3]) if len(data) == 4 else None
        tree.insert(key, value, left, right)

    tree.root = tree.nodes[1]
    print(f'#{test_case} ', end='')
    tree.inorder(tree.root)
    print()
