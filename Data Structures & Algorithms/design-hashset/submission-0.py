class MyHashSet:

    def __init__(self):
        self.buckets = [0] * 1000000

    def add(self, key: int) -> None:
        self.buckets[key] = 1

    def remove(self, key: int) -> None:
        self.buckets[key] = 0

    def contains(self, key: int) -> bool:
        return bool(self.buckets[key])


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)