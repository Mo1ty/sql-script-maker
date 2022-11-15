class Speciality:

    def __init__(self, speciality_id, name, description):
        self.speciality_id = speciality_id
        self.name = name
        self.description = description

    def generate_spec_query(self, file, is_last):
        file.write(f"({self.speciality_id}, \"{self.name}\", \"{self.description}\"){is_last} \n")
