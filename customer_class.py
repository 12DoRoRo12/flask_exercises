class Customer:
    def __init__(self, first, last, gender, mail, phone):
        self.first = first
        self.last = last
        self.gender = gender
        self.mail = mail
        self.phone = phone

    @property
    def fullname(self):
        return  '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.fullname, self.gender, self.mail, self.phone)

