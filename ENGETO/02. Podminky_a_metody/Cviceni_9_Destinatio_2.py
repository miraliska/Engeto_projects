# Vstupní proměnné
mesta = [
    "Praha", "Viden", "Olomouc",
    "Svitavy", "Zlin", "Ostrava"
]
domeny = ("gmail.com", "seznam.cz", "email.cz")
slevy = ("Olomouc", "Svitavy", "Ostrava")
ceny = (150, 200, 120, 120, 100, 180)
dvojita_cara = "=" * 35
cara = "-" * 35
nabidka = \
"""
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180"""

# Pozdrav a nabídka
print("Zdarec, tady je nabídka:")
print(nabidka)
print(cara)

# Vybrat destinaci, verifikace destinace
destinace = input("Vyber cíl (1-6):", )
if destinace.isnumeric() and int(destinace) in range(1, 7):
    prepocitana_destinace = mesta[int(destinace) - 1]
    print("Zvolená destinace:", prepocitana_destinace)
else:
    print("Neplatná vstupní data, ukončuji zadávání.")
    quit()

# Ověřit jestli uživatel dostane slevu
if mesta[int(destinace) - 1] in slevy:
    cena = ceny[int(destinace) - 1] * 0.75
    print("Zrovna ve slevě 25%")
else:
    cena = ceny[int(destinace) - 1]

# Ověřit validní jméno a přijmení
jmeno = input("Řekni jméno, nestyď se: ", )
prijmeni = input("Nebuď slušnej, ještě příjmení: ", )
if not jmeno.isalpha() and not prijmeni.isalpha():
    print("Neplatná vstupní data, ukončuji zadávání.")
    quit()

# Ověření validni emailové adresy
email = input("To jméno! Nebo raději e-mail: ")
if email.count("@") > 0:
    zadana_domena = email.split("@")
    if not zadana_domena[1] in domeny:
        print("Nepodporovaná doména, ukončuji zadávání.")
        quit()
else:
    print("Neplatná vstupní data, ukončuji zadávání.")
    quit()

# Rekapitulace objednávky
print(dvojita_cara)
print("Děkuji za objednávku", jmeno)
print("Tvá objednávka do", prepocitana_destinace, "za cenu", cena)
print("byla odeslána na e-mail", email)
