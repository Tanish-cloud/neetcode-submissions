class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for words in strs :
           count=[0]*26
           for char in words:
                count[ord(char)-ord('a')]+=1
           key=tuple(count)
           seen.setdefault(key,[]).append(words)
        output_list=list(seen.values())
        return output_list