from model.Hospital import Hospital

hospital = Hospital()

hospital.add_person(name="name_1", surname="surname_1", personID="PID01")
hospital.add_person(name="name_2", surname="surname_2", personID="PID02")
try:
    hospital.add_person(name="name_3", surname="surname_3", personID="PID02")
except Exception:
    print("This personID already exists!")
hospital.add_person(name="name_4", surname="surname_4", personID="PID04")

hospital.add_doctor(name="doc_name_1", surname="doc_sur_1", personID="PID05", doctorID="DID01")
try:
    hospital.add_doctor(name="doc_name_2", surname="doc_sur_2", personID="PID06", doctorID="DID01")
except Exception:
    print("This doctorID already exists!")
hospital.add_doctor(name="doc_name_3", surname="doc_sur_3", personID="PID07", doctorID="DID03")

print(hospital.get_people())
print(hospital.get_doctors())

hospital.assign_doctor(doctorID="DID03", personID="PID02")
hospital.assign_doctor(doctorID="DID03", personID="PID01")
try:
    hospital.assign_doctor(doctorID="DID03", personID="PID01")
except Exception:
    print("This person has already been assigned to this doctor!")

print(hospital.get_assignments())
