class Queue:
    def __init__(self, n):
        self.que_list = [None for _ in range(n)]
        self.que_size = 0
        self.cnt = 0
    def push(self, num):
        self.que_list[self.size()] = int(num)
        self.que_size += 1
        self.cnt += 1
    
    def pop(self):
        if self.size() > 0:
            last_value = self.que_list[self.cnt - self.size()]
            self.que_list[self.cnt - self.size()] = None
            self.que_size -= 1
            return last_value
        return -1

        
    def size(self):
        return self.que_size
    
    def empty(self):
        if self.size() > 0:
            return 0
        return 1
    
    def front(self):
        return self.que_list[0]

    def back(self):
        return self.que_list[self.size()-1]
   


def run_que(command, new_que_list):
    cmd_type = command[0]
    if cmd_type == 'push':
        num = command[1]
        new_que_list.push(num)
    elif cmd_type == 'pop':
        print(new_que_list.pop())
    elif cmd_type == 'size':
        print(new_que_list.size())
    elif cmd_type == 'empty':
        print(new_que_list.empty())    
    elif cmd_type == 'front':
        print(new_que_list.front())    
    elif cmd_type == 'back':
        print(new_que_list.back())
    return new_que_list


#
n = int(input())
new_que_list = Queue(n)

for _ in range(n):
    command = input().split()
    new_que_list = run_que(command, new_que_list)

    print(new_que_list.que_list)
    #print(new_que_list.que_size)
