class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        suffix_prefix: list = []
        current_string = ''
        for i in needle:
            current_string += i
            current_prefix = ''
            current_suffix = ''
            max_length: int = 0
            for j in zip(current_string[:-1], current_string[1:][::-1]):
                current_prefix += j[0]
                current_suffix = j[1] + current_suffix
                print(current_prefix, current_suffix)
                if current_suffix == current_prefix:
                    max_length = len(current_prefix)
            suffix_prefix.append(max_length)
        print(suffix_prefix)
s = Solution()
s.strStr('1','ababab')

def gen_next(template: str):
    i = 0
    j = -1
    next_val = [-1] * len(template)
    while i < len(template) - 1:
        # print(f'i={i}, j={j}, {template[:i+1]}', next_val)
        if j == -1 or template[i] == template[j]:
            i += 1
            j += 1
            next_val[i] = j
        else:
            j = next_val[j]
        # print(f'i={i}, j={j}, {template[:i+1]}', next_val)
        # print()
    return next_val


def KMP(m, p):
    next_ = gen_next(p)
    i = 0
    j = -1
    m_length = len(m)
    p_length = len(p)
    while i < m_length - 1:
        if j == -1 or m[i] == p[j]:
            i += 1
            j += 1
            if j == p_length:
                return i - j
        else:
            j = next_[j]
    return -1
