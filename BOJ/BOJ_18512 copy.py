X, Y, P1, P2 = map(int, input().split())

# P1+X*i == P2+Y*j
i, j = 0
while True:
    V =P1+X*i
    W =P2*Y*j
    if V == W:
        print(i, j) 

