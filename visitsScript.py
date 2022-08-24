import random
import datetime

def visitScriptCreator(dbName, size, maxClientId, maxServiceId, maxDoctorId):

    print(f"INSERT INTO `{dbName}`.`visits` VALUES")

    for visitId in range(1, size+1):
        serviceId = random.randint(1, maxServiceId)
        clientId = random.randint(1, maxClientId)
        doctorId = random.randint(1, maxDoctorId)

        data = datetime.date(2022, random.randint(4, 8), random.randint(1, 30))
        time = datetime.time(random.randint(6, 18), 0)

        print(f"({visitId}, {serviceId}, {clientId}, {doctorId}, \"{data}\", \"{time}\"),")
