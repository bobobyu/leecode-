class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        n, up = len(S), 2147483647

        def get_list(start):
            # 判断前面两个数会不会超过上限
            if max(li) > up:
                return False

            # 遍历后面所有的字符串看看能不能组成斐波那契，
            # 如果 数超上限 或 最后一个数超字符串长度 或 字符串并不是下一个数 则直接跳出
            while start < n:
                now = li[-1] + li[-2]
                c = len(str(now))
                if now > up or start + c > n or int(S[start:start + c]) != now:
                    return False
                li.append(now)
                start += c
            return True

        for i in range(1, 11):
            # 这里让j取不到字符串末尾最后一位，顺便如果两个字符串有个是0开始的，直接只跑0的情况
            for j in range(1, min(11, n - i)):
                li = [int(S[:i]), int(S[i:i + j])]
                if get_list(i + j):
                    return li
                if S[i] == '0':
                    break
            if S[0] == '0':
                break
        return []


s = Solution()
print(s.splitIntoFibonacci("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"))
"539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
# [539834657, 21, 539834678, 539834699, 1079669377, 1619504076, 2699173453, 4318677529, 7017850982, 11336528511]
