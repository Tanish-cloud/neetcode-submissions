class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for words in strs:
            key=tuple(sorted(words))
            seen.setdefault(key,[]).append(words)
        output_list=list(seen.values())
        return output_list
