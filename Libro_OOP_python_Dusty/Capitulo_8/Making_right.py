subtotal = 12.32
tax = subtotal * 0.07
total = subtotal + tax

print("Sub: ${0} Tax: ${1} Total: ${total}".format(subtotal, tax, total= total))


print("Sub: ${0:0.2f} Tax: ${1:0.2f} Total: ${total:0.3f}".format( subtotal, tax, total=total))

orders = [('burger',2,5),('fries',3.5,1),('cola',1.75,1)]
print('Product     Quantity     Price     Subtotal')
for product, price, quantity in orders:
    subtotal = price*quantity
    print('{0:10s}{1: ^9d}     ${2: <8.2f}${3: >7.2f}'.format(product,quantity,price,subtotal))


import datetime
print("{0:%Y-%m-%d %I:%M%p }".format(datetime.datetime.now()))

""" The most comprehensive instructions can
be found in PEP 3101 at http://www.python.org/dev/peps/pep-3101/, although
the details are a bit dry"""