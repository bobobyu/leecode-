class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        numDict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        length_num1:int = len(num1)
        length_num2:int = len(num2)
        n1 = 0
        n2 = 0
        for i, j in enumerate(num1):
            n1 += pow(10,(length_num1 - i - 1)) * numDict[j]
        for i, j in enumerate(num2):
            n2 += pow(10,(length_num2 - i - 1)) * numDict[j]
        return str(n1*n2)
s = Solution()
s.multiply('12','34')
