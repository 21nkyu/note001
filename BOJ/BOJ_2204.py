# https://www.acmicpc.net/problem/2204

import sys

while True:
    n = int(sys.stdin.rstrip())

    if n == 0:
        break
    box=[]    
    for _ in range(n):        
        
        m = sys.stdin.rstrip()
        box.append((m.lower(), m))
        box.sort()
    print(box[0][1])
       
    