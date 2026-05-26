class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        key_values = self.store[key]

        start, end = 0, len(key_values) - 1
        result = ""
        while start <= end:
            mid = (start + end) // 2

            ts, val = key_values[mid]
            # T T T F 
            # invariant <=

            if ts <= timestamp:
                result = val
                start = mid + 1
            else:
                end = mid - 1
        
        return result

        
