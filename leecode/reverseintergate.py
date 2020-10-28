class Solution:
    def reverse(self, x: int) -> int:
        if x > 9 or x < -9:
            x = [i for i in str(x)]
            low_index: int = 0
            height_index: int = len(x) - 1
            if x[low_index] == '-':
                low_index += 1
            while x[height_index] == '0':
                height_index -= 1
                x.pop(-1)
            while low_index < height_index:
                x[low_index], x[height_index] = x[height_index], x[low_index]
                low_index += 1
                height_index -= 1
            result = int(''.join(x))
            return result if result <= pow(2, 31) - 1 and result >= -pow(2, 31) else 0
        return x


a = Solution()
print(a.reverse(42804))
