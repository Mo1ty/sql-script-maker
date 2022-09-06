import random
import unidecode

usedNameSurnameCombos = []
emailsList = []

def doctorScriptCreator(size: int, names, surnames):

    print("INSERT INTO `medcenter_database`.`doctors` VALUES")

    for doctorId in range(1, size + 1):

        # setting name & surname
        sex = random.randint(0, 1)
        firstName = names[sex][random.randint(0, 13)]
        lastName = surnames[sex][random.randint(0, 13)]

        while firstName + lastName in usedNameSurnameCombos:
            firstName = names[sex][random.randint(0, 13)]
            lastName = surnames[sex][random.randint(0, 13)]

        usedNameSurnameCombos.append(firstName + lastName)

        email = unidecode.unidecode(f"{firstName}.{lastName}@email.cz")

        addressId = random.randint(1, 7)

        print(f"({doctorId}, \"{firstName}\", \"{lastName}\", \"{email}\", "
              f"{addressId}),")

        usedNameSurnameCombos.append(firstName + lastName)
        emailsList.append(email)
    return emailsList
