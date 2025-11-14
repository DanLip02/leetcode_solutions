def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.lower().replace(" ", "").replace(',', "").replace(":","")
    print(s)
    low = 0
    high = len(s) - 1
    while low < high:
        if s[low] == s[high]:
            low += 1
            high -= 1
        else:
            return False
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))