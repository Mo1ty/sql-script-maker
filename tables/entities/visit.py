import random
import datetime


class Visit:

    def __init__(self, visit_id, client_id, doctor_id, treatment_id, total_price, the_time):
        self.visit_id = visit_id
        self.client_id = client_id
        self.doctor_id = doctor_id
        self.treatment_id = treatment_id
        self.total_price = total_price
        self.time = the_time

    def generate_visit_query(self, file, is_last):
        file.write(f"({self.visit_id}, {self.client_id}, {self.doctor_id}, {self.treatment_id}, {self.total_price}, \"{self.time}\"){is_last} \n")

    def generate_unique_datetime(self, doctors_used_datetimes):
        while f"{self.time}" in doctors_used_datetimes:
            self.time = datetime.datetime(2022, random.randint(9, 12), random.randint(1, 30), random.randint(9, 17), 0)
