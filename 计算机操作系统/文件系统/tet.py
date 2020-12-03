from file_system import *

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
        self.each_block_size: int = 512  # 每块磁盘的大小(B)
        self.data_block_size: int = 5  # 每个数据块大小(B)
        self.file_catalog_size: int = 20  # 文件目录大小

    def initial_system(self):
        disk_block: DiskBlock = DiskBlock(disk_block_size=self.disk_block_size)
        disk_block.map[0], disk_block.map[1] = 1, 1  # 初始化存放位示图的盘块
        file_catalog: List[FileCatalog] = [FileCatalog() for _ in range(self.file_catalog_size)]  # 初始化文件目录

        with open('file_system', 'wb+') as f:  # 位示图盘块写入系统文件
            pickle.dump(disk_block, f)
            pickle.dump(file_catalog, f)
        with open('file_content', 'w+') as f:  # 申明文件内容空间
            f.write(' ' * (self.data_block_size * self.disk_block_size - 2))

        # 释放变量占用的内存
        # del disk_block
        # del file_catalog
        # gc.collect()

        print('！！！系统初始化成功！！！')

    def writefile(self) -> None:  # 将目录以及空闲盘块表写入磁盘
        with open('file_system', 'wb+') as f:
            pickle.dump(self.disk_block, f)
            pickle.dump(self.file_catalog, f)

    def make_file(self) -> None:
        # 反序列化，从磁盘读取位示图和文件目录
        with open('file_system', 'rb+') as f:
            disk_block: DiskBlock = pickle.load(f)
            file_catalog: List[FileCatalog] = pickle.load(f)

        # 查询有无空闲的文件目录
        if not any([i.valid_sign for i in file_catalog]):
            print('文件目录已满！！！请清理后再写入文件！！！')
            return

        # 申请数据块实例
        head_block = pre_block = DataBlock(block_size=self.data_block_size)

        block_point: int = 0  # 数据块文本指针
        block_count: int = 0  # 数据块计数器
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

                # 当填满一个数据块后，申请一个新的数据块。
                pre_block.visited_sign = True
                if block_point == self.data_block_size:
                    block_point = 0
                    block_count += 1
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
                    block_count += 1
                    pre_block.visited_sign = True
                    next_block: DataBlock = DataBlock(block_size=self.data_block_size)
                    pre_block.next_data_block = next_block
                    pre_block = next_block

        print(f'文本长度为：{text_length}')
        while pre_block and pre_block.visited_sign:
            print(''.join(pre_block.word).rstrip(' '), text_length)
            pre_block = pre_block.next_data_block

        file_name: str = input('请输入文件名称:')
        exp_name: str = input('请输入文件扩展名:')

        file_catalog_index, disk_index = 0, 0  # 文件目录序号，磁盘头序号

        # 查询空闲的文件目录
        for file_catalog_i, catalog in enumerate(file_catalog):
            if catalog.valid_sign:
                file_catalog_index = file_catalog_i
                break

        occupancy_size: int = int(com) + 1 if (com := text_length / self.each_block_size) - int(
            com) else 0  # 计算需要至少需要多少磁盘区域

        # 申请磁盘空间
        for empty_block_index, block_ in enumerate(disk_block.map[2:]):
            if not block_:
                valid_sign: bool = True
                for check_sign in range(empty_block_index, empty_block_index + occupancy_size):
                    if disk_block.map[check_sign]:
                        valid_sign = False
                        break
                if valid_sign:

                    # 设置文件目录
                    file_catalog[file_catalog_index].set_catalog(file_name=file_name, exp_name=exp_name,
                                                                 file_size=text_length, disk_index=empty_block_index,
                                                                 occ_num=occupancy_size)

                    # 修改磁盘位示图
                    disk_block.map[empty_block_index: empty_block_index + occupancy_size] = [1] * occupancy_size

                    print(
                        f'找到适配的磁盘空间，第一块序号：{empty_block_index},最后一块序号：{empty_block_index + occupancy_size - 1},'
                        f'开始将文本内容写入磁盘....')

                    with open('file_content', 'a+') as f:
                        f.seek(self.each_block_size * empty_block_index)  # 将指针移动到第一块空闲区域位置
                        while head_block and head_block.visited_sign:  # 将数据块中的内容写入
                            f.write(''.join(head_block.word).rstrip(' '))
                            head_block = head_block.next_data_block
                    print('！！！写入成功！！！')

        print('没有足够的磁盘空间！！！请清理文件后再创建文件！！')


s = FileSystem()
s.initial_system()
s.make_file()
