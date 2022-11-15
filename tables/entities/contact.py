class Contact:

    def __init__(self, contact_id, first_name, last_name, phone_number, address):
        self.contact_id = contact_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

    def generate_contact_query(self, file, is_last):
        file.write(f"({self.contact_id}, \"{self.first_name}\", \"{self.last_name}\", "
                f"\"{self.phone_number}\", \"{self.address}\"){is_last} \n")
