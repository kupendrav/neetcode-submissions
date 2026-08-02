class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack = []


        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val,self.min_stack[-1]))
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None
        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None
