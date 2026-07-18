class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val=0
        if len(self.minstack)==0:
            val1=float('inf')
            min_val=min(val,val1)
        else:
            min_val=min(val,self.minstack[-1])
        self.minstack.append(min_val)


    def pop(self) -> None:
        if len(self.stack)!=0 and len(self.minstack)!=0:
            self.stack.pop()
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
