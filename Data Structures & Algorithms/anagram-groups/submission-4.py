class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_map = defaultdict(list)

        for s in strs:
            sorted_s = sorted(s)
            char_map[tuple(sorted_s)].append(s)
        
        return list(char_map.values())
        