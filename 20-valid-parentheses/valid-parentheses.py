class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # стек для хранения открывающих скобок
        
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            # если символ — закрывающая скобка
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                # если открывающая — кладём в стек
                stack.append(char)

        # если стек пуст — всё ок
        return len(stack) == 0