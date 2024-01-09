def isValid(s: str) -> bool:
    stack_it = []

    for el in s:
        if el in ["(", "[", "{"]:
            stack_it.append(el)
            continue
        if len(stack_it) == 0:
            return False
        

        popped_el = stack_it.pop(len(stack_it)-1)
        if popped_el == "(" and el in ["}", "]"]:
            return False
        if popped_el == "[" and el in ["}", ")"]:
            return False
        if popped_el == "{" and el in [")", "]"]:
            return False
    return len(stack_it) == 0

print(isValid("(()}"))