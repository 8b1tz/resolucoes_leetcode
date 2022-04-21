from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.sort()
        if len(nums) == 0:
            return -1
        if nums.__contains__(target):
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
        else:
            indices_menor = [i for i in range(len(nums)) if nums[i] < target]
            indices_maior = [i for i in range(len(nums)) if nums[i] > target]
            if indices_menor:
                menor = indices_menor[-1]
                if menor == nums[-1]:
                    return len(nums) - 1
                else:
                    return menor + 1
            if indices_maior:
                maior = indices_maior[0]
                if maior == 0:
                    return 0
                else:
                    return maior - 1
