class MinStack:

    def __init__(self):
        self.min_val     = []
        self.stack       = []

    def push(self, val: int) -> None:

        self.stack.append(val)

        if not self.min_val:
            self.min_val.append(val)
            return 
        
        min_value = self.min_val[-1]        
        
        if val <= min_value:
            self.min_val.append(val)
        

    def pop(self) -> None:
        popped_val = self.stack.pop(len(self.stack) - 1)
        if popped_val == self.min_val[-1]:
            self.min_val = self.min_val[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
print(minStack.push(-2))
print(minStack.push(0) )
print(minStack.push(-3))
print(minStack.getMin()) # return -3
print(minStack.pop())
print(minStack.top())  #)   // return 0
print(minStack.getMin()) # // return -2