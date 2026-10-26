class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for i in strs:
            key = ''.join(sorted(i))
            if not key in words:
                words[key] = []

            words[key].append(i)
        
        return list(words.values())