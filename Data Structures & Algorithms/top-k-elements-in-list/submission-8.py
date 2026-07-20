class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        freq_arr = [[] for _ in range(len(nums) + 1)]
        res = []

        for num, count in freq_map.items():
            freq_arr[count].append(num)
        for i in range(len(freq_arr) - 1, 0, -1):
            for num in freq_arr[i]:
                if len(res) < k: 
                    res.append(num)
        
        return res
