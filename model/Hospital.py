from model.Person import Person
from model.Doctor import Doctor


class Hospital:
    def __init__(self):
        self.people = list()
        self.doctors = list()
        self.assignments = dict()

    def get_people(self):
        return self.people

    def get_doctors(self):
        return self.doctors

    def get_assignments(self):
        return self.assignments

    def add_person(self, name: str, surname: str, personID: str):
        new_person = Person(name, surname, personID)
        for person in self.people:
            if person.personID == new_person.personID:
                raise Exception()
        self.people.append(new_person)

    def add_doctor(self, name: str, surname: str, personID: str, doctorID: str):
        new_doctor = Doctor(name, surname, personID, doctorID)
        for doctor in self.doctors:
            if doctor.doctorID == new_doctor.doctorID:
                raise Exception()
        self.doctors.append(new_doctor)

    def get_person(self, personID: str):
        for person in self.people:
            if person.personID == personID:
                return person

    def get_doctor(self, doctorID: str):
        for doctor in self.doctors:
            if doctor.doctorID == doctorID:
                return doctor

    def assign_doctor(self, doctorID: str, personID: str):
        doctor = self.get_doctor(doctorID)
        person = self.get_person(personID)
        if doctor in self.assignments:
            if person in self.assignments[doctor]:
                raise Exception()
            self.assignments[doctor].append(person)
        else:
            self.assignments.update({doctor: [person]})
