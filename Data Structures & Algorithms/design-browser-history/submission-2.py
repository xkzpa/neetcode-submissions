class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = homepage
        self.cursor = 0
        self.history = [homepage]

    def visit(self, url: str) -> None:
        self.curr = url
        if self.cursor == len(self.history) - 1:
            self.cursor += 1
        else:
            self.cursor += 1
            self.history = self.history[:self.cursor]
        self.history.append(url)

    def back(self, steps: int) -> str:
        if steps > len(self.history) - 1:
            return self.history[0]
        else:
            self.cursor -= steps
            if self.cursor < 0:
                self.cursor = 0
            self.curr = self.history[self.cursor]
            return self.curr
    
    def forward(self, steps: int) -> str:
        if self.cursor == len(self.history) - 1:
            return self.history[-1]
        else:
            self.cursor += steps
            if self.cursor > len(self.history):
                self.cursor = len(self.history) - 1
            self.curr = self.history[self.cursor]
            return self.curr
        