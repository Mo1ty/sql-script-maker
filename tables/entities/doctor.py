import random
import unidecode

usedNameSurnameCombos = []
emailsList = []


class Doctor:

    def __init__(self, doctor_id, contact_id, description, speciality_id, qualification_level, shift_type_id):
        self.doctor_id = doctor_id
        self.contact_id = contact_id
        self.description = description
        self.speciality_id = speciality_id
        self.qualification_level = qualification_level
        self.shift_type_id = shift_type_id

    def generate_doctor_query(self, file, is_last):
        file.write(f"({self.doctor_id}, \"{self.contact_id}\", \"{self.description}\", "
                f"\"{self.speciality_id}\", \"{self.qualification_level}\", \"{self.shift_type_id}\"){is_last} \n")
