class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if char=='(':
                stack.append(')')
            elif char=='{':
                stack.append('}')
            elif char=='[':
                stack.append(']')
            else:
                if stack and stack[-1]==char:
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        return False