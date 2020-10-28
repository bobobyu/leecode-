# import random
#
#
# class Progress:
#     def __str__(self):
#         return f'{self.ID}\t\t\t' \
#                f'{self.ArriveTime}\t\t\t\t\t' \
#                f'{self.CPUTime}\t\t\t\t' \
#                f'{self.AllTime}\t\t\t\t' \
#                f'{self.Priority}\t\t' \
#                f'{self.State}'
#
#     def __init__(self, ID: int = -1):
#         self.ID = ID
#         self.Priority: int = random.randint(0, 10)
#         self.AllTime: int = random.randint(0, 200)
#         self.State: int = ProgressControlScheduling.READY
#         self.ArriveTime: int = 0
#         self.CPUTime: int = 0
#         self.Counter: int = 0
#         self.next: Progress = None
#
#
# class ProgressControlScheduling:
#     READY: int = 0
#     RUNNING: int = 1
#     BLOCK: int = 3
#     OVER: int = 4
#
#     def __init__(self, num_of_progress: int) -> None:
#         pre_PCB: Progress = Progress(ID=1)
#         self.head_PCB: Progress = pre_PCB
#         self.PCB_list: list = [pre_PCB]
#         for i in range(2, num_of_progress + 1):
#             next_PCB: Progress = Progress(ID=i)
#             self.PCB_list.append(next_PCB)
#             pre_PCB.next = next_PCB
#             pre_PCB = next_PCB
#
#     def _Display(self, head: Progress):
#         print(f'ID\t\tArriveTime\t\tCPUTime<Occupied>\t\tAllTime\t\tPriority\tState')
#         while head:
#             print(head)
#             head = head.next
#
#     def _sort_PCB(self, key: str, reverse: bool = False) -> list:
#         if key == 'AllTime':
#             return sorted(self.PCB_list, key=lambda x: x.AllTime, reverse=reverse)
#         else:
#             return sorted(self.PCB_list, key=lambda x: x.Priority, reverse=reverse)
#
#     def _FCFS(self):
#         head_PCB = self.head_PCB
#         pre_PCB: Progress = self.head_PCB
#         each_waiting_time: int = 0
#         total_waiting_time: int = 0
#         count_time: int = 0
#         while pre_PCB:
#             pre_PCB.State = ProgressControlScheduling.RUNNING
#             each_waiting_time += pre_PCB.AllTime
#             total_waiting_time += each_waiting_time
#             pre_PCB.CPUTime = pre_PCB.AllTime
#             pre_PCB.AllTime = 0
#             pre_PCB.State = ProgressControlScheduling.OVER
#             pre_PCB = pre_PCB.next
#             count_time += 1
#             print(f'{count_time} times executed algorithm. Show ready queue: ')
#             self._Display(head=pre_PCB)
#         print(f'The finish queue:')
#         self._Display(head=head_PCB)
#         print(f'The average time of each progress：{total_waiting_time / count_time}s.')
#         print(f'Total time of all progress：{total_waiting_time}s.')
#
#     def _SJ(self):
#         service_queue: list = self._sort_PCB(key='AllTime')
#         for progess
#
#
# test = ProgressControlScheduling(5)
# # test._Display(test.head_PCB)
# test._Display(test.head_PCB)
# test._FCFS()
