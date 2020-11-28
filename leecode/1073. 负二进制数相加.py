from typing import List


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_: int = sum([j*pow(-2, i) for i, j in enumerate(arr1)])
        arr2_: int = sum([j*pow(-2, i) for i, j in enumerate(arr2)])
        return [int(i) for i in bin(arr1_ + arr2_)[2:]]


