class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = Counter(nums)
        freq_arr = [[] for _ in range(len(nums) + 1)]
        for num, freq in hash_map.items():
            freq_arr[freq].append(num)
        res = []
        for i in range(len(freq_arr) - 1, 0, -1):
            for num in freq_arr[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
