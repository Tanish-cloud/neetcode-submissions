class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if stack and tokens[i]=='+':
                b=stack.pop()
                a=stack.pop()
                res=a+b
                stack.append(res)
            elif stack and tokens[i]=='-':
                b=stack.pop()
                a=stack.pop()
                res=a-b
                stack.append(res)
            elif stack and tokens[i]=='*':
                b=stack.pop()
                a=stack.pop()
                res=a*b
                stack.append(res)
            elif stack and tokens[i]=='/':
                b=stack.pop()
                a=stack.pop()
                res=int(a/b)
                stack.append(res)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]
            