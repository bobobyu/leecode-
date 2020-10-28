class Solution:
    def minimumOperations(self, leaves: str) -> int:
        flag: bool = False
        count_op: int = 0
        start_point: int = 0
        end_point: int = len(leaves) - 1


s = Solution()
print(s.minimumOperations('rrryyyyrryyrr'))
