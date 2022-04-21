class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            if s[i] == "I":
                if i + 1 != len(s):
                    if s[i + 1] == "V":
                        result += 4
                    elif s[i + 1] == "X":
                        result += 9
                    else:
                        result += 1
                else:
                    result += 1
            if s[i] == "V":
                if s[i - 1] == "I" and i != 0:
                    continue
                else:
                    result += 5
            if s[i] == "X":
                if s[i - 1] == "I" and i != 0:
                    continue
                if i + 1 != len(s):
                    if s[i + 1] == "L":
                        result += 40
                    elif s[i + 1] == "C":
                        result += 90
                    else:
                        result += 10
                else:
                    result += 10
            if s[i] == "L":
                if s[i - 1] == "X" and i != 0:
                    continue
                else:
                    result += 50
            if s[i] == "C":
                if s[i - 1] == "X" and i != 0:
                    continue
                if i + 1 != len(s):
                    if s[i + 1] == "D":
                        result += 400
                    elif s[i + 1] == "M":
                        result += 900
                    else:
                        result += 100
                else:
                    result += 100
            if s[i] == "D":
                if s[i - 1] == "C" and i != 0:
                    continue
                else:
                    result += 500
            if s[i] == "M":
                if s[i - 1] == "C" and i != 0:
                    continue
                else:
                    result += 1000
        return int(result)
