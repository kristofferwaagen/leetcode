class Solution:
    def merge_alternately(self, word_1: str, word_2: str) -> str:
        merged = []
        for i in range(max(len(word_1), len(word_2))):
            if i < len(word_1):
                merged.append(word_1[i])
            if i < len(word_2):
                merged.append(word_2[i])
        return ''.join(merged)

