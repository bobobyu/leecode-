class Solution:
    def isUnique(self, astr: str) -> bool:
        mark = 0
        for i in astr:
            move_step: int = ord(i) - 96
            if 1 << move_step & mark:
                return False
            else:
                mark |= 1 << move_step

        return True
