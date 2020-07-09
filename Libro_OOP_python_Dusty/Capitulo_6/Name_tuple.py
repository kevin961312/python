from collections import namedtuple
Stock = namedtuple("Stock", "symbol current high low")
stock = Stock("FB", 75.00, high=75.03, low=74.90)
print(stock)
print(stock.high)
symbol, current, high , low = stock
print(current)
#namedtuple aren't inmutable
#stock.current = 78.6