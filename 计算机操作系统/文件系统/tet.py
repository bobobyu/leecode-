from file_system import *
from typing import Set, Dict
import _pickle as pickle
from progarmmer_declaration import writer_log

""""

    python通过pickle库将python类写入磁盘时是通过了一些协议对写入的内容进行了处理，
所以难以通过移动指针的准确定位文件目录，存放盘位示图，文件内容在磁盘中的位置。
    所以本次实验将建立两个模拟盘，第一个模拟盘存放文件目录和盘块位示图，而第二
个盘将存放文件内容。

"""


@writer_log(writer='BoYu-Du', summary='file system')
class FileSystem:

    def __init__(self):
        self.disk_block_size: int = 20  # 划分磁盘块大小
        self.each_block_size: int = 1024  # 每块磁盘的大小(B)
        self.data_block_size: int = 64  # 每个数据块大小(B)
        self.file_catalog_size: int = 20  # 文件目录大小
        self.UIF: bool = False  # 无条件终止标志
        self.IF: bool = False  # 系统初始化标志
        self.program_dict: Dict[Callable[None]] = {
            0: self.initial_system,
            1: self.make_file,
            2: self.copy,
            3: self.type,
            4: self.delete_file,
            5: self.dir
        }

    def launch_file_system(self) -> None:
        print('正在启动文件系统....\n\n启动成功，请选择以下功能:（！！！！初次使用请先进行初始化！！！！）\n\n')
        print('\t0：初始化系统\t1：创建新文件\t2：复制文件\t3：打开文件\t4：删除文件\t5：打开文件目录\n\n')
        while (op := int(input('请选择:'))) in range(6):
            print('\t0：初始化系统\t1：创建新文件\t2：复制文件\t3：打开文件\t4：删除文件\t5：打开文件目录\n\n')
            if op != 0 and not self.IF:
                print('！！！！请先初始化系统！！！！\n\n')
                continue
            self.program_dict[op]()
            print('\n')

    def initial_system(self) -> None:
        if self.disk_block_size <= 2:
            print('！！！磁盘划分块数量不足！！！')
            self.UIF = True
            return
        disk_block: DiskBlock = DiskBlock(disk_block_size=self.disk_block_size)
        disk_block.map[0], disk_block.map[1] = 1, 1  # 初始化存放位示图的盘块
        file_catalog: List[FileCatalog] = [FileCatalog() for _ in range(self.file_catalog_size)]  # 初始化文件目录

        with open('file_system', 'wb+') as f:  # 位示图盘块写入系统文件
            pickle.dump(disk_block, f)
            end_index = self.check_space(end_index=f.tell(), start_index=0)
            pickle.dump(file_catalog, f)
            self.check_space(start_index=end_index, end_index=f.tell())

        with open('file_content', 'r+') as f:  # 申请文件内容空间
            f.seek(2 * self.each_block_size)
            f.write(' ' * (self.each_block_size * (self.disk_block_size - 2)))

        # 释放变量占用的内存
        # del disk_block
        # del file_catalog
        # gc.collect()

        self.IF = True
        print('！！！系统初始化成功！！！')

    def check_space(self, start_index: int, end_index: int) -> int:
        if self.each_block_size <= (end_index - start_index):
            print('！！磁盘空间不足！！无法存入磁盘位示图！!')
            self.UIF = True
        return end_index

    def writefile(self, disk_block: DiskBlock, file_catalog: List[FileCatalog]) -> None:  # 将目录以及空闲盘块表写入磁盘
        with open('file_system', 'wb+') as f:
            pickle.dump(disk_block, f)
            end_index = self.check_space(end_index=f.tell(), start_index=0)
            pickle.dump(file_catalog, f)
            self.check_space(start_index=end_index, end_index=f.tell())

    def make_file(self) -> None:

        # 反序列化，从磁盘读取位示图和文件目录
        with open('file_system', 'rb+') as f:
            disk_block: DiskBlock = pickle.load(f)
            file_catalog: List[FileCatalog] = pickle.load(f)

        # 查询有无空闲的文件目录
        if disk_block.file_number == self.file_catalog_size:
            print('文件目录已满！！！请清理后再写入文件！！！')
            return

        # 申请数据块实例
        head_block = pre_block = DataBlock(block_size=self.data_block_size)

        block_point: int = 0  # 数据块文本指针
        text_length: int = 0  # 文本长度计数
        while (text_content := input('请输入文件内容,按 @ 键保存且退出!\n：'))[-1] != '@':
            # print(text_content, text_content[-1])
            text_point: int = 0  # 文本指针
            text_length += len(text_content)

            while text_point < (size_ := len(text_content)):
                while block_point < self.data_block_size:
                    pre_block.word[block_point] = text_content[text_point]
                    text_point += 1
                    block_point += 1

                    if text_point >= size_:  # 文本长度小于数据块容量，退出循环。
                        break

                pre_block.visited_sign = True
                # 当填满一个数据块后，申请一个新的数据块。
                if block_point == self.data_block_size:
                    block_point = 0
                    next_block: DataBlock = DataBlock(block_size=self.data_block_size)
                    pre_block.next_data_block = next_block
                    pre_block = next_block

        # 填充最后一段数据
        text_point = 0
        text_length += len(text_content) - 1
        if text_content[0] != '@':
            while text_point < (size_ := len(text_content) - 1):
                while block_point < self.data_block_size:
                    pre_block.word[block_point] = text_content[text_point]
                    block_point += 1
                    text_point += 1
                    if text_point == size_:
                        break

                # 填满一个数据块，申请下一个
                pre_block.visited_sign = True
                if block_point == self.data_block_size:
                    block_point = 0
                    next_block: DataBlock = DataBlock(block_size=self.data_block_size)
                    pre_block.next_data_block = next_block
                    pre_block = next_block

        print(f'文本长度为：{text_length}')
        pre_block = head_block
        print('文本内容为:', end=' ')
        while pre_block and pre_block.visited_sign:
            print(''.join(pre_block.word).rstrip(' '), end='')
            pre_block = pre_block.next_data_block
        print()

        # 输入文件名，并查重
        name_list: Set[str] = {i.file_name + i.expanded_name for i in file_catalog}
        while (file_name := input('请输入文件名称:')) + (exp_name := input('请输入文件扩展名:')) in name_list:
            print('文件名已存在！！请重新输入！！')

        # 文件目录序号，磁盘头序号
        file_catalog_index, disk_index = 0, 0

        # 查询空闲的文件目录序号
        for file_catalog_i, catalog in enumerate(file_catalog):
            if catalog.valid_sign:
                file_catalog_index = file_catalog_i
                break

        occupancy_size: int = int(com) + 1 if (com := text_length / self.each_block_size) - int(
            com) else 0  # 计算需要至少需要多少磁盘区域

        # 申请磁盘空间
        for empty_block_index, block_ in enumerate(disk_block.map):
            if not block_:
                valid_sign: bool = True
                for check_sign in range(empty_block_index, empty_block_index + occupancy_size):
                    if disk_block.map[check_sign]:
                        valid_sign = False
                        break
                if valid_sign:  # 成功申请到空间

                    print(
                        f'找到适配的磁盘空间，第一块序号：{empty_block_index},最后一块序号：{empty_block_index + occupancy_size - 1}.\n'
                        f'开始将文本内容写入磁盘....')

                    # 设置文件目录
                    file_catalog[file_catalog_index].set_catalog(file_name=file_name, exp_name=exp_name,
                                                                 file_size=text_length, disk_index=empty_block_index,
                                                                 occ_num=occupancy_size)

                    # 修改磁盘位示图
                    disk_block.map[empty_block_index: empty_block_index + occupancy_size] = [1] * occupancy_size
                    # 文件数加一
                    disk_block.file_number += 1
                    # 将修改后的文件目录和位示图写入磁盘
                    self.writefile(file_catalog=file_catalog, disk_block=disk_block)

                    with open('file_content', 'r+') as f:
                        f.seek(self.each_block_size * empty_block_index, 0)  # 将指针移动到第一块空闲区域位置
                        while head_block and head_block.visited_sign:  # 将数据块中的内容写入
                            f.write(''.join(head_block.word).rstrip(' '))
                            head_block = head_block.next_data_block
                    print('！！！写入成功！！！')
                    return

        print('没有足够的磁盘空间！！！请清理文件后再创建文件！！')

    def type(self) -> None:
        print(f'>{"-" * 20}启动读取文件功能{"-" * 20}<')
        # 从磁盘上加载文件目录和位示图到内存
        with open('file_system', 'rb+') as f:
            disk_block: DiskBlock = pickle.load(f)
            if disk_block.file_number == 0:
                print('当前文件数为0！！！自动退出查询！！！')
                return
            file_catalog: List[FileCatalog] = pickle.load(f)
        name_list: Set[str] = {i.file_name + i.expanded_name for i in file_catalog}
        while (file_name := input('请输入文件名称:') + input('请输入文件扩展名:')) not in name_list:
            print('文件名不存在！！请重新输入！！')

        # 文件所处位置
        file_index: int = -1
        for i, j in enumerate(file_catalog):
            if j.file_name + j.expanded_name == file_name:
                file_index = i
                break

        # 序号对应的文件目录首地址
        current_file_catalog: FileCatalog = file_catalog[file_index]
        with open('file_content', 'r+') as f:
            f.seek(current_file_catalog.disk_block_index * self.each_block_size)  # 文件指针移动到第一块存储区域
            print(f'当前文件内容为：\n\n{f.read(current_file_catalog.file_size)}')  # 读取文件长度的数据
        print('\n！！读取完成！！')

    def dir(self) -> None:
        print(f'>{"-" * 20}启动读取文件目录功能{"-" * 20}<')
        # 从磁盘上加载文件目录和位示图到内存
        with open('file_system', 'rb+') as f:
            disk_block: DiskBlock = pickle.load(f)
            if (file_num := disk_block.file_number) == 0:
                print('当前文件数为0！！！自动退出打开功能！！！')
                return
            file_catalog: List[FileCatalog] = pickle.load(f)

        print(f'目前共有{file_num}个文件:')
        for i, file_c in enumerate(file_catalog):
            if not file_c.valid_sign:
                print(
                    f'文件序号：{i}\t文件名：{file_c.file_name}\t文件扩展名：{file_c.expanded_name}\n文件大小：{file_c.file_size}'
                    f'\t第一块磁盘序号：{file_c.disk_block_index}\t占用磁盘分区数：{file_c.occupy_disk_block_num}\n')

    def delete_file(self) -> None:
        print(f'>{"-" * 20}'
              f'启动删除文件功能'
              f'{"-" * 20}<')
        # 从磁盘上加载文件目录和位示图到内存
        with open('file_system', 'rb+') as f:
            disk_block: DiskBlock = pickle.load(f)
            if disk_block.file_number == 0:
                print('当前文件数为0！！！自动退出删除功能！！！')
                return
            file_catalog: List[FileCatalog] = pickle.load(f)

        # 搜寻需要删除的文件
        name_list: Set[str] = {i.file_name + i.expanded_name for i in file_catalog}
        while (file_name := input('请输入需要删除的文件名称:')) + (exp_name := input('请输入需要删除的文件扩展名:')) not in name_list:
            print('文件名不存在！！请重新输入！！')

        file_index: int = -1
        for j, i in enumerate(file_catalog):
            if i.file_name == file_name and i.expanded_name == exp_name:
                file_index = j
                break

        current_file_catalog: FileCatalog = file_catalog[file_index]
        text_length: int = current_file_catalog.file_size  # 获取文件长度
        disk_first_index: int = current_file_catalog.disk_block_index  # 第一块磁盘序号
        disk_space: int = current_file_catalog.occupy_disk_block_num  # 获取文件占用的磁盘数

        disk_block.map[disk_first_index:disk_first_index + disk_space] = [0] * disk_space  # 修改位示图
        disk_block.file_number -= 1  # 文件数减一
        current_file_catalog.delete_catalog()  # 删除文件目录

        self.writefile(disk_block=disk_block, file_catalog=file_catalog)
        with open('file_content', 'r+') as f:  # 删除磁盘内容
            f.seek(self.each_block_size * disk_first_index)
            f.write(' ' * text_length)
        print('！！！删除成功！！！')

    def copy(self) -> None:
        print(f'>{"-" * 20}'
              f'启动复制文件功能'
              f'{"-" * 20}<')
        # 从磁盘上加载文件目录和位示图到内存
        with open('file_system', 'rb+') as f:
            disk_block: DiskBlock = pickle.load(f)
            if disk_block.file_number == 0:
                print('当前文件数为0！！！自动退出复制！！！')
                return
            file_catalog: List[FileCatalog] = pickle.load(f)
            if disk_block.file_number == self.file_catalog_size:
                print('当前文件目录已满！！！自动退出复制！！！')
                return

        # 搜寻需要复制的文件
        name_list: Set[str] = {i.file_name + i.expanded_name for i in file_catalog}
        while (file_name := input('请输入需要复制的文件名称:')) + (exp_name := input('请输入需要复制的文件扩展名:')) not in name_list:
            print('文件名不存在！！请重新输入！！')

        file_index: int = -1
        for j, i in enumerate(file_catalog):
            if i.file_name == file_name and i.expanded_name == exp_name:
                file_index = j
                break

        current_file_catalog: FileCatalog = file_catalog[file_index]
        text_length: int = current_file_catalog.file_size  # 获取文件长度
        ori_disk_first_index: int = current_file_catalog.disk_block_index  # 原文件第一块磁盘序号
        disk_space: int = current_file_catalog.occupy_disk_block_num  # 获取文件占用的磁盘数
        # 申请磁盘空间
        for index, block in enumerate(disk_block.map):
            if not block:
                valid_sign: bool = True
                for i in range(index, index + disk_space):
                    if disk_block.map[i]:
                        valid_sign = False
                        break
                if valid_sign:  # 成功申请到空间

                    first_block_index = index
                    print('！！！成功申请到磁盘空间！！！')

                    while (file_name := input('请输入复制文件名称:')) + (exp_name := input('请输入复制文件扩展名:')) in name_list:
                        print('文件名已存在！！请重新输入！！')

                    # 申请文件目录

                    file_catalog_index: int = -1
                    for i, j in enumerate(file_catalog):
                        if j.valid_sign:
                            file_catalog_index: int = i
                            break

                    # 设置文件目录
                    file_catalog[file_catalog_index].set_catalog(file_name=file_name, exp_name=exp_name,
                                                                 file_size=text_length, disk_index=index,
                                                                 occ_num=disk_space)

                    # 修改磁盘位示图
                    disk_block.map[index: index + disk_space] = [1] * disk_space
                    # 文件数加一
                    disk_block.file_number += 1

                    # 将修改后的文件目录和位示图写入磁盘
                    self.writefile(file_catalog=file_catalog, disk_block=disk_block)

                    head = pre_block = DataBlock(block_size=self.data_block_size)  # 申请数据块

                    block_point: int = 0  # 数据块文本指针
                    start_address: int = ori_disk_first_index * self.each_block_size
                    with open('file_content', 'r+') as f:  # 将原文件内容写入数据块
                        f.seek(start_address)  # 文件指针移动到源文件的第一块存储区域

                        text_point: int = 0  # 文本指针
                        while text_point < text_length:
                            while block_point < self.data_block_size:
                                pre_block.word[block_point] = f.read(1)  # 读取一个字节的内容

                                block_point += 1
                                text_point += 1

                                f.seek(start_address + text_point)  # 指针移动一个字节
                                if text_point >= text_length:
                                    break
                            pre_block.visited_sign = True
                            if block_point == self.data_block_size:
                                block_point = 0
                                next_block: DataBlock = DataBlock(block_size=self.data_block_size)
                                pre_block.next_data_block = next_block
                                pre_block = next_block

                        # 将数据块中的内容写入磁盘
                        f.seek(first_block_index * self.each_block_size, 0)  # 文件指针移动到申请到空间的第一区域
                        while head and head.visited_sign:
                            f.write(''.join(head.word).rstrip(' '))
                            head = head.next_data_block
                        print('！！！复制成功！！!')
                        return

        print('没有足够的磁盘空间！！！请清理文件后再创建文件！！')


s = FileSystem()
s.launch_file_system()
