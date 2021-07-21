import sys #sys.stdin.readline()
from collections import deque


class Qued:
    def __init__(self):
        self.array = deque()
    
    def push(self, num):
        self.array.append(num)
            
    def pop(self):
        if self.size() > 0 :
            return self.array.popleft()
            
        return -1
        
    def size(self):
        return len(self.array)
    
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
    


def deque_run(command, new_deque_list):
    cmd_type = command[0]
    
    if cmd_type == "push":
        num = command[1]
        new_deque_list.push(num)
    if cmd_type == "pop":
        print(new_deque_list.pop())
    if cmd_type == "size":
        print(new_deque_list.size())
    if cmd_type == "empty":
        print(new_deque_list.empty())
    if cmd_type == "front":
        print(new_deque_list.front())
    if cmd_type == "back":
        print(new_deque_list.back())
    return new_deque_list


n = int(sys.stdin.readline())
new_deque_list = Qued()
for _ in range(n):
    command = (sys.stdin.readline().split())
    new_deque_list = deque_run(command, new_deque_list)
    print(new_deque_list.array)