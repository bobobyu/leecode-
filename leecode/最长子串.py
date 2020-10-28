class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s:
            start_point: int = 0
            end_point: int = 0
            son_string: str = ''
            max_length: int = 1
            length_start: int = 0
            while end_point < len(s):
                new_str = s[end_point]
                if new_str in son_string:
                    move_index: int = son_string.find(new_str)
                    start_point += move_index + 1
                    length_start += move_index + 1
                    son_string = son_string[start_point:] + new_str
                    start_point = 0
                else:
                    son_string += s[end_point]
                    max_length = max(max_length, len(son_string))
                end_point += 1
            return max_length
        return 0


a = Solution()
print(a.lengthOfLongestSubstring("bbtablud"))
