# https://www.acmicpc.net/problem/5585

# money = int(input())
# change = 1000 - money

# coins = [500, 100, 50 , 10 , 5, 1]

# coin_cnt = 0
# for coin in coins:    
#     plus_coin = change//coin 
#     change %= coin 
#     coin_cnt += plus_coin

# print(coin_cnt) 

# Recursion

money = int(input())
change = 1000 - money
coins = [500, 100, 50 , 10 , 5, 1]

def get_change(i, rest_of_change, coins):

    if i == len(coins):
        return 0 
    
    return rest_of_change//coins[i] + get_change(i + 1, rest_of_change % coins[i], coins)

print(get_change(0, change, coins))




# money = int(input())
# change = 1000 - money

# coins = [500, 100, 50 , 10 , 5, 1]

# coin_cnt = 0
# for coin in coins:
    
#     plus_coin = change//coin # 1
#     # print(plus_coin)
#     change %= coin # 120
#     # print(minus_money)
#     # change -= minus_money
#     # print(change)

#     coin_cnt += plus_coin


# print(coin_cnt) 


# coins = [500, 100, 50 , 10 , 5, 1]
# def get_coin(change, coin):
#     coin_cnt = 0
#     for coin in coins:
#         plus_coin = change//coin
#         minus_money = change % coin
    
#         coin_cnt += plus_coin
#         change -= minus_money
#     return coin_cnt, change

# cnt, _ = get_coin(change, coins)
# print(cnt)