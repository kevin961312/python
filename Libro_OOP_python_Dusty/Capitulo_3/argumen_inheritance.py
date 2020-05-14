class Contacts:
    all_contacts = []
    def __init__(self, name='', email='',**kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        #self.all_contacts.append(self)
        Contacts.all_contacts.append(self)
        print(**kwargs)


class AdressHolder:
    def __init__(self, street='', city='', state='', code='',**kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contacts, AdressHolder):
    def __init__(self,phone,**kwargs):
        super().__init__(**kwargs)
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
friend = Friend(phone= 7763395, name='Kevin Sebastian' )
supplier = Supplier('Kevin Sebastian', 'kevin961312@gmail.com')
adress = AdressHolder()


print(
    contact.name, contact.email, supplier.name, supplier.email
     )
print(contact.all_contacts)
print(supplier.all_contacts)
supplier.order('I need pliers')
print(friend.all_contacts)
print(friend.__dict__)
print(contact.__dict__)
print(supplier.__dict__)
print(adress.__dict__)

email_1 = EmailableContact('Kevin Pineda','garfolks@gmail.com')
print(Contacts.all_contacts)
email_1.send_email("hello, test e-mail here")
