import hashlib


class User:
    def __init__(self, ID, Name, Surname, Email, Phone, Password, Role):
        self.id = ID
        self.name = Name
        self.surname = Surname
        self.email = Email
        self.phone = Phone
        self.password = Password
        # self.password = hashlib.md5(Password.encode()).hexdigest()
        self.role = Role

    @classmethod
    def create(cls, Name, Surname, Email, Phone, Password, ID=0, Role=1):
        return cls(ID, Name, Surname, Email, Phone, Password, Role)

    def print(self):
        print(
            f" ID - {self.id}, Name and Surname - {self.name} {self.surname},\nemail - {self.email}, phone - {self.phone}, роль - {self.role}.")

    def get_all(self):
        return self.id, self.name, self.surname, self.email, self.phone

    def set_email(self, Email):
        self.email = Email

    def set_phone(self, Phone):
        self.phone = Phone
