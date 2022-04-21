from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        contador = Counter(nums)
        for k, v in contador.items():
            if v > len(nums)/2:
                return k
