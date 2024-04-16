#first implementation
"""task"""
from collections import defaultdict, deque

class FreqStack:
    """created new class"""
    def __init__(self):
        """init"""
        self.stack = deque()
        self.freq = defaultdict(int)
        self.num = defaultdict(deque)
        self.count = 0

    def push(self, val: int) -> None:
        """push"""
        self.freq[val] += 1
        freq = self.freq[val]
        self.num[freq].append(val)
        self.count = max(self.count, freq)

    def pop(self) -> int:
        """pop"""
        val = self.num[self.count].pop()
        if not self.num[self.count]:
            self.count -= 1
        self.freq[val] -= 1
        return val

#second implementation(additional)
# class FreqStack:
#     def __init__(self):
#         self.l1 = []
#         self.d1 = {}
        

#     def push(self, val: int) -> None:
#         self.l1.append(val)
#         if val in self.d1:
#             self.d1[val] += 1
#         else:
#             self.d1[val] = 1

#     def pop(self) -> int:
#         max = 0
#         for key, value in self.d1.items():
#             if max < value:
#                 max = value
#         index = len(self.l1) - 1
#         while index >= 0:
#             val = self.l1[index]
#             if self.d1[val] == max:
#                 res = self.l1[index]
#                 self.d1[val] -= 1
#                 del self.l1[index]
#                 return res
#             index -= 1