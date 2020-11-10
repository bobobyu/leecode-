class Solution:
    def wordBreak(self, s: str, wordDict: list) -> list:
        res: list = []
        length = len(s)
        obtainable_ = {i:1 for i in ''.join(wordDict)}
        for i in s:
            if i not  in obtainable_:
                return []
        def dp(word_list: list, current_string: list, next_index: int = 0):
            # print(current_string, next_index)
            if ''.join(current_string) == s:
                res.append(' '.join(current_string))
            else:
                for j in word_list:
                    match_index: int = 0
                    flag = True
                    for alpha in j:
                        if next_index + match_index >= length or alpha != s[next_index+match_index]:
                            flag = False
                            break
                        match_index += 1

                    flag and dp(word_list, current_string + [j], next_index+match_index)
        dp(word_list=wordDict[:], current_string=[])
        return res


s = Solution()
print(s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))


