import hashlib


class User:
    def __init__(self, Id, Name, Surname, Email, Phone, Password):
        self.id = Id
        self.name = Name
        self.surname = Surname
        self.email = Email
        self.phone = Phone
        self.password = hashlib.md5(Password.encode()).hexdigest()

    def print(self):
        print(f" ID - {self.id}, Name and Surname - {self.name} {self.surname},\nemail - {self.email}, phone - {self.phone}.")

    def get_all(self):
        return self.id, self.name, self.surname, self.email, self.phone

    def set_email(self, Email):
        self.email = Email

    def set_phone(self, Phone):
        self.phone = Phone