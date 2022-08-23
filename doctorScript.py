import random

usedIds = []
usedEmails = []

def doctorScriptCreator(size: int, names, surnames):

    print("INSERT INTO `medcenter_database`.`doctors` VALUES")

    for i in range(0, size):

        # set doctor id that is not used yet
        doctorId = random.randint(1, 99)
        while(doctorId in usedIds):
            doctorId = random.randint(1, 99)

        # setting name & surname
        sex = random.randint(0, 1)
        firstName = names[sex][random.randint(0, 13)]
        lastName = surnames[sex][random.randint(0, 13)]

        email = f"{firstName}.{lastName}@email.cz"

        addressId = random.randint(1, 7)
        serviceTypeId = random.randint(1, 7)
        qualificationLevel = random.randint(4, 10)

        print(f"({doctorId}, {firstName}, {lastName}, {email}, {addressId}, {serviceTypeId}, {qualificationLevel})")

        usedIds.append(doctorId)
        usedEmails.append(email)