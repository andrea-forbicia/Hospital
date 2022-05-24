from model.Person import Person


class Doctor(Person):
    def __init__(self, name, surname, personID, doctorID):
        super().__init__(name, surname, personID)
        self.doctorID = doctorID
        self.patients = list()

    def get_doctorID(self):
        return self.doctorID

    def add_patient(self, person: object):
        self.patients.append(person)

    def get_patients(self):
        return self.patients
