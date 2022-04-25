class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        result = 0
        count = 1
        while result < num:
            result = count * count
            count += 1
        return num == result
