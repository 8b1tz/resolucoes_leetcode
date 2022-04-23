from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        pattern_groups = defaultdict(list)
        for i, p in enumerate(pattern):
            pattern_groups[p].append(i)

        words = s.split(" ")
        words_group = defaultdict(list)

        for i, word in enumerate(words):
            words_group[word].append(i)

        return list(words_group.values()) == list(pattern_groups.values())


teste = Solution()
print(teste.wordPattern(pattern="abba", s="dog cat cat dog"))
