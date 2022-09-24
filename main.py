class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        '''проверка стека на пустоту. Метод возвращает True или False.'''
        return self.stack == []

    def push(self, item):
        '''добавляет новый элемент на вершину стека. Метод ничего не возвращает.'''
        self.stack.append(item)

    def pop(self):
        '''удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека'''
        if self.isEmpty():
            return None
        removed = self.stack.pop()
        return removed

    def peek(self):
        '''возвращает верхний элемент стека, но не удаляет его. Стек не меняется.'''
        if self.isEmpty():
            return None
        return self.stack[-1]

    def size(self):
        '''возвращает количество элементов в стеке.'''
        return len(self.stack)


def is_balanced(string):
    if len(string) % 2 != 0:
        return 'Несбалансированно'
    brackets = {'(': ')', '{': '}', '[': ']'}
    my_stack = Stack()
    for bracket in string:
        if bracket in brackets:
            my_stack.push(bracket)
        elif bracket in brackets.values() and my_stack.isEmpty():
            return 'Несбалансированно'
        else:
            pop_bracket = my_stack.pop()
            if (pop_bracket, bracket) not in brackets.items():
                return 'Несбалансированно'
    if my_stack.isEmpty():
        return 'Сбалансированно'


if __name__ == '__main__':
    print(is_balanced('{{[[](())]}}'))
