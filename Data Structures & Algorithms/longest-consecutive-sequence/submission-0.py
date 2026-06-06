class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(set(nums))
        nums1=list(nums)
        best=0
        for i in range(len(nums1)):
            length=1
            j=i+1
            while j<len(nums1) and nums1[j]==nums1[j-1]+1:
                length+=1
                j+=1
            best=max(best, length)
        return best