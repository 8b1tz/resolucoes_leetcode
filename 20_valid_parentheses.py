class Solution:
    def isValid(self, s: str) -> bool:
        left = []
        retorno = []
        if len(s) <= 1:
            return False
        for c in s:
            try:
                if c in ['(', '[', '{']:
                    left.append(c)
                elif c == ')' and left != 0 and left[-1] == '(':
                    retorno.append(True)
                    left.pop()
                elif c == ']' and left != 0 and left[-1] == '[':
                    retorno.append(True)
                    left.pop()
                elif c == '}' and left != 0 and left[-1] == '{':
                    retorno.append(True)
                    left.pop()
                else:
                    return False
            except IndexError:
                return False
        if len(retorno) == 0 or len(retorno) != len(s)/2:
            return False
        else:
            return True