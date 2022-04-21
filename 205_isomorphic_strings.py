class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letras_dict = {}

        if len(s) != len(t):
            return False

        for letra_1, letra_2 in zip(s, t):
            if letra_1 in letras_dict.keys() or letra_2 in letras_dict.values():
                continue
            else:
                letras_dict[letra_1] = letra_2

        result = ""
        try:
            for letra in s:
                result += letras_dict[letra]
        except KeyError:
            return False
        return result == t
