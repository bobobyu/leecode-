class Solution:
    def longestMountain(self, A: list) -> int:
        point: int = 1
        max_length: int = 0
        while point < len(A) - 1:
            left_point: int = point - 1
            right_point: int = point + 1
            if A[left_point] >= A[point] or A[right_point] >= A[point]:
                point += 1
                continue
            while left_point >= 0 and A[left_point] < A[left_point + 1] :
                left_point -= 1
            while right_point < len(A) and A[right_point] < A[right_point - 1] :
                right_point += 1
            max_length = max(max_length, right_point - left_point - 1)
            point = right_point
        return max_length


s = Solution()
print(s.longestMountain([0,1,2,3,4,5,4,3,2,1,0]))
