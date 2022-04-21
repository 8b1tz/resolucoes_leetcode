from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if not str:
            return prefix
        elif len(strs) == 1:
            return strs[0]
        strs.sort()
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                prefix += x
            else:
                break
        return prefix
