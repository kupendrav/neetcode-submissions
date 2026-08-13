import bisect

class TimeMap:
    def __init__(self):
        # Each key maps to two parallel lists: timestamps and values
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {"timestamps": [], "values": []}
        self.store[key]["timestamps"].append(timestamp)
        self.store[key]["values"].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        timestamps = self.store[key]["timestamps"]
        values = self.store[key]["values"]

        # Binary search for rightmost timestamp <= query
        idx = bisect.bisect_right(timestamps, timestamp) - 1

        if idx >= 0:
            return values[idx]
        return ""
