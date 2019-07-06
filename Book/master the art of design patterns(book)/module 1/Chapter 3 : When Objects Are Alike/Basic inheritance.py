class ContactList(list):
    def search(self, name):
        """Return all contacts that contain the search value
                   in their name."""
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send"
              "'{}' order to '{}'".format(order, self.name))


class AddressHolder:
    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder):
    def __init__(self, name, email, phone, street, city, state, code):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone


class MailSender:
    def __init__(self, email):
        self.email = email

    def send_mail(self, massage):
        print("Sending mail to " + self.email)
        # Logic stuff


class EmailAbleContact(Contact, MailSender):
    pass




e = EmailAbleContact("john Smith", "jsmith@example.net")
e.send_mail("hi")

# c = Contact("Some Body", "somebody@example.net")
# s = Supplier("Sup Plier", "supplier@example.net")
# print(c.name, c.email, s.name, s.email)
#
# # print(c.order("I need pliers"))
#
# #  Error : AttributeError: 'Contact' object has no attribute 'order'
#
#
# print(s.order("I need pliers"))
