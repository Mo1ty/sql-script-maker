class Treatment:

    def __init__(self, treatment_id, name, price):
        self.treatment_id = treatment_id
        self.name = name
        self.price = price

    def write_first_line(self):
        f = open("script.sql", "a")
        f.write("INSERT INTO `medcenter_database`.`treatments` VALUES\n")
        f.close()

    def generate_treatment_query(self, file, is_last):
        file.write(f"({self.treatment_id}, \"{self.name}\", {self.price}){is_last} \n")

