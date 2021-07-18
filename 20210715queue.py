class Stack:
    def __init__(self, n):                         #constructor : class를 호출할 때 실행하는 함수
        self.stack_list = [None for _ in range(n)] #입력받은 n, stack_list = n만큼 비어있는 리스트 생성
        self.stack_size = 0                        #stack_size = 0
                                                   #class를 호출 할때 마다 리셋됨?
    
    def push(self, num):
        self.stack_list[self.size()] = int(num)
        self.stack_size += 1
    
    def pop(self):
        if self.size() > 0:
            last_val = self.top()

            self.stack_list[self.size()-1] = None
            
            self.stack_size -= 1
            return last_val

            # self.stack_size -= 1
            # return self.stack_list[self.size()]
        
        return -1
    
    def size(self):         #stack_size와 연동
        return self.stack_size 

    def empty(self):
        if self.size() > 0:
            return 0                #false
        
        return 1

    def top(self):
        if self.size() > 0:
            return self.stack_list[self.size()-1] #인덱스를 반환 하기 때문에 size-1
        
        return -1

def run_cmd_with_stack(cmd, new_stack_list):
    cmd_type = cmd[0]

    if cmd_type == "push":
        _, num = cmd # num = cmd[1]
        new_stack_list.push(num)             #Stack(n) = new_stack_list = run_cmd_with_stack(command, new_stack_list)///// Stack(n).run_cmd_with_stack(command).push(num)
    elif cmd_type == "pop":                  #new_stack_list = Stak(n)을 실행한것
        print(new_stack_list.pop())    
    elif cmd_type == "size":
        print(new_stack_list.size())
    elif cmd_type == "empty":
        print(new_stack_list.empty())
    elif cmd_type == "top":
        print(new_stack_list.top())
    
    return new_stack_list

n = int(input())                   #n(input) = Stack(n) 으로 들어가 class를 호출하고 = constructor생성자 함수를 호출하고 = new_stack_list 인스턴스 생성 
new_stack_list = Stack(n)    #인스턴스 생성 (클래스를 받을 객체)

# class Stack:
#     def __init__(self, n):
#         self.stack_list = [None for _ in range(n)] #입력받은 n만큼 none을 집어넣는다
#         self.stack_size = 0                            이부분이 실행 되어 
#new_stack_list = [None] * n만큼 생성된다 [None,None,None,None,None,.......None,]

for _ in range(n):              #n번 반복해서 입력을 받고 def run_cmd_with_stack(cmd)로 작동한다
    # "push 2".split() => ["push", "2"]
    # "size".split() => ["size"]

    command = input().split()    #commnad를 입력 받는다
    new_stack_list = run_cmd_with_stack(command, new_stack_list)

    print(new_stack_list.stack_list)
    print(new_stack_list.size())