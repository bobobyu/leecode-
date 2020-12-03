from typing import List
import gc
import _pickle as pickle
from progarmmer_declaration import writer_log


class FileCatalog:
    """
    文件目录结构

    文件名:    file_name
    文件扩展名:    expanded_name
    文件占用磁盘块的第一块:    disk_block_index
    文件大小：   file_size
    """

    def __init__(self):
        self.valid_sign: bool = True
        self.file_name: str = ''
        self.expanded_name: str = ''
        self.disk_block_index: int = -1
        self.occupy_disk_block_num: int = -1
        self.file_size: int = -1

    def set_catalog(self, file_name: str, exp_name: str, disk_index: int, occ_num: int, file_size: int):
        self.valid_sign: bool = False
        self.file_name: str = file_name
        self.expanded_name: str = exp_name
        self.disk_block_index: int = disk_index
        self.occupy_disk_block_num: int = occ_num
        self.file_size: int = file_size


class DiskBlock:
    """
    盘块结构

    位置示图：   map
    文件数量：   file_number

    """

    def __init__(self, disk_block_size: int = 3):
        self.map: List[int] = [0] * disk_block_size
        self.file_number: int


class DataBlock:
    """
    数据块

    数据块大小：  word
    指向下一个数据块：   next_data_block

    """

    def __init__(self, block_size: int = 64):
        self.word: List[str] = [' '] * block_size  # 申请数据块空间
        self.visited_sign: bool = False
        self.next_data_block: DataBlock = None
