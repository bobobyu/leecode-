class Solution:
    def compressString(self, S: str) -> str:
        compress_str:str = ''
        start_point = 0
        length = len(S) - 1
        if length<2:
            return S
        while start_point < length:
            num_count:int = 1
            while start_point < length and S[start_point] == S[start_point+1]:
                start_point += 1
                num_count += 1
            print(start_point)
            compress_str += f'{S[start_point]}{num_count}'
            start_point += 1
        if start_point==length and  S[start_point] != S[start_point-1]:
            compress_str += f'{S[start_point]}1'
        print(compress_str)
        return min(S, compress_str, key=len)
s = Solution()
s.compressString("ccc")
