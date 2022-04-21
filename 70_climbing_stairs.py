class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 2 or n == 1 or n == 0:
            return n
        atual, passo_1, passo_2 = 0, 1, 2
        for i in range(2, n):
            atual = passo_1 + passo_2
            passo_1 = passo_2
            passo_2 = atual
        return atual