class MinStack:

    def __init__(self):
        self.stack = []      # основной стек
        self.min_stack = []  # стек минимумов

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # если стек минимумов пуст или новый элемент меньше/равен минимуму
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # если удаляемый элемент равен текущему минимуму
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]