class Stack:
    def __init__(self, n):
        self.stack_list = [None for _ in range(n)]
        self.stack_size = 0
    
    def push(self, num):
        self.stack_list[self.size()] = int(num)
        self.stack_size += 1

    def pop(self):
        if self.size() > 0:
            last_value = self.top()
            self.stack_list[self.size()-1] = None
            self.stack_size -= 1
            return last_value
        return -1
    
    def size(self):
        return self.stack_size

    def empty(self):
        if self.size() > 0:
            return 0
        return 1

    def top(self):
        if self.size() > 0:
           self.stack_list[self.size()-1]
           return self.stack_list[self.size()-1]

def run_cmd_with_stack(command, new_stack_list):
    cmd_type = command[0]

    if cmd_type == 'push':
        num = command[1]
        new_stack_list.push(num)
    elif cmd_type == 'pop':
        print(new_stack_list.pop())
    elif cmd_type == 'size':
        print(new_stack_list.size())
    elif cmd_type == 'empty':
        print(new_stack_list.empty())
    elif cmd_type == 'top':
        print(new_stack_list.top())
    return new_stack_list

n = int(input())
new_stack_list = Stack(n)

for _ in range(n):
    command = input().split()
    new_stack_list = run_cmd_with_stack(command, new_stack_list) #이부분이 잘 이해가 안감
