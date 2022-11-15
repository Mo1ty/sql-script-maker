import random
import unidecode

usedIds = []
usedNameSurnameCombos = []


class Client:

    def __init__(self, client_id, contact_id, total_spendings, loyalty_level):
        self.client_id = client_id
        self.contact_id = contact_id
        self.total_spendings = total_spendings
        self.loyalty_level = loyalty_level

    def generate_client_query(self, file, is_last):
        file.write(f"({self.client_id}, \"{self.contact_id}\", "
                   f"\"{self.total_spendings}\", \"{self.loyalty_level}\"){is_last} \n")

