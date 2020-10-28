class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name[-1] == typed[-1] and name[0] == typed[0]:
            name_point: int = 0
            type_point: int = 0
            while name_point < len(name) and type_point < len(typed):
                print(name_point, type_point)
                if name[name_point] == typed[type_point]:
                    name_point += 1
                    type_point += 1
                else:
                    while type_point < len(typed) and typed[type_point] == typed[type_point - 1]:
                        type_point += 1
                    if type_point < len(typed) and name[name_point] == typed[type_point]:
                        continue
                    else:
                        return False
            if name_point != len(name):
                print('a')
                return False
            return True
        return False


s = Solution()
print(s.isLongPressedName("alex",
"alexxr"))
