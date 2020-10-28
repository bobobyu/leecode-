class Solution:
    def plusOne(self, digits: list) -> list:
        # sum_ = digits[-1] + 1
        # cf = sum_ // 10
        # digits[-1] = sum_ % 10
        # for i in range(len(digits)-2, -1, -1):
        #     sum_ = digits[i] + cf
        #     cf = sum_ // 10
        #     digits[i] = sum_ % 10
        # if cf:
        #     digits.insert(0, 1)
        # return digits
        string_num = int(''.join([str(i) for i in digits])) + 1
        return [int(i) for i in str(string_num)]

s = Solution()
print(s.plusOne([9,9,9]))