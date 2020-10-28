class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sol: str = ''
        CF: int = 0
        for i, j in zip(num1[::-1], num2[::-1]):
            count_ = int(i) + int(j) + CF
            sol = str(count_ % 10) + sol
            CF = count_ // 10
        if len(num1) > len(num2):
            point = len(num2)
            while point < len(num1):
                count_ = int(num1[::-1][point]) + CF
                sol = str(count_%10) + sol
                CF = count_ // 10
                point += 1
            if CF:
                sol = '1' + sol
        elif len(num1) < len(num2):
            point = len(num1)
            while point < len(num2):
                count_ = int(num2[::-1][point]) + CF
                sol = str(count_%10) + sol
                CF = count_ // 10
                point += 1
            if CF:
                sol = '1' + sol
        else:
            if CF:
                sol = '1' + sol
        return sol
s = Solution()
print(s.addStrings('1',''))