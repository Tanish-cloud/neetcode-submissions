class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right=0,0
        max_len=0
        seen={}
        while right<len(s):
            if s[right] not in seen:
                seen[s[right]]=right
                max_len=max(max_len,right-left+1)
            else:
                left=max(left,seen[s[right]]+1)
                seen[s[right]]=right
                max_len=max(max_len,right-left+1)
            right+=1
        return max_len