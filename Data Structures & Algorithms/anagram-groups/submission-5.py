class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            count = [0] * 26  # a to z
            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            seen.setdefault(key, []).append(word)
        return list(seen.values())