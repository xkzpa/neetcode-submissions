class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        op_b = ['(', '{', '[']
        cl_b = [')', ']', '}']
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}',
            ')': '(',
            ']': '[',
            '}': '{'
        }
        r = []
        for c in s:
            if c in op_b:
                r.append(c)
            else:
                if len(r) == 0:
                    return False
                c1 = r.pop()
                if c1 != pairs.get(c):
                    return False
        if len(r) == 0:
            return True
        return False
