a, b, c, d, e, f = map(int, input().split())
for x in range(-999, 1000, 1):
    for y in range(-999, 1000, 1):
        (a*e-b*d)*x + (b*e-b*e)*y == (c*e - b*f)
        print(x, y)