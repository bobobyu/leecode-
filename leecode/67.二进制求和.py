class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return eval('0b'+a) + eval('0b'+b)