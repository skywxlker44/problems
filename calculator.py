class Calculator:
    def __init__(self, expr):
        self.expr = expr
        self.tokens = []
        self.ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
            "D": lambda x, y: x // y,
            "%": lambda x, y: x % y
            }

    def tokenize(self):
        num = ''
        prev_char = ''
        for i in self.expr.replace(" ", "").replace("//", "D"):
            if i.isdigit():
                num += i
            elif i in "+-" and (prev_char == "" or prev_char in "()+-*/%D"):
                num += i
            else:
                if num:
                    self.tokens.append(num)
                    num = ""
                self.tokens.append(i)
            prev_char = i
        if num:
            self.tokens.append(num)

    def eval_parentheses(self):
        stack = []
        for i, token in enumerate(self.tokens):
            if token == "(":
                stack.append(i)
            elif token == ")":
                start = stack[-1]
                end = i

                eval_res = self.eval_tokens(self.tokens[start+1:end])
                self.tokens = self.tokens[:start] + [str(eval_res)] + self.tokens[end + 1:]

                return self.eval_parentheses()
        return

    def eval_tokens(self, expr):
        i = 1
        while i < len(expr) - 1:
            if expr[i] in ("*", "/", "D", "%"):
                left = int(expr[i-1])
                right = int(expr[i+1])
                res = self.ops[expr[i]](left,right)
                expr = expr[:i-1] + [res] + expr[i+2:]
            else:
                i += 2

        i = 1
        while i < len(expr) - 1:
            if expr[i] in ("+", "-"):
                left = int(expr[i-1])
                right = int(expr[i+1])
                res = self.ops[expr[i]](left,right)
                expr = expr[:i-1] + [res] + expr[i+2:]
            else:
                i += 2
        return expr[0]

    def calculate(self):
        self.tokenize()
        self.eval_parentheses()
        return self.eval_tokens(self.tokens)


if __name__ == "__main__":
    expression = input("Expression: ")
    c = Calculator(expression)
    print(c.calculate())
