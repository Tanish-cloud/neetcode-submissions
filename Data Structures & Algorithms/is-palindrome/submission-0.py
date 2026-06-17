class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","")
        chars=[]
        for i in s:
            if i.isalnum():
                chars.append(i.lower())
        s="".join(chars)
        if s[0::]==s[::-1]:
            return True
        else:
            return False