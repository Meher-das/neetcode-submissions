class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.minvalue = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minvalue:
            self.minvalue = val
        if self.minvalue != val:
            self.minstack.append(min(self.minvalue,val))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
