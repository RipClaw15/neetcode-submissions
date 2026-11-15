class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for w in strs:
            freq = [0] * 26
            for l in w:
            
                freq[ord(l)-ord('a')] += 1
                
            group[tuple(freq)].append(w)
        return list(group.values())