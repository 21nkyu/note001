# https://www.acmicpc.net/problem/3053

# 택시기하학에서 원 = 대각길이가 2r인 정사각형
import math

class Area():
    def tx(self, r):
        self.l = r
        return 2*self.l**2 

    def cc(self, r):
        self.r = r
        return math.pi*self.r**2


area = Area()

r = int(input())
print(f'{area.cc(r):.6f}')
print(f'{area.tx(r):.6f}')
