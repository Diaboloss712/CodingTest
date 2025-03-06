from collections import deque


class Node:
    def __init__(self, key, index):
        self.left = None
        self.right = None
        self.index = index
        self.key = key


class Tree:
    def __init__(self):
        self.root = None

    def insert_number(self, index, key):
        self._insert_number(index, key)

    def _insert_number(self, index, key):
        node = self.search(index)
        node.key = key

    def insert_operation(self, num, key, left_num, right_num):
        if self.root is None:
            self.root = Node(key, num)
        else:
            self.insert_number(num, key)
        self._insert_operation(num, left_num, right_num)

    def _insert_operation(self, parent_index, left_num, right_num):
        node = self.search(parent_index)
        node.left = Node(0, left_num)
        node.right = Node(0, right_num)

    def search(self, index):
        return self._search(self.root, index)

    def _search(self, node, index):
        if node is None:
            return -1
        queue = deque([node])
        while queue:
            node = queue.popleft()
            if node.index == index:
                return node
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return

    def calculate(self):
        self._calculate(self.root)
        return self.root.key


    def _calculate(self, node):
        if not node.left.key.isdigit():
            self._calculate(node.left)
        if not node.right.key.isdigit():
            self._calculate(node.right)
        node.key = operation(node.left.key, node.right.key, node.key)



def operation(num1, num2, oper):
    if oper == '-':
        return int(num1) - int(num2)
    if oper == '+':
        return int(num1) + int(num2)
    if oper == '*':
        return int(num1) * int(num2)
    if oper == '/':
        return int(num1) / int(num2)


for test_case in range(1, 11):
    N = int(input())
    t = Tree()
    for i in range(0, N):
        tree_input = list(map(str, input().split()))
        if not tree_input[1].isdigit():
            t.insert_operation(*tree_input)
        else:
            t.insert_number(*tree_input)
    answer = t.calculate()

    print(f'#{test_case} {int(answer)}')
