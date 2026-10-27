class TimeMap:

    def __init__(self):
        # hashmap of {key: {time, value}} ?
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            # list of tuples
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # all times are strictly increasing
        history = self.store.get(key, [])
        res = ""

        l = 0
        r = len(history) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            if history[mid][1] <= timestamp:
                res = history[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res