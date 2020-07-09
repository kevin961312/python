stock = {
    "GOOG": (613.30,625.86,610.50),
    "MSFT": (30.25,30.70,30.19)}
print(stock)
stock.get("RIM","Not Found")
stock.setdefault("BBRY",(10.50,10.62,10.39))
print(stock)