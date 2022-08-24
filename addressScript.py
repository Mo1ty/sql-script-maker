import random

cities = ['Brno', 'Praha', 'Dresden', 'Pardubice', 'Ostrava', 'České Budějovice']
streets = ['Rooseveltova', "Nováková", "Drahunova", "Tinková", "Fialová",
           "Horáková", "Němcová", "Hlinky", "Červinková", "Dobrovolná",
           "Svobodná", "Novotná", "Mendlová", "Klusačková", "Jelínková"]

def clients_addresses():

    print("INSERT INTO `medcenter_database`.`addresses` VALUES")
    for id in range(1, 21):
        print(f"({id}, \"{cities[random.randint(0, len(cities)-1)]}\", \"{random.randint(10000, 90000)}\", "
              f"\"{streets[random.randint(0, len(streets)-1)]}\", {random.randint(1, 100)}),")
