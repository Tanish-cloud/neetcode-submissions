from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        output = []
        output1 = []
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        for bucket in buckets:
            bucket.sort()
        for bucket in buckets:
            output.extend(bucket)
        for i in range(len(output) - k, len(output)):
            output1.append(output[i])
        return output1
