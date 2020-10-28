class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        public_prefix: str = ''
        for prefix_list in zip(*strs):
            if len(set(prefix_list)) == 1:
                public_prefix += prefix_list[0]
            else:
                break
        return public_prefix


s = Solution()
s.longestCommonPrefix(["flower", "flow", "flight"])
