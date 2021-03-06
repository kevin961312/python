class Contacts:
    all_contacts = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        #self.all_contacts.append(self)
        Contacts.all_contacts.append(self)


class AdressHolder:
    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contacts, AdressHolder):
    def __init__(self,name='',email='',phone='',street='', city='', state='', code=''):
        Contacts.__init__(self, name, email)
        AdressHolder.__init__(self, street, city, state, code)
        self.phone = phone

class Supplier(Contacts):
    def order(self,order):
        print("If this were real system we would send"
                "'{}' order to '{}'".format(order,self.name))

class MailSender:
    def send_email(self, email):
        print("Sending mail to "+self.email)
   
class EmailableContact(Contacts,MailSender):
    pass


contact = Contacts('Kevin Pineda','garfolks@gmail.com')
friend = Friend(name='Kevin Sebastian', email='kevin961312@gmail.com',phone ='7763395')
supplier = Supplier('Kevin Sebastian', 'kevin961312@gmail.com')


print(
    contact.name, contact.email, supplier.name, supplier.email
     )
print(contact.all_contacts)
print(supplier.all_contacts)
supplier.order('I need pliers')
print(friend.all_contacts)

email_1 = EmailableContact('Kevin Pineda','garfolks@gmail.com')
print(Contacts.all_contacts)
email_1.send_email("hello, test e-mail here")