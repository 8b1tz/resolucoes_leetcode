class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        while len(num) != 1:
            digitos = []
            digitos[:0] = str(num)
            soma = 0
            for digito in digitos:
                soma += int(digito)
            num = str(soma)
        return int(num)
