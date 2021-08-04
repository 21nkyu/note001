

a, b, c, d, e, f = map(int, input().split())
x = ((e*c)-(b*f))/((e*a)-(b*d))
y = ((c*d)-(a*f))/((b*d)-(a*e))
print(int(x),int(y))

#연립방정식을 그대로 옮김


# for x in range(-999, 1000, 1):
#     for y in range(-999, 1000, 1):
#         ((e*a)-(b*d))*x == ((e*c)-(b*f))
#         print(x)