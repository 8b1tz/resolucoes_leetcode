from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maior = 0
        contador = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                contador += 1
            else:
                contador = 0
            if contador > maior:
                maior = contador
        return maior
