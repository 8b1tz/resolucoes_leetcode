class Solution:
    def findComplement(self, num: int) -> int:
        num = "{0:b}".format(num)
        numero = str(num).replace('0', '2').replace('1', '0').replace('2', '1')
        return int(numero, 2)