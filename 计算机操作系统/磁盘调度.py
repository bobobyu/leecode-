from typing import List
from progarmmer_declaration import writer_log

def show_information(scan_sequence: List[int], sum_search_length) -> None:
    print(f'\nDisk scan sequence:{scan_sequence}\nAverage search length:{sum_search_length / len(scan_sequence):.4f}\n')


def bubble_sort(list_: List[int]) -> None:
    length: int = len(list_)
    for i in range(length):
        for m in range(i + 1, length):
            if list_[i] > list_[m]:
                list_[i], list_[m] = list_[m], list_[i]

@writer_log(writer='BoYu-Du', summary='disk scheduling policy')
class Disk:
    def __init__(self):
        self.disk_sequence: List[int] = [int(i) for i in input('Please input disk sequence:').split(' ')]  # 磁盘请求序列
        self.sorted_sequence: list = self.disk_sequence.copy()
        bubble_sort(self.sorted_sequence)  # 排序后的磁道序列

    def launch_disk_dispatch(self):
        op_dict: dict = {
            1: self.first_come_first_server,
            2: self.shortest_seek_time_first,
            3: self.scan,
            4: self.circle_scan,
        }
        print(f'1.first_come_first_server\n'
              f'2.shortest_seek_time_first\n'
              f'3.scan_dispatch\n'
              f'4.circle_scan_dispatch\n'
              f'0:exit\n')

        while True:
            if not op_dict.get(op := int(input('Please choice algorithm:'))):
                return
            op_dict[op]()

    def first_come_first_server(self) -> None:
        next_magnetic_head: int = int(input('Please input current disk index:'))
        sum_search_length: int = 0
        for current_magnetic_head in self.disk_sequence:
            sum_search_length += abs(next_magnetic_head - current_magnetic_head)
            next_magnetic_head = current_magnetic_head
        show_information(scan_sequence=self.disk_sequence, sum_search_length=sum_search_length)

    def shortest_seek_time_first(self):

        next_magnetic_head: int = int(input('Please input current disk index:'))
        sum_search_length: int = 0

        for current_magnetic_head in self.sorted_sequence:
            sum_search_length += abs(next_magnetic_head - current_magnetic_head)
            next_magnetic_head = current_magnetic_head
        show_information(scan_sequence=self.sorted_sequence, sum_search_length=sum_search_length)

    def scan(self):
        sort_copy: List[int] = self.sorted_sequence.copy()
        start_index: int = len(sort_copy)
        current_magnetic_head = int(input('Please input current disk index:'))
        move_dir: bool = True if input(
            'Please input the direction of movable arm:(l -> inward, r -> outward)') == 'l' else False
        for i, j in enumerate(sort_copy):
            if j > current_magnetic_head:
                sort_copy.insert(i, current_magnetic_head)
                start_index = i
                break
        if start_index == len(sort_copy):
            sort_copy.append(current_magnetic_head)
        if move_dir:
            sort_copy = sort_copy[:start_index + 1][::-1] + sort_copy[
                                                            min(len(sort_copy) - 1, start_index + 1):len(sort_copy)]
        else:
            sort_copy = sort_copy[start_index:] + sort_copy[:max(0, start_index)][::-1]

        if move_dir and start_index == len(sort_copy) - 2:
            sort_copy.pop(-1)

        sum_search_length: int = 0
        for i in range(1, len(sort_copy)):
            sum_search_length += abs(sort_copy[i] - sort_copy[i - 1])
        show_information(sum_search_length=sum_search_length, scan_sequence=sort_copy[1:])

    def circle_scan(self):
        current_magnetic_head = int(input('Please input current disk index:'))
        sort_copy: List[int] = self.sorted_sequence.copy()
        start_index: int = len(sort_copy)
        sum_search_length: int = 0
        for i, j in enumerate(sort_copy):
            if j > current_magnetic_head:
                sort_copy.insert(i, current_magnetic_head)
                start_index = i
                break
        if start_index == len(sort_copy):
            sort_copy.append(current_magnetic_head)

        sort_copy = sort_copy[start_index:] + sort_copy[:start_index]
        for i in range(1, len(sort_copy)):
            sum_search_length += abs(sort_copy[i] - sort_copy[i - 1])
        show_information(sum_search_length=sum_search_length, scan_sequence=sort_copy[1:])


s = Disk()
s.launch_disk_dispatch()
