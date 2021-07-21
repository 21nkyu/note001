import sys #sys.stdin.readline()
from collections import deque


class Qued:
    def __init__(self):
        self.array = deque()
    def push(self, num):
        self.array.append(num)
            
    def pop(self):
        if self.size() > 0 :
            self.popleft()
            return self.front()
        return -1
        
    def size(self):
        return self.len(self.array)
    
    def empty(self):
        if self.size() > 0:
            return 0
        return -1
    def front(self):
        if self.size() > 0:
            return self.array[0]
        return -1
    def back(self):
        if self.size() > 0:
            return self.array[-1]
        return -1
    


def run_deque(command, new_deque_list):
    cmd_type = command[0]
    
    if cmd_type == "push":
        run_deque.push()
    if cmd_type == "pop":
        print(run_deque.pop())
    if cmd_type == "size":
        print(run_deque.size())
    if cmd_type == "empty":
        print(run_deque.empty())
    if cmd_type == "front":
        print(run_deque.front())
    if cmd_type == "back":
        print(run_deque.back())
    return new_deque_list


n = int(input())
new_deque_list = Qued()
for _ in range(n):
    command = (input().split(), new_deque_list)