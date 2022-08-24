import random

password = "{bcrypt}" + "$2a$10$0YnP.OvKmDCTi2TtsWAcNun9WEQDw7a9Ddt9L3KzLPEgd47oSsw4i"

def internalLoginScriptCreator(emails):

    usedMails = []

    print("INSERT INTO `medcenter_database`.`internal_logins` VALUES")

    for id in range(1, len(emails) + 1):

        mail = emails[random.randint(0, len(emails) -1 )]
        while(mail in usedMails):
            mail = emails[random.randint(0, len(emails) - 1)]

        print(f"({id}, \"{mail}\", \"{password}\", \"ROLE_DOCTOR\"),")
        usedMails.append(mail)