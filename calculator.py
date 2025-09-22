operators = ["+", "-", "*", "/", "//", "%"]

def calculate():
    expression = input()
    expression = expression.split(" ")
    for i in range(len(expression)):
            element = expression[i]
            if "*" in element:
                first, second = element.split("*")
                first, second = int(first), int(second)
                expression[i] = str(first*second)
            elif "//" in element:
                first, second = element.split("//")
                first, second = int(first), int(second)
                expression[i] = str(first//second)
            elif "/" in element:
                    first, second = element.split("/")
                    first, second = int(first), int(second)
                    expression[i] = str(first/second)
            elif "%" in element:
                first, second = element.split("%")
                first, second = int(first), int(second)
                expression[i] = str(first%second)
    result = float(expression[0])
    for i in range(1, len(expression), 2):
         if expression[i] == "+":
              result += float(expression[i+1])
         else:
            result -= float(expression[i+1])
    return result


def main():
    print(calculate())


main()
