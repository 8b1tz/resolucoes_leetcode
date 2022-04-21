from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lista = [
            [i, j]
            for i in range(len(nums))
            for j in range(i + 1, len(nums))
            if nums[i] + nums[j] == target
        ][0]
        return lista
