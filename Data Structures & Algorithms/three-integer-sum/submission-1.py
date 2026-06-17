class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen=set()
        output=[]
        target=0
        for i in range(len(nums)):
            left,right=i+1,len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if target==total:
                    seen.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif target>total:
                    left+=1
                else:
                    right-=1
        for i in seen:
            output.append(list(i))
        return output