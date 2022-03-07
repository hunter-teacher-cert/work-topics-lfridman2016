#Program to predict whether the S&P 500 will go down or up
import random
stock_chain = {
    'down': ['down', 'down', 'up', 'up', 'down', 'down', 'down', 'up', 'down', 'up'],
    'up': ['up', 'up', 'up', 'up', 'down', 'up', 'down', 'up', 'down', 'up']
}

stock_market = [random.choice(list(stock_chain.keys()))]

for i in range(10):
    stock_market.append(random.choice(stock_chain[stock_market[i]]))

print(stock_market)