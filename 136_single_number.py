from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = Counter(nums)
        for k, v in dict.items():
             if v == 1:
                return k