import datetime

from tables.entities.address import Address
from tables.entities.contact import Contact
from tables.entities.specialities import Speciality
from tables.entities.treatment import Treatment
from tables.entities.internal_login import InternalLogin
from tables.entities.client import Client
from tables.entities.client_login import ClientLogin
from tables.entities.doctor import Doctor
from tables.entities.visit import Visit

from tables.values.values_bank import *
from tables.values.string_generator import *

import random

# import unidecode
# ending = ";" if is_last else ","

addresses_list = []
treatments_list = []
speciality_list = []
internal_logins_list = []
clients_list = []
client_logins_list = []
contacts_list = []
doctors_list = []
specialities_list = []
treatments_has_doctors_list = [[0, 0]]
visits_list = []

used_datetimes: dict[int, list[str]] = {}

file = open("script.sql", "a", encoding='utf8')

# Adding addresses
file.write("INSERT INTO `alternative-db`.`addresses` VALUES\n")
for idNum in range(1, 11):
    address: Address = Address(
        idNum,
        cities[random.randint(0, len(cities)-1)],
        random.randint(10000, 99999),
        streets[random.randint(0, len(streets)-1)],
        random.randint(10, 199)
    )
    addresses_list.append(address)
    address.generate_address_query(file, ";" if idNum == 10 else ",")
file.write("\n")

# Adding specialities
file.write("INSERT INTO `alternative-db`.`specialities` VALUES\n")
for idNum in range(1, 4):
    speciality: Speciality = Speciality(
        idNum,
        treatments_types[idNum-1],
        "description"
    )
    specialities_list.append(speciality)
    speciality.generate_spec_query(file, ";" if idNum == 3 else ",")
file.write("\n")

# Adding treatments
file.write("INSERT INTO `alternative-db`.`treatments` VALUES\n")
for idNum in range(1, 6):
    treatment: Treatment = Treatment(
        idNum,
        specialities_list[random.randint(0, len(specialities_list)-1)],
        treatments[random.randint(0, len(treatments)-1)],
        random.randint(1, 9) * 100,
        random.randint(1, 9)
    )
    treatments_list.append(treatment)
    treatment.generate_treatment_query(file, ";" if idNum == 5 else ",")
file.write("\n")

# Adding clients logins (Clients required - but only ids 1-500 will be provided)
file.write("INSERT INTO `alternative-db`.`login-data` VALUES\n")
for idNum in range(1, 11):
    login_data: ClientLogin = ClientLogin(
        idNum,
        email_generator(10) + "@email.com",
        password,
        "ROLE_CLIENT" if idNum < 9 else "ROLE_DOCTOR"
    )
    client_logins_list.append(login_data)
    login_data.generate_client_login_query(file, ";" if idNum == 10 else ",")
file.write("\n")

# Adding specialities
file.write("INSERT INTO `alternative-db`.`contact` VALUES\n")
for idNum in range(1, 11):
    contact: Contact = Contact(
        idNum,
        names[idNum % 2][random.randint(0, 19)],
        surnames[idNum % 2][random.randint(0, 19)],
        treatments_types[random.randint(0, 2)],
        "description"
    )
    contacts_list.append(contact)
    contact.generate_contact_query(file, ";" if idNum == 10 else ",")
file.write("\n")

# Adding clients (Addresses required - but only ids 1-500 will be provided)
file.write("INSERT INTO `alternative-db`.`clients` VALUES\n")
for idNum in range(1, 9):
    client: Client = Client(
        idNum,
        names[idNum % 2][random.randint(0, 19)],
        surnames[idNum % 2][random.randint(0, 19)],
        email_generator(10) + "@email.com"
    )
    clients_list.append(client)
    client.generate_client_query(file, ";" if idNum == 8 else ",")
file.write("\n")

# Adding doctors (Addresses 501-600 required, internal logins required - 1-100 will be used)
file.write("INSERT INTO `alternative-db`.`doctors` VALUES\n")
for idNum in range(1, 3):
    doctor: Doctor = Doctor(
        idNum,
        idNum+8,
        "description_slot",
        random.randint(1, 2),
        idNum*3,
        random.randint(1, 2)
    )
    doctors_list.append(doctor)
    doctor.generate_doctor_query(file, ";" if idNum == 2 else ",")
    used_datetimes[doctor.doctor_id] = []
file.write("\n")

# --------------------------------------------------------------- #

file.write("INSERT INTO `alternative-db`.`visits` VALUES\n")
for idNum in range(1, 31):
    clientNum = random.randint(1, len(clients_list))
    doctorNum = random.randint(1, len(doctors_list))
    treat = random.randint(1, len(treatments_list))

    visit: Visit = Visit(
        idNum,
        clientNum,
        doctorNum,
        treat,
        treatments_list[treat-1].regular_price,
        datetime.datetime(2022, random.randint(9, 12), random.randint(1, 30), random.randint(9, 17), 0)
    )
    if visit.doctor_id not in used_datetimes:
        used_datetimes[visit.doctor_id] = []
    visit.generate_unique_datetime(used_datetimes[visit.doctor_id])
    used_datetimes[visit.doctor_id].append(f"{visit.time}")
    visit.generate_visit_query(file, ";" if idNum == 30 else ",")
file.write("\n")
file.close()
