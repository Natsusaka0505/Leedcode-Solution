from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq_word1 = Counter(word1)
        # print(freq_word1)
        freq_word2 = Counter(word2)

        sort_freq_word1 = sorted(freq_word1.values())
        # print(sort_freq_word1)
        sort_freq_word2 = sorted(freq_word2.values())

        key = set(freq_word1.keys()) == set(freq_word2.keys())

        return sort_freq_word1 == sort_freq_word2 and key


word1 = "cabbba"
word2 = "abbccc"

sol = Solution()
print(sol.closeStrings(word1, word2))
