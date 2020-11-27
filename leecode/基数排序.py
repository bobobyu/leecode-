from typing import List

bin_list: List[List[int]] = [[] for _ in range(10)]


def base_sort(bin_list,ori_list: List[str], pos: int = -1) -> List[str]:
    if abs(pos) < max_len+1:
        for i in ori_list:
            bin_list[int(i[pos]) if abs(pos) < len(i) +1 else 0].append(i)
        ori_list.clear()
        for i in bin_list:
            if i:
                ori_list += i
        [bin_list[i].clear() for i in range(10)]
        return base_sort(ori_list=ori_list, pos=pos - 1, bin_list=bin_list)
    else:
        return ori_list

ori_list: List[str] = [str(i) for i in [1,0, 22, 33, 444, 555, 32, 12, 23]]
max_len = len(max(ori_list, key=len))
print(base_sort(ori_list=ori_list, bin_list=bin_list))
