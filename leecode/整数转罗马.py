


class Solution:
    def intToRoman(self, num: int) -> str:
        intToRoma = {1: 'I', 4: 'IV', 5: 'V',
                     9: 'IX', 10: 'X', 40: "XL",
                     50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
                     500: 'D', 900: 'CM', 1000: 'M'}
        roma_string: str = ''

        for i, j in zip(str(num), range(len(str(num)), -1, -1)):
            post = pow(10, j-1)
            head = int(i)
            current_string = intToRoma.get(head * post,
                                           head * intToRoma[post] if head < 5 else intToRoma[5*post] + (head-5) * intToRoma[
                                               post])
            roma_string += current_string

        return roma_string



a = Solution()
print(a.intToRoman(1984))
