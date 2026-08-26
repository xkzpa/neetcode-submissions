class MinStack:

    def __init__(self):
        self.stack = []
        self.mn = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mn:
            if self.mn[-1] >= val:
                self.mn.append(val)
        else:
            self.mn.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.mn[-1] == val:
            self.mn.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mn[-1] if len(self.mn) > 0 else 0
