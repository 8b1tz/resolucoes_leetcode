class Solution:
    def toHex(self, num: int) -> str:
        for i in range(len(str(num))):
            16**i