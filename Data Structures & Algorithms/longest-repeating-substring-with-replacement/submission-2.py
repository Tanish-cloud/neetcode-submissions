class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right=0,0
        count={}
        max_length,max_freq=0,0
        while right<len(s):
            if s[right] not in count:
                count[s[right]]=0
            count[s[right]]+=1
            max_freq=max(max_freq,count[s[right]])
            while (right-left+1)-max_freq>k:
                count[s[left]]-=1
                left+=1
            max_length=max(max_length,right-left+1)
            right+=1
        return max_length