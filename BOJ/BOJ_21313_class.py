# # https://www.acmicpc.net/problem/21313


# def array():
#     a = [i for i in range(1,3)]
#     return a

# N = int(input())

# if N%2 == 0:
#     print(*array()*int(N//2))
    
# else:
#     print(*array()*int(N//2), 3)


class Octopus():
    def __init__(self, N):
        self.N = N

    def odd_num(self):
        print(*c()*int(self.N//2), 3)

    def even_num(self):
        print(*c()*int(self.N//2))


def c():
    a = [i for i in range(1, 3)]
    return a


N = int(input())

oper = Octopus(N)

if N%2 != 0:
    oper.odd_num()
else:
    oper.even_num()