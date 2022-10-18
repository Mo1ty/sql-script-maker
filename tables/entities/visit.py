import random
import datetime


class Visit:

    def __init__(self, visit_id, treatment_id, client_id, doctor_id, the_date, the_time):
        self.visit_id = visit_id
        self.treatment_id = treatment_id
        self.client_id = client_id
        self.doctor_id = doctor_id
        self.date = the_date
        self.time = the_time

    def generate_visit_query(self, file, is_last):
        file.write(f"({self.visit_id}, \"{self.treatment_id}\", \"{self.client_id}\", "
                f"\"{self.doctor_id}\", \"{self.date} {self.time}\"){is_last} \n")

    def generate_unique_datetime(self, doctors_used_datetimes):
        while f"{self.date} {self.time}" in doctors_used_datetimes:
            self.date = datetime.date(2022, random.randint(9, 12), random.randint(1, 30))
            self.time = datetime.time(random.randint(9, 17), 0)
