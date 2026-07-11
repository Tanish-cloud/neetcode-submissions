class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window,countT={},{}
        have=0
        res,reslen=[-1,-1],float("inf")
        left=0
        for index,value in enumerate(t):
            if value not in countT:
                countT[value]=0
            countT[value]+=1
        need=len(countT)
        for right in range(len(s)):
            if s[right] not in window:
                window[s[right]]=0
            window[s[right]]+=1
            if s[right] in countT and window[s[right]]==countT[s[right]]:
                have+=1
            while have==need:
                if (right-left+1)<reslen:
                    res=[left,right]
                    reslen=right-left+1
                window[s[left]]-=1
                if s[left] in countT and window[s[left]]<countT[s[left]]:
                    have-=1
                if window[s[left]]==0:
                    del window[s[left]]
                left+=1
        if reslen!=float("inf"):
            left,right=res
            res=s[left:right+1]
        else:
            return ""
        return res
