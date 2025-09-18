def max_profit(prices):
    max_profit = 0
    min_price = 100000
    for price in prices:
        if price<min_price:
            min_price = price
        profit = price - min_price
        if profit>max_profit:
           max_profit = profit
    return max_profit

prices = [7,1,5,3,6,4]
print(max_profit(prices))
