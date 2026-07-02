class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for index, value in enumerate(nums):
            if value not in seen:
                seen[value] = []
            seen[value].append(index)

        l = list(seen.values())
        
        for i in l:
            if len(i) > 1:
                for j in range(1, len(i)):
                    if abs(i[j] - i[j-1]) <= k:
                        return True

        return False