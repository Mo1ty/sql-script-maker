class InternalLogin:

    def __init__(self, int_id, email, password, role):
        self.int_id = int_id
        self.email = email
        self.password = password
        self.role = role

    def generate_internal_login(self, file, is_last):
        file.write(f"({self.int_id}, \"{self.email}\", \"{self.password}\", \"{self.role}\"){is_last} \n")
