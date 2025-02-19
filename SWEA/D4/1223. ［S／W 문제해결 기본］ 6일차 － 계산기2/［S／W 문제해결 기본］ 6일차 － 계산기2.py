class Stack:
    top = -1

    def __init__(self, size=100):
        self.size = size
        self.top = -1
        self.items = [None] * size

    def push(self, item):
        self.top += 1
        self.items[self.top] = item

    def pop(self):
        item = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        item = self.items[self.top]
        return item

    def is_empty(self):
        return self.top == -1


priority = {'(' : 5, ')' : 0, '*' : 2, '/' : 2, '-' : 1, '+' : 1}

for test_case in range(1, 11):
    N = int(input())
    string = list(map(str, input()))
    cal_list = []
    sub_list = Stack()
    for i in range(len(string)):
        if string[i].isdigit():
            cal_list.append(string[i])
        else:
            if sub_list.is_empty():
                sub_list.push(string[i])
            elif string[i] == ')':
                while sub_list.peek() != '(':
                    cal_list.append(sub_list.pop())
                cal_list.append(sub_list.pop())
            else:
                if sub_list.is_empty() or priority[string[i]] > priority[sub_list.peek()]:
                    sub_list.push(string[i])
                elif priority[string[i]] <= priority[sub_list.peek()]:
                    while not sub_list.is_empty() and priority[sub_list.peek()] >= priority[string[i]]:
                        cal_list.append(sub_list.pop())
                    sub_list.push(string[i])
    while not sub_list.is_empty():
        cal_list.append(sub_list.pop())

    sub_list = Stack()
    for char in cal_list:
        if char.isdigit():
            sub_list.push(char)
        elif char == '+':
            if sub_list.top < 1:
                flag = False
                break
            num1 = sub_list.pop()
            num2 = sub_list.pop()
            sub_list.push(int(num2) + int(num1))
        elif char == '*':
            if sub_list.top < 1:
                flag = False
                break
            num1 = sub_list.pop()
            num2 = sub_list.pop()
            sub_list.push(int(num2) * int(num1))
        elif char == '-':
            if sub_list.top < 1:
                flag = False
                break
            num1 = sub_list.pop()
            num2 = sub_list.pop()
            sub_list.push(int(num2) - int(num1))
        elif char == '/':
            if sub_list.top < 1:
                flag = False
                break
            num1 = sub_list.pop()
            num2 = sub_list.pop()
            sub_list.push(int(num2) // int(num1))
        elif char == '%':
            if sub_list.top < 1:
                flag = False
                break
            num1 = sub_list.pop()
            num2 = sub_list.pop()
            sub_list.push(int(num2) % int(num1))
    print(f'#{test_case} {sub_list.pop()}')
