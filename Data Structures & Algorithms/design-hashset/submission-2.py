class MyHashSet:
    # lets use a hash function instead
    def __init__(self):
        self.buckets = [[] for _ in range(10000)]

    def __hash(self, key: int) -> int:
        return key % 10000

    def add(self, key: int) -> None:
        if key not in self.buckets[self.__hash(key)]:
            self.buckets[self.__hash(key)].append(key)
        

    def remove(self, key: int) -> None:
        if key in self.buckets[self.__hash(key)]:
            self.buckets[self.__hash(key)].remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.buckets[self.__hash(key)]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)