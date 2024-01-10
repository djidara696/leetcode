from typing import List
import math

def evalRPN(tokens: List[str]) -> int:
    stack = []

    for el in tokens:
        if el.lstrip("-").isnumeric():
            stack.append(el)
        else:
            do_operation(stack, el)
    
    return int(stack[0])

def do_operation(stack: List[str], operator: str):
    second, first = get_last_two(stack)

    if operator == "+":
        stack.append(first + second)
    
    elif operator == "-":
        stack.append(first - second)
    
    elif operator == "*":
        stack.append(first * second)

    else:
        res = first/second
        if res >= 0:
            res = math.floor(res)
        else:
            res = math.ceil(res)
        stack.append(res)


def get_last_two(stack: List[str]) -> tuple:
    return int(stack.pop()), int(stack.pop())

if __name__ == "__main__":
    print(evalRPN(["2","1","+","3","*"]))
    print(evalRPN(["4","13","5","/","+"]))
    print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))