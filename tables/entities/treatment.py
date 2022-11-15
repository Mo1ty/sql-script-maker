class Treatment:

    def __init__(self, treatment_id, speciality_id, name, regular_price, required_qualification):
        self.treatment_id = treatment_id
        self.speciality_id = speciality_id
        self.name = name
        self.regular_price = regular_price
        self.required_qualification = required_qualification

    def write_first_line(self):
        f = open("script.sql", "a")
        f.write("INSERT INTO `alternative-db`.`treatments` VALUES\n")
        f.close()

    def generate_treatment_query(self, file, is_last):
        file.write(f"({self.treatment_id}, \"{self.speciality_id}\", {self.name}, "
                   f"\"{self.regular_price}\", {self.required_qualification}){is_last} \n")

