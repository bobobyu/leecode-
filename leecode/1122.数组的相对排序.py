class Solution:
    def relativeSortArray(self, arr1: list, arr2: list) -> list:
        arr1_dict:dict = {}
        for i in arr1:
            arr1_dict[i] = arr1_dict.get(i, 0) + 1
        new_arr1 = []
        print(arr1_dict)
        for i in arr2:
            new_arr1 += [i] * arr1_dict[i]
            print(new_arr1, i, arr1_dict[i])
            del arr1_dict[i]
        other_list = []
        for i, j in arr1_dict.items():
            other_list += [i]*j
        new_arr1 += sorted(other_list)
        return new_arr1

s = Solution()
print(s.relativeSortArray([2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31],
[2,42,38,0,43,21]))
