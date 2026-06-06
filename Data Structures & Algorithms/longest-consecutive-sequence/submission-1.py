class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        nums1=set()
        for val in nums:
            if val-1 in nums:
                continue
            else:
                nums1.add(val)
        best=0
        for val in nums1:
            length=1
            while val+length in nums:
                length+=1
            best=max(best,length)
        return best
