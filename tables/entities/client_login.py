class ClientLogin:

    def __init__(self, contact_id, email, password, role):
        self.contact_id = contact_id
        self.email = email
        self.password = password
        self.role = role

    def generate_client_login_query(self, file, is_last):
        file.write(f"(\"{self.contact_id}\", \"{self.email}\", \"{self.password}\", \"{self.role}\"){is_last} \n")
