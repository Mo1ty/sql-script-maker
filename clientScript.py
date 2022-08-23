import random
# import bcrypt

usedIds = []
usedEmails = []


def clientScriptCreator(size: int, names, surnames):

    print("INSERT INTO `medcenter_database`.`clients` VALUES")

    for i in range(0, size):

        # set doctor id that is not used yet
        clientId = random.randint(1, 99)
        while clientId in usedIds:
            clientId = random.randint(1, 99)

        # setting name & surname
        sex = random.randint(0, 1)
        firstName = names[sex][random.randint(0, 13)]
        lastName = surnames[sex][random.randint(0, 13)]

        email = f"{firstName}.{lastName}@email.cz"

        password = "batman"  # implement bcrypt and add {bcrypt} in the password for Java

        addressId = random.randint(1, 7)

        print(f"({clientId}, {firstName}, {lastName}, {email}, {password}, {addressId})")

        usedIds.append(clientId)
        usedEmails.append(email)
