from collections import *
import _heapq


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # senate = list(senate)
        # invalid_counter: dict = {'R': 0, 'D': 0}
        # valid_counter: Counter = Counter(senate)
        # while all(valid_counter.values()):
        #     for j, i in enumerate(senate):
        #         if i == 'D':
        #             if invalid_counter['D']:
        #                 invalid_counter['D'] -= 1
        #                 valid_counter['D'] -= 1
        #                 senate[j] = ''
        #             else:
        #                 invalid_counter['R'] += 1
        #         elif i=='R':
        #             if invalid_counter['R']:
        #                 invalid_counter['R'] -= 1
        #                 valid_counter['R'] -= 1
        #                 senate[j] = ''
        #             else:
        #                 invalid_counter['D'] += 1
        #         # print(i, valid_counter, invalid_counter, senate)
        #         if valid_counter['R'] == 0:
        #             return 'Dire'
        #         elif valid_counter['D'] == 0:
        #             return "Radiant"
        #
        # if valid_counter['D'] == valid_counter['R']:
        #     return 'Radiant' if senate[0] == 'R' else 'Dire'
        hr, hd = [], []
        for i, j in enumerate(senate):
            if j == 'D':
                hd.append(i)
            else:
                hr.append(i)



print(Solution().predictPartyVictory("DRDRR"))
