import clientScript
import doctorScript

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

mailboxes = ["gmail.com", "protonmail.com", "seznam.cz", ]

names = [maleNames, femaleNames]
surnames = [maleSurnames, femaleSurnames]

usedIds = []
usedEmails = []

doctorScript.doctorScriptCreator(10, names, surnames)
print("\n")

clientScript.clientScriptCreator(10, names, surnames)
