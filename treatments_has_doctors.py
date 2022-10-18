import random

def joinScriptCreator(treatmentsCount: int, doctorsCount: int, comboCount: int):
    usedCombos = []
    print("INSERT INTO `medcenter_database`.`treatments_has_doctors` VALUES")
    for i in range(0, comboCount):
        combo = [random.randint(1, treatmentsCount), random.randint(1, doctorsCount)]
        while combo in usedCombos:
            combo = [random.randint(1, treatmentsCount), random.randint(1, doctorsCount)]
        print(f"({combo[0]}, {combo[1]}),")
        usedCombos.append(combo)

