import random
import bcrypt
import unidecode

usedIds = []
usedNameSunameCombos = []


def clientScriptCreator(size: int, names, surnames):

    print("INSERT INTO `medcenter_database`.`clients` VALUES")

    for clientId in range(1, size+1):


        # setting name & surname
        sex = random.randint(0, 1)
        firstName = names[sex][random.randint(0, 13)]
        lastName = surnames[sex][random.randint(0, 13)]

        while firstName + lastName in usedNameSunameCombos:
            firstName = names[sex][random.randint(0, 13)]
            lastName = surnames[sex][random.randint(0, 13)]

        usedNameSunameCombos.append(firstName+lastName)

        email = unidecode.unidecode(f"{firstName}.{lastName}@email.cz")

        password = "{bcrypt}" + "$2a$10$0YnP.OvKmDCTi2TtsWAcNun9WEQDw7a9Ddt9L3KzLPEgd47oSsw4i"

        addressId = random.randint(1, 7)

        print(f"({clientId}, \"{firstName}\", \"{lastName}\", \"{email}\", \"{password}\", {addressId}),")

        usedIds.append(clientId)
        usedNameSunameCombos.append(firstName+lastName)
