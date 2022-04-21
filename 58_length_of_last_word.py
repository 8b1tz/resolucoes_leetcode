class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.lstrip().rstrip().split()[-1])