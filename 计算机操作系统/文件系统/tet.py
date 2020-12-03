from file_system import *

""""
    python通过pickle库将类写入磁盘时是通过了一定的协议对写入的内容进行了处理，
所以难以通过移动指针的准确定位文件目录，存放盘位示图，文件内容在磁盘中的头位
置。
    所以本次实验将建立两个模拟盘，第一个模拟盘存放文件目录和盘块位示图，而第二
个盘将存放文件内容。

"""


@writer_log(writer='BoYu-Du', summary='file system')
class FileSystem:

    def __init__(self):
        self.disk_block_size: int = 20  # 划分磁盘块大小
        self.each_block_size: int = 512  # 每块磁盘的大小(B)
        self.data_block_size: int = 5  # 每个数据块大小(B)

    def initial_system(self):
        disk_block: DiskBlock = DiskBlock(disk_block_size=self.disk_block_size)
        disk_block.map[0], disk_block.map[1] = 1, 1  # 初始化存放位示图的盘块
        file_catalog: FileCatalog = FileCatalog()  # 初始化文件目录

        with open('file_system', 'wb+') as f:  # 位示图盘块写入系统文件
            pickle.dump(disk_block, f)
            pickle.dump(file_catalog, f)
        with open('file_content', 'w+') as f:  # 申明文件内容空间
            f.write('' * (self.data_block_size * self.disk_block_size - 2))

        # 释放变量占用的内存
        # del disk_block
        # del file_catalog
        # gc.collect()

        print('！！！系统初始化成功！！！')

    def writefile(self):  # 将目录以及空闲盘块表写入磁盘
        with open('file_system', 'wb+') as f:
            pickle.dump(self.disk_block, f)
            pickle.dump(self.file_catalog, f)

    def make_file(self):
        # 反序列化，从磁盘读取位示图和文件目录
        with open('file_system', 'rb+') as f:
            disk_block: DiskBlock = pickle.load(f)
            file_catalog: FileCatalog = pickle.load(f)

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

        pre_block = head_block
        while pre_block and pre_block.visited_sign:
            # print(''.join(pre_block.word).rstrip(' '), text_length)
            pre_block = pre_block.next_data_block


s = FileSystem()
# s.initial_system()
s.make_file()
