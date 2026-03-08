def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}

    for ch in s:
        print(stack)
        if stack:
            if ch in pairs:
                if stack[-1] != pairs[ch]:
                    break
                stack.pop()
        else:
            stack.append(ch)

    # в конце стек должен быть пуст
    return len(stack) == 0

print(isValid("([])"))