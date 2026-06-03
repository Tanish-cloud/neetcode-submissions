class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in nums:
                if i!=nums.index(diff):
                    return [min(i,nums.index(diff)),max(i,nums.index(diff))]
            seen[nums[i]]=i
