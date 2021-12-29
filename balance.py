from stack import Stack


def check_str(text):
    stack = Stack()
    delimiters = {"{": "}", "[": "]", "(": ")"}

    for str in text:
        if str in "{[(":
            stack.push(str)

        elif stack.data and str == delimiters[stack.data[-1]]:
            stack.pop()

        else:
            print("Несбалансированно")
            return False

    if stack.size() == 0:
        print("Сбалансированно")
        return True
