from typing import List

'''

实验中除循环首次适应算法采用循环双链表结构，其余只是普通的双链表结构。

'''


# 将每个内存定义为双向节点
class StorageNode:
    def __init__(self, start_address: int = None, length: int = None):
        self.start_address: int = start_address  # 起始地址
        self.length: int = length  # 可用的内存空间
        self.state = True  # 内存块使用状态
        self.next: StorageNode = None  # 前一个节点
        self.pre: StorageNode = None  # 后一个节点

    def _allocation_storage(self, allocation_length: int):  # 实现内存的分配功能
        if allocation_length <= self.length:
            self.length -= allocation_length  # 可用空间修改
            self.state = False if not self.length else True  # 改变内存块状态
            self.start_address += allocation_length  # 起始地址修改
            if not self.state:  # 如果没有可用的内存空间将此节点从链表中移除
                self.pre.next = self.next
                if self.next:
                    self.next.pre = self.pre


class ContinueStorageAllocationManagement:
    def __init__(self, file_name: str):
        self.storage_list: List[StorageNode] = []  # 定义一个和数组存储每个节点，在排序时使用
        self.work_dict: dict = {}  # 定义字典结构存储每个作业的状态
        with open(file_name) as f:  # 读取文件，组装链表
            for i in f.readlines():
                current_storage_list: list = [int(i) for i in i.split(' ')]
                if not self.storage_list:
                    head_node: StorageNode = StorageNode(start_address=current_storage_list[0],
                                                         length=current_storage_list[1])
                    previous_node: StorageNode = head_node
                    self.storage_list.append(previous_node)
                else:
                    current_node: StorageNode = StorageNode(start_address=current_storage_list[0],
                                                            length=current_storage_list[1])
                    previous_node.next = current_node
                    self.storage_list.append(current_node)
                    current_node.pre = previous_node
                    previous_node = current_node
        self.empty_node: StorageNode = StorageNode()  # 添加头节点方便删除操作
        head_node.pre = self.empty_node
        self.empty_node.next = head_node

        self.previous_node: StorageNode = self.storage_list[0]  # 上次查找到的空闲分区

        # [print(i.start_address, i.length) for i in self.storage_list]

    def continue_storage_allocation_management(self):
        print('''
        programmer: BoYu-Du
        by:2020/11/17
        summary:This program is used to simulate continuous storage allocation management.
        ''')
        allocation_function: dict = {
            1: self._first_fit_allocation_storage_space,
            2: self._best_fit_allocation_storage_space,
            3: self._worst_fit_allocation_storage_space,
            4: self._circle_first_fit_allocation,
            5: self._take_back_work,

        }

        while True:
            self._show_free_storage_information()
            if not allocation_function.get(choice := int(
                    input('1:first-fit\n2:best-fit\n3:worst-fit\n4:circle-first-fit\n5:take-back\n0:exit\n:'))):
                if not choice:
                    return
                else:
                    print('!!!Input error!!!')
            allocation_function[choice]()

    def _show_free_storage_information(self):
        print(f'<{"-" * 20}\tCurrent Free Table\t\t{"-" * 20}>')
        print('Start-Address\tLength\tState')
        head: StorageNode = self.empty_node
        while head:
            if head.length:
                print(f'{head.start_address}\t\t\t\t{head.length}\t\t{head.state}')
            head = head.next
        print(f'\n<{"-" * 20}\tCurrent Free Table\t\t{"-" * 20}>\n\n')

        print(f'<{"-" * 20}\tCurrent Allocated Table\t{"-" * 20}>')
        print('Start-Address\tLength\tWork-Name')
        for name, inf in self.work_dict.items():
            print(f'{inf["start_address"]}\t\t\t\t{inf["length"]}\t\t{name}')
        print(f'\n<{"-" * 20}\tCurrent Allocated Table\t{"-" * 20}>')

    def _circle_first_fit_allocation(self):  # 循环首次适应算法
        work_name, work_size = input('Please input work name and size of space:(split with space)').split(' ')
        work_size = int(work_size)

        # 由于其他几种算法没有适应循环结构，所把双链表升级为循环双链表
        self.storage_list[0].pre = self.storage_list[-1]
        self.storage_list[-1].next = self.storage_list[0]

        # 获取上次空闲分区的下一个分区的地址
        start_address: StorageNode = self.previous_node.next
        print(self.previous_node.start_address, start_address.start_address)

        # 可用内存块总个数(移动的步长)
        max_step: int = len([_ for _ in self.storage_list if _.state])
        print([_.start_address for _ in self.storage_list if _.state])
        # 查询下一个可用的内存
        while start_address.length < work_size and max_step:
            start_address = start_address.next
            max_step -= 1

        # 如果找到了就更新
        if max_step:
            start_address._allocation_storage(work_size)
            self.work_dict[work_name] = {'storage_address': start_address,
                                         'start_address': start_address.start_address - work_size,
                                         'length': work_size}
            self.previous_node = start_address  # 更新下一个起始地址
        # 没找到就报错
        else:
            print('!!!!Current don\'t have enough storage space to allocate.Please try again!!!!')

        # 由于其他几种算法没有适应循环结构，所以这里重新变为普通双链表
        self.empty_node.next = self.storage_list[0]
        self.storage_list[0].pre = self.empty_node
        self.storage_list[-1].next = None

    def search_available_storage_address(self, work_size, head_) -> list:  # 递归实现查询可用的空闲内存块的功能
        if head_.length >= work_size:  # 找到了可用的空闲内存块
            head_._allocation_storage(allocation_length=work_size)  # 调用内存分配功能
            return [True, head_, head_.start_address - work_size]  # 返回状态信息
        elif head_.next:
            return self.search_available_storage_address(work_size=work_size, head_=head_.next)
        else:  # 没有找到可用的空闲内存块
            return [False, None, None]

    def _first_fit_allocation_storage_space(self) -> None:  # 首次适应算法
        work_name, work_size = input('Please input work name and size of space:(split with space)').split(' ')
        work_size = int(work_size)
        flag, storage, start_address = self.search_available_storage_address(work_size=work_size,
                                                                             head_=self.empty_node.next)
        if not flag:
            print('!!!!Current don\'t have enough storage space to allocate.Please try again!!!!')
        else:
            # 更新作业字典
            self.work_dict[work_name] = {'storage_address': storage,
                                         'start_address': start_address,
                                         'length': work_size}
            # 更新上次使用的节点
            self.previous_node = storage

    def _best_fit_allocation_storage_space(self) -> None:
        sorted_list: List[StorageNode] = sorted(self.storage_list, key=lambda x: x.length)  # 在数组中对内存块的可用空间排序（同worst算法）
        work_name, work_size = input('Please input work name and size of space:(split with space)').split(' ')
        work_size = int(work_size)

        def search_available_storage_address(work_size: int) -> list:  # 直接遍历排序好的数组，查询是否有可用的内存空间（同worst算法）
            for storage in sorted_list:
                if storage.length >= work_size:  # 找到了可用的内存空间
                    storage._allocation_storage(work_size)  # 调用内存分配函数
                    return [True, storage, storage.start_address - work_size]
            return [False, None, None]

        flag, storage, start_address = search_available_storage_address(work_size=work_size)

        if flag:
            # 更新作业字典
            self.work_dict[work_name] = {'storage_address': storage,
                                         'start_address': start_address,
                                         'length': work_size}
            self.previous_node = storage  # 更新上次访问节点
        else:
            print('!!!!Current don\'t have enough storage space to allocate.Please try again!!!!')

    def _worst_fit_allocation_storage_space(self) -> None:
        sorted_list: List[StorageNode] = sorted(self.storage_list, key=lambda x: x.length, reverse=True)
        work_name, work_size = input('Please input work name and size of space:(split with space)').split(' ')
        work_size = int(work_size)

        def search_available_storage_address(work_size: int) -> list:
            for storage in sorted_list:
                if storage.length >= work_size:
                    storage._allocation_storage(work_size)
                    return [True, storage, storage.start_address - work_size]
            return [False, None, None]

        flag, storage, start_address = search_available_storage_address(work_size=work_size)

        if flag:
            self.work_dict[work_name] = {'storage_address': storage,
                                         'start_address': start_address,
                                         'length': work_size}
            self.previous_node = storage

        else:
            print('!!!!Current don\'t have enough storage space to allocate.Please try again!!!!')

    def _take_back_work(self):
        work_name: str = input('Please input witch work name you want to take back:')
        work_inf: dict = self.work_dict.get(work_name)
        if work_inf:
            storage_: StorageNode = work_inf['storage_address']
            length: int = work_inf['length']
            storage_.start_address -= length
            storage_.length += length  # 归还内存
            storage_.state = True  # 归还状态

            # 把该节点重新连接到链表
            storage_.pre.next = storage_
            if storage_.next:
                storage_.next.pre = storage_

            del self.work_dict[work_name]  # 在作业字典中移除该作业
        else:
            print('!!!!!Work name not exist!Please try again!!!!!')


'C:\\Users\\Administrator\\Desktop\\TestFile.txt'
s = ContinueStorageAllocationManagement(input('Input the file path:'))
s.continue_storage_allocation_management()
