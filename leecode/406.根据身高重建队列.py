from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        print(sorted(people))

s = Solution()
s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])