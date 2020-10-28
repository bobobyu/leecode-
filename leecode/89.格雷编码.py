class Solution:
    def grayCode(self, n: int) -> list:
        if n:
            initial_res = [0, 1]
            for i in range(n-1):
                r = [eval(str(bin(i)) + '0') for i in initial_res]
                g = [eval(str(bin(i)) + '1') for i in initial_res[::-1]]
                initial_res = r + g
            return initial_res
        return [0]

