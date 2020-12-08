"""
用一个整数表示位示图
"""
file_catalog_size: int = 20
disk_map: int = 1 << file_catalog_size - 1
print(f'初始化位图,展示当前位示图：\t\t\t\t{bin(disk_map)[2:]}')
"""
1.标记位示图：
"""
# 对第1块分区进行标识：
disk_map += 1
print(f'对第1块分区进行标识,展示当前位示图：\t\t{bin(disk_map)[2:]}')
# 对第2块分区进行标识：
disk_map |= 1 << 1
print(f'对第2块分区进行标识,展示当前位示图：\t\t{bin(disk_map)[2:]}')
# 对第5块分区进行标识：
disk_map |= 1 << 4
print(f'对第5块分区进行标识,展示当前位示图：\t\t{bin(disk_map)[2:]}')
# 对第10块分区进行标识：
disk_map |= 1 << 9
print(f'对第10块分区进行标识,展示当前位示图：\t\t{bin(disk_map)[2:]}')
# 取消对第10块分区的标识：
disk_map &= 1 << 19 | 1 << 9 | 3
print(f'取消对第10块分区的标识,展示当前位示图：\t{bin(disk_map)[2:]}')


# # 取消对第5块分区的标识：
# disk_map &= 1 << 19 | 1 << 4 | 3
# print(f'取消对第5块分区的标识,展示当前位示图：\t{bin(disk_map)[2:]}')


def search_free_block(disk_map_: int, need_size: int, max_size: int) -> int:
    print(f'展示当前位示图：\t{bin(disk_map_ ^ 0xfffff)}, 需要申请的空间大小：{need_size}')
    point = 4
    count_: int = 0
    index_count: int = 3
    disk_map_ ^= 0xfffff
    while index_count < max_size:
        if disk_map_ | point:
            print(bin(disk_map_))
            print(bin(point), count_)
            count_ += 1
        else:
            count_ = 0
        if count_ - 1 == need_size:;;/
            print(bin(disk_map))
            print(f'已经申请到足够的空间，第一块地址为：{index_count - need_size + 1}')
            return index_count
        point <<= 1
        index_count += 1
    print('没有申请到足够的空间！')
    return -1


search_free_block(disk_map_=disk_map, need_size=8, max_size=file_catalog_size)
'''
10000000001000000011
111111110111111100
1111111110111111100


10000000001000000011
11111111111111111111
1111111110111111100

0b1111111110111111100
         0b1000000000
'''
