class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack:list = [num[0]]
        point = 1
        while point < len(num) and k:
            if num[point] >= stack[-1]:
                stack.append(num[point])
                point+=1
                continue
            while k and stack and stack[-1] > num[point]:
                # print(stack)
                stack.pop(-1)
                k -= 1
            stack.append(num[point])
            point += 1

        print(stack, k)
        stack += num[point:]
        while stack and stack[0] == '0':
            stack.pop(0)
        if len(stack) == k:
            return '0'
        if k:
            stack = stack[:len(stack) - k]
        return ''.join(stack) if stack else '0'

s =Solution()
print(s.removeKdigits('1123', 1))
