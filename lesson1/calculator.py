class Calculator:
    def __init__(self, expr):
        self.expr = expr.replace(" ", "")
        self.tokens = []
        self.ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
            "//": lambda x, y: x // y,
            "%": lambda x, y: x % y
            }

    def tokenize(self):
        num = ""
        prev_char = ""
        for char in self.expr:
            if char.isdigit():
                num += char
            elif char in "+-" and (prev_char == "" or prev_char in "+-*/%("):
                num += char
            else:
                if num:
                    self.tokens.append(int(num))
                    num = ""
                if char == "/" and prev_char == "/":
                    self.tokens = self.tokens[:-1]
                    self.tokens.append("//")
                else:
                    self.tokens.append(char)
            prev_char = char
        if num:
            self.tokens.append(int(num))

    def eval_parentheses(self):
        stack = []
        while "(" in self.tokens:
            for i, token in enumerate(self.tokens):
                if token == "(":
                    stack.append(i)
                elif token == ")":
                    start = stack.pop()
                    end = i

                    res = self.eval_tokens(self.tokens[start+1:end])
                    self.tokens = self.tokens[:start] + [res] + self.tokens[end+1:]
                    break

    def eval_tokens(self, expr):
        i = 1
        while i < len(expr) - 1:
            if expr[i] in ("*", "/", "//", "%"):
                left = expr[i-1]
                right = expr[i+1]
                res = self.ops[expr[i]](left, right)
                expr = expr[:i-1] + [res] + expr[i+2:]
            else:
                i += 2

        i = 1
        while i < len(expr) - 1:
            left = expr[i-1]
            right = expr[i+1]
            res = self.ops[expr[i]](left, right)
            expr = expr[:i-1] + [res] + expr[i+2:]
            i += 2

        return expr[0]

    def calculate(self):
        self.tokenize()
        self.eval_parentheses()
        return self.eval_tokens(self.tokens)


def main():
    c = Calculator("-3 + (2 * (-4 + 5) // 3) % 2")
    try:
        print(c.calculate())
    except Exception:
        print("Invalid expression")


if __name__ == "__main__":
    main()
