import random
import unidecode

usedIds = []
usedNameSurnameCombos = []


class Client:

    def __init__(self, client_id, first_name, last_name, address_id):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.address_id = address_id

    def generate_client_query(self, file, is_last):
        file.write(f"({self.client_id}, \"{self.first_name}\", \"{self.last_name}\", \"{self.address_id}\"){is_last} \n")

