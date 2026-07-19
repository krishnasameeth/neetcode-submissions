class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        res = [[] for _ in range(len(nums)+1)]

        for num,count in freq.items():
            res[count].append(num)

        j = len(res)-1
        top_el = []
        while j > 0:
            for num in res[j]:
                if k != 0:
                    top_el.append(num)
                    k -= 1
            j -= 1
        
        return top_el