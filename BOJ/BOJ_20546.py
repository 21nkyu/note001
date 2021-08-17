# https://www.acmicpc.net/problem/20546

# money = int(input())
# stock = 0
# stock_prices = [i for i in map(int, input().split())]

# for stock_price in stock_prices:
#     if stock_price <= money:
#         get_stock = money // stock_price
#         print(f'{money} // {stock_price} = {stock}')
#         money = money % stock_price
#         print(f'{money} % {stock_price} = {money}')
#         stock += get_stock
#         print(f'money : {money}')
#         print(f'stock : {stock}')        
#         print("----------------")
#     elif stock_price > money:
#         money = money
#         stock = stock
#         print(f'money : {money}')
#         print(f'stock : {stock}')        
#         print("----------------")
# closings = stock_prices[-1]
# print(money + closings*stock)      
# # print(stock)
# # print(money)
# # print()

money = int(input())
poss = list(map(int, input().split()))

def jh():
    now_money = money
    now_stock = 0
    for pos in poss:
        now_stock += now_money // pos
        now_money = now_money %  pos        
        if now_money == 0:
            break
                       
    return now_money, now_stock


def sm():
    now_money = money
    now_stock = 0
    for i in range(len(poss)-4):
        if poss[i] < poss[i+1] < poss[i+2] < poss[i+3]:  #업 3일째에 판다  돈+ stock == 0
            now_money += now_stock * poss[i+3]
            now_stock = 0
        if poss[i] > poss[i+1] > poss[i+2] > poss[i+3]:  #다운 3일째 산다 돈- stock +
            now_stock += now_money // poss[i+3]
            now_money = now_money % poss[i+3]
    return now_money, now_stock


j_money, j_stock = jh()
closings_j = j_money + j_stock*poss[-1]

s_money, s_stock = sm()
closings_s = s_money + s_stock*poss[-1]

if closings_j > closings_s:
    print('BNP')
elif closings_j < closings_s:
    print('TIMING')
else:
    print('SAMESAME')
