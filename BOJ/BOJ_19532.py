

a, b, c, d, e, f = map(int, input().split())
x = ((e*c)-(b*f))/((e*a)-(b*d))
y = ((c*d)-(a*f))/((b*d)-(a*e))
print(int(x),int(y))

#연립방정식을 그대로 옮김
# ax + by = c *e     | aex + bey = ce
# dx + ey = f *b    -| bdx + bey = bf
#                      (ae-bd)x + (be-be)y = (ce - bf) 이런식으로 식을 만들어서 x로 정리하고 y로 정리해서 계산함
#이게 내가 할 수 있는 선에는 최선이었음

# for x in range(-999, 1000, 1):
#     for y in range(-999, 1000, 1):
#         ((e*a)-(b*d))*x == ((e*c)-(b*f))
#         print(x)