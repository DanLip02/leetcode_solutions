"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        # если закрывающая скобка
        if ch in pairs:
            # стек должен быть НЕ пуст
            if not stack:
                return False
            # и верх должен соответствовать паре
            if stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            # открывающая скобка
            stack.append(ch)

    # в конце стек должен быть пуст
    return len(stack) == 0