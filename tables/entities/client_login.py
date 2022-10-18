class ClientLogin:

    def __init__(self, client_id, email, password, phone_number):
        self.client_id = client_id
        self.email = email
        self.password = password
        self.phone_number = phone_number

    def generate_client_login_query(self, file, is_last):
        file.write(f"({self.client_id}, \"{self.email}\", \"{self.password}\", \"{self.phone_number}\"){is_last} \n")
