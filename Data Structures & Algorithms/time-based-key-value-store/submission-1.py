class TimeMap:
    def __init__(self) -> None:
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key] = self.dict.get(key, []) + [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:

        items = self.dict.get(key, [])
        lo = 0
        hi = len(items) - 1
        result = -1

        while lo <= hi:
            mid = (hi - lo) // 2 + lo

            (v, t) = items[mid]

            if t <= timestamp:
                result = max(result, mid)
                lo = mid + 1
            else:
                hi = mid - 1

        return "" if result == -1 else items[result][0]
