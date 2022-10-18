class Address:

    def __init__(self, addr_id, city, postal_code, street, house_number):
        self.addr_id = addr_id
        self.city = city
        self.postal_code = postal_code
        self.street = street
        self.house_number = house_number

    def generate_address_query(self, file, is_last):
        file.write(f"({self.addr_id}, \"{self.city}\", \"{self.postal_code}\", "
                f"\"{self.street}\", {self.house_number}){is_last} \n")
