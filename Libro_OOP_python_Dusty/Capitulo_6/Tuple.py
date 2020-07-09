stock = "FB0",75.00,75.03,74.90
stock_2 = ("FB0",75.00,75.03,74.90)
#
import datetime
def middle (stock, date):
    symbol,current, high, low = stock
    return ((high+low)/2, date)

mid_value, date = middle(stock_2, datetime.date(2014,10,31))
print(mid_value,date)
print(middle(stock_2, datetime.date(2014,10,31)))

print(stock[2])
print(stock[0:3])