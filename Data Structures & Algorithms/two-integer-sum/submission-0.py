class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in nums:
                j = nums.index(diff)

                if i < j:
                    return [i, j]
                elif i > j:
                    return [j, i]