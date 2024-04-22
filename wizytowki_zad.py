from faker import Faker

fake = Faker()

class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
    
    def contact(self):
        print(f"Wybieram numer prywatny {self.phone} i dzwonię do {self.name} {self.surname}")
    
    @property
    def label_length(self):
        return len(self.name) + len(self.surname)

class BusinessContact(BaseContact):
    def __init__(self, name, surname, phone, email, job_position, company, business_phone):
        super().__init__(name, surname, phone, email)
        self.job_position = job_position
        self.company = company
        self.business_phone = business_phone
    
    def contact(self):
        print(f"Wybieram służbowy numer {self.business_phone} i dzwonię do {self.name} {self.surname}")
    
    @property
    def label_length(self):
        return len(self.name) + len(self.surname)

def create_contacts(contact_type, quantity):
    contacts = []
    for _ in range(quantity):
        name = fake.first_name()
        surname = fake.last_name()
        phone = fake.phone_number()
        email = fake.email()
        if contact_type == 'Base':
            contact = BaseContact(name, surname, phone, email)
        elif contact_type == 'Business':
            job_position = fake.job()
            company = fake.company()
            business_phone = fake.phone_number()
            contact = BusinessContact(name, surname, phone, email, job_position, company, business_phone)
        contacts.append(contact)
    return contacts

base_contacts = create_contacts('Base', 1)
business_contacts = create_contacts('Business', 1)

print("Wizytówki prywatne:")
for contact in base_contacts:
    print(f"Imię: {contact.name}")
    print(f"Nazwisko: {contact.surname}")
    print(f"Telefon prywatny: {contact.phone}")
    print(f"Email: {contact.email}")
    print(f"Długość etykiety: {contact.label_length}")
    contact.contact()

print("\n")

print("Wizytówki służbowe:")
for contact in business_contacts:
    print(f"Imię: {contact.name}")
    print(f"Nazwisko: {contact.surname}")
    print(f"Stanowisko: {contact.job_position}")
    print(f"Firma: {contact.company}")
    print(f"Telefon służbowy: {contact.business_phone}")
    print(f"Długość etykiety: {contact.label_length}")
    contact.contact()