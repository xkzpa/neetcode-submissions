class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for i, t in enumerate(tokens):
            if t in ("+", "-", "*", "/"):
                tmp1 = result.pop()
                tmp2 = result.pop()
                if t == "+":
                    print('+', tmp1, '+', tmp2)
                    result.append(tmp1+tmp2)
                elif t == "-":
                    result.append(tmp2-tmp1)
                elif t == "*":
                    result.append(tmp2*tmp1)
                elif t == "/":
                    result.append(int(tmp2/tmp1))
            else:
                result.append(int(t))
        return int(result[0])