class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        integers = {}

        for i in nums:
            if not i in integers:
                integers[i] = 0

            integers[i] += 1
        
        sorted_keys = sorted(integers, key=lambda x: integers[x], reverse=True)
        return sorted_keys[:k]