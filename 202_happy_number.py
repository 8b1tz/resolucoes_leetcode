class Solution:
    def isHappy(self, n: int) -> bool:
        somas = []
        while True:
            numeros = []
            for i in str(n):
                numeros.append(i)
            soma = sum(map(lambda x: int(x)**2, numeros))
            if soma != 1:
                if soma not in somas:
                    n = soma
                    somas.append(soma)
                else:
                    return False
            else:
                return True