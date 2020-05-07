class Contacts:
    all_contacts = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        #self.all_contacts.append(self)
        Contacts.all_contacts.append(self)


class Supplier(Contacts):
    def order(self,order):
        print("If this were real system we would send"
                "'{}' order to '{}'".format(order,self.name))


contact = Contacts('Kevin Pineda','garfolks@gmail.com')
supplier = Supplier('Kevin Sebastian', 'kevin961312@gmail.com')

print(
    contact.name, contact.email, supplier.name, supplier.email
     )
print(contact.all_contacts)
print(supplier.all_contacts)
supplier.order('I need pliers')