class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*len(nums)
        suffix=[1]*len(nums)
        output=[1]*len(nums)
        p=1
        for i in range(len(nums)):
            prefix[i]=p
            p=p*nums[i]
        p=1
        for i in range(len(nums)-1,-1,-1):
            suffix[i]=p
            p=p*nums[i]
        for i in range(len(nums)):
            output[i]=prefix[i]*suffix[i]
        return output