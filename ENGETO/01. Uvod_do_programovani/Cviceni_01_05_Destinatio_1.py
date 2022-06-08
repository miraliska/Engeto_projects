# vstupni hodnoty
MESTA = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
CENY = (150, 200, 120, 120, 100, 180)
ODDELOVAC = "=" * 35

# uvitani uzivatele
print("VITEJTE U NASI APLIKACE DESTINATIO!")
print(ODDELOVAC)
print("Nabidka:")
print("1 - Praha   | 150")
print("2 - Viden   | 200")
print("3 - Olomouc | 120")
print("4 - Svitavy | 120")
print("5 - Zlin    | 100")
print("6 - Ostrava | 180")
print(ODDELOVAC)

# vkladani udaju
destinace = input("Jakou volíte destinaci číslo?: ", )
mistenka = input("Přejete si zakoupit místenku? ano / ne: ", )
jmeno = input("Zadejte Vaše ctěné jméno a příjmení: ", )
print(ODDELOVAC)

# uprava zadanych hodnot
destinace = int(destinace)

# vypisovani vystupu
print("Rezervovali jste jízdenku do", MESTA[destinace - 1], "za cenu", CENY[destinace - 1], "Kč, místenka", mistenka, ", na jméno", jmeno)
