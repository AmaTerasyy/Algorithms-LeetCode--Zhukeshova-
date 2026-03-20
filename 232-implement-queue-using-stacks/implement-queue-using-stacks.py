class MyQueue:

    def __init__(self):
        self.in_stack = []   # стек для добавления
        self.out_stack = []  # стек для извлечения

    def push(self, x: int) -> None:
        # просто добавляем в входной стек
        self.in_stack.append(x)

    def pop(self) -> int:
        # если выходной стек пуст — переносим элементы
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        return self.out_stack.pop()

    def peek(self) -> int:
        # аналогично pop, но не удаляем элемент
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        return self.out_stack[-1]

    def empty(self) -> bool:
        # очередь пуста, если оба стека пусты
        return not self.in_stack and not self.out_stack