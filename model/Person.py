class Person:
    def __init__(self, name, surname, personID):
        self.name = name
        self.surname = surname
        self.personID = personID

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_ID(self):
        return self.personID

    def set_doctor(self, doctor: object):
        self.doctor = doctor

    def get_doctor(self):
        return self.doctor
