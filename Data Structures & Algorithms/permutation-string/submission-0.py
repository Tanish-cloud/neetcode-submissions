class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen={}
        k=len(s1)
        for index,value in enumerate(s1):
            if value not in seen:
                seen[value]=0
            seen[value]+=1
        check=s2[:k]
        seen2={}
        for index,value in enumerate(check):
            if value not in seen2:
                seen2[value]=0
            seen2[value]+=1
        if seen==seen2:
            return True
        left=0
        for right in range(k,len(s2)):
            if s2[right] not in seen2:
                seen2[s2[right]]=0
            seen2[s2[right]]+=1
            seen2[s2[left]]-=1
            if seen2[s2[left]]==0:
                del seen2[s2[left]]
            left+=1
            if seen==seen2:
                return True
        return False