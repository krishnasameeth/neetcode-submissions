class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))

            str_map[sorted_s].append(s)
        
        return list(str_map.values())