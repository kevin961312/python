#extension de la clase lista
class ContactList(list):
    def search(self, name):
        '''Return all contacts that contain the search value in their name.'''
        matching_contacts = []
        for contact in elfs:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContactList()
    def __init__(self, name, email):
        self.name = name
        self.email = email
        #self.all_contacts.append(self)
        Contact.all_contacts.append(self)

#uso de la extension
c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@example.net")
c3 = Contact("Jenna C", "jennac@example.net")
list_1 = [c.name for c in Contact.all_contacts.search('John')]
print(list_1)

#Extension de la clase diccionario 
class LongNameDict(dict):
    def longest_key(key):
        longest = None
        for key in self:
            if not longest or len(key)> len(longest):
                longest = key
        return longest

longkeys = LongNameDict()
