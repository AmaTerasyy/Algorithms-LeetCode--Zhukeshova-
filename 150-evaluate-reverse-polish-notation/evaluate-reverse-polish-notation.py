class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            # если токен — оператор
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()  # второй операнд
                a = stack.pop()  # первый операнд

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    # деление с округлением к нулю
                    stack.append(int(a / b))
            else:
                # если число — добавляем в стек
                stack.append(int(token))

        return stack[0]