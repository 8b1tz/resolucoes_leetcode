class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lista_s = []
        lista_t = []
        lista_s[:0] = s
        lista_t[:0] = t
        lista_s.sort()
        lista_t.sort()
        return lista_t == lista_s