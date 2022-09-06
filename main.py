import TreatmentDoctorJoin
import addressScript
import clientScript
import doctorScript
import internalLoginScript
import serviceScript
import visitsScript

# import unidecode

maleNames = ["Jiří", "Jan", "Petr", "Pavel", "Jaroslav", "Martin",
             "Tomáš", "Miroslav", "František", "Josef", "Václav",
             "Michal", "Karel", "David", "Jakub", "Ladislav",
             "Roman", "Ondřej", "Radek", "Marek"]

maleSurnames = ["Svoboda", "Novák", "Novotný", "Dvořák", "Černý", "Procházka",
                "Kučera", "Veselý", "Horák", "Němec", "Marek", "Pospíšil",
                "Pokorný", "Hájek", "Král", "Jelínek", "Růžička",
                "Beneš", "Fiala", "Sedláček"]

femaleNames = ["Marie", "Jana", "Eva", "Anna", "Hana", "Lenka", "Alena",
               "Jaroslava", "Lucie", "Ludmila", "Jitka", "Jarmila",
               "Veronika", "Martina"]

femaleSurnames = ["Nováková", "Svobodová", "Novotná", "Dvořáková", "Černá", "Procházková",
                  "Kučerová", "Veselá", "Horáková", "Němcová", "Marková", "Pokorná",
                  "Pospíšilová", "Hájková", "Králová", "Jelínková", "Růžičková",
                  "Benešová", "Fialová", "Sedláčková"]

mailboxes = ["gmail.com", "protonmail.com", "seznam.cz"]

someWords = "Lorem ipsum dolor sit amet consectetur adipiscing elit Etiam fringilla dolor sit amet tincidunt aliquet nunc nunc laoreet ipsum id commodo enim est ac antet"

someWords = someWords.split(" ")

names = [maleNames, femaleNames]
surnames = [maleSurnames, femaleSurnames]



addressScript.clients_addresses()
print("\n")

emailsList = doctorScript.doctorScriptCreator(10, names, surnames)
print("\n")

internalLoginScript.internalLoginScriptCreator(emailsList)
print("\n")

clientScript.clientScriptCreator(10, names, surnames)
print("\n")

visitsScript.visitScriptCreator("medcenter_database", 40, 10, 10, 10)
print("\n")

serviceScript.serviceScriptCreator("medcenter_database", 10, 7, someWords)
print("\n")

TreatmentDoctorJoin.joinScriptCreator(10, 10, 50)

