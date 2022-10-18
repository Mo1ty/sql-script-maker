import datetime

from tables.entities.address import Address
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
internal_logins_list = []
clients_list = []
client_logins_list = []
doctors_list = []
treatments_has_doctors_list = [[0, 0]]
visits_list = []

used_datetimes: dict[int, list[str]] = {}

file = open("script.sql", "a", encoding='utf8')

# Adding addresses
file.write("INSERT INTO `medcenter_database`.`addresses` VALUES\n")
for idNum in range(1, 601):
    address: Address = Address(
        idNum,
        cities[random.randint(0, len(cities)-1)],
        random.randint(10000, 99999),
        streets[random.randint(0, len(streets)-1)],
        random.randint(10, 199)
    )
    addresses_list.append(address)
    address.generate_address_query(file, ";" if idNum == 600 else ",")
file.write("\n")

# Adding treatments
file.write("INSERT INTO `medcenter_database`.`treatments` VALUES\n")
for idNum in range(1, len(treatments) + 1):
    treatment: Treatment = Treatment(
        idNum,
        treatments[idNum - 1],
        random.randint(1, 9) * 100
    )
    treatments_list.append(treatment)
    treatment.generate_treatment_query(file, ";" if idNum == (len(treatments)) else ",")
file.write("\n")

# Adding internal logins
file.write("INSERT INTO `medcenter_database`.`internal_logins` VALUES\n")
for idNum in range(1, 111):
    internal_login: InternalLogin = InternalLogin(
        idNum,
        email_generator(10) + "@email.com",
        password,
        "ROLE_DOCTOR" if idNum <= 100 else "ROLE_ADMIN"
    )
    internal_logins_list.append(internal_login)
    internal_login.generate_internal_login(file, ";" if idNum == 110 else ",")
file.write("\n")

# Adding clients (Addresses required - but only ids 1-500 will be provided)
file.write("INSERT INTO `medcenter_database`.`clients` VALUES\n")
for idNum in range(1, 501):
    client: Client = Client(
        idNum,
        names[idNum % 2][random.randint(0, 19)],
        surnames[idNum % 2][random.randint(0, 19)],
        idNum
    )
    clients_list.append(client)
    client.generate_client_query(file, ";" if idNum == 500 else ",")
file.write("\n")

# Adding clients logins (Clients required - but only ids 1-500 will be provided)
file.write("INSERT INTO `medcenter_database`.`clients_logins` VALUES\n")
for idNum in range(1, 501):
    client_login: ClientLogin = ClientLogin(
        idNum,
        email_generator(10) + "@email.com",
        password,
        "+420" + number_generator(9)
    )
    client_logins_list.append(client_login)
    client_login.generate_client_login_query(file, ";" if idNum == 500 else ",")
file.write("\n")

# Adding doctors (Addresses 501-600 required, internal logins required - 1-100 will be used)
file.write("INSERT INTO `medcenter_database`.`doctors` VALUES\n")
for idNum in range(1, 101):
    doctor: Doctor = Doctor(
        idNum,
        internal_logins_list[idNum].email,
        names[idNum % 2][random.randint(0, 19)],
        surnames[idNum % 2][random.randint(0, 19)],
        idNum+500,
        "Description test value"
    )
    doctors_list.append(doctor)
    doctor.generate_doctor_query(file, ";" if idNum == 100 else ",")
    used_datetimes[doctor.doctor_id] = []
file.write("\n")

# Adding treatment & doctor connection
file.write("INSERT INTO `medcenter_database`.`treatments_has_doctors` VALUES\n")
for idNum in range(1, 251):

    is_last = ";" if idNum == 250 else ","
    treat, doc = 0, 0
    while [treat, doc] in treatments_has_doctors_list:
        treat = idNum if idNum < len(treatments_list) + 1 else random.randint(1, 20)
        doc = idNum if idNum < len(treatments_list) + 1 else random.randint(1, 20)
    treatments_has_doctors_list.append([treat, doc])

    file.write(f"({treat}, {doc})" + is_last + "\n")
file.write("\n")

file.write("INSERT INTO `medcenter_database`.`visits` VALUES\n")
for idNum in range(1, 5001):
    visit: Visit = Visit(
        idNum,
        random.randint(1, len(treatments_list)),
        random.randint(1, len(clients_list)),
        random.randint(1, len(doctors_list)),
        datetime.date(2022, random.randint(9, 12), random.randint(1, 30)),
        datetime.time(random.randint(9, 17), 0)
    )
    visit.generate_unique_datetime(used_datetimes[visit.doctor_id])
    used_datetimes[visit.doctor_id].append(f"{visit.date} {visit.time}")
    visit.generate_visit_query(file, ";" if idNum == 5000 else ",")
file.write("\n")
file.close()
