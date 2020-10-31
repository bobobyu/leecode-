import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set_list: list = []
        self.index_dict: dict = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val not in self.index_dict:
            self.index_dict[val]: set = set()
        self.index_dict[val].add(len(self.set_list))
        self.set_list.append(val)
        return len(self.index_dict[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        index = self.index_dict.get(val)
        if index:
            index_replace = self.index_dict.get(val).pop()
            end_val = self.set_list[-1]
            self.index_dict[end_val].add(index_replace)
            self.index_dict[end_val].discard(len(self.set_list)-1)
            self.set_list[-1], self.set_list[index_replace] = self.set_list[index_replace], self.set_list[-1]
            self.set_list.pop(-1)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.set_list)


s = RandomizedCollection()
print(s.insert(0))
print(s.set_list, s.index_dict)
print(s.remove(0))
print(s.set_list, s.index_dict)
print(s.insert(2))
print(s.set_list, s.index_dict)
print(s.remove(0))
print(s.set_list, s.index_dict)
print(s.remove(0))
print(s.set_list, s.index_dict)
print(s.getRandom())
print(s.getRandom())
print(s.getRandom())
print(s.getRandom())
