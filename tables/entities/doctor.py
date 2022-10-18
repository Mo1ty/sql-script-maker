import random
import unidecode

usedNameSurnameCombos = []
emailsList = []


class Doctor:

    def __init__(self, doctor_id, email, first_name, last_name, address_id, description):
        self.doctor_id = doctor_id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.address_id = address_id
        self.description = description

    def generate_doctor_query(self, file, is_last):
        file.write(f"({self.doctor_id}, \"{self.email}\", \"{self.first_name}\", "
                f"\"{self.last_name}\", \"{self.address_id}\", \"{self.description}\"){is_last} \n")
