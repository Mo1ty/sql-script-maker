import random


def serviceScriptCreator(dbName, size, maxServiceTypeId, someWords):

    usedServiceNames = []

    print(f"INSERT INTO `{dbName}`.`services` VALUES")

    for serviceId in range(1, size+1):

        serviceName = someWords[random.randint(0, len(someWords) - 1)]
        while serviceName in usedServiceNames:
            serviceName = someWords[random.randint(0, len(someWords) - 1)]

        print(f"({serviceId}, {random.randint(1, maxServiceTypeId)}, \"{serviceName}\","
              f" {random.randint(200, 800) // 100}, {random.randint(1, 9)}),")
        usedServiceNames.append(serviceName)
