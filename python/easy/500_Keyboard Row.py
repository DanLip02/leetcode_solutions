class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        res = []
        for word in words:
            lower = set(word.lower())
            if lower <= row1 or lower <= row2 or lower <= row3:
                res.append(word)
        return res
