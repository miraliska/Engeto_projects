# Vstupní hodnoty uživatele
jmeno = input("Tvoje jméno:", )
vaha = float(input("Tvoje váha (kg):"))
vyska = float(input("Tvoje výška (m):"))
jmeno = "Ty hele,"
#vaha = 113
#vyska = 1.91

# Výpočet BMI
bmi = vaha / vyska ** 2

#když by se výška zadávala v cm, což je přirozeněnjší
#bmi = vaha / (vyska / 100) ** 2)

# Vytvoř proměnnou "kategorie", kam uložíš slovní ohodnocení BMI
if bmi < 18.5:
    kategorie = "což znamená, že brzo pojdeš, protože nežereš!"
elif bmi >= 18.5 and bmi <= 25:
    kategorie = "seš hubenej, běž se najest..."
elif bmi > 25 and bmi <= 30:
    kategorie = "takže jsi v pohodě, normální chlap"
elif bmi > 30 and bmi <= 40:
    kategorie = ", nežer tolik"
else:
    kategorie = ", seš tlustej jak prase, dělej se sebou něco!"

# Vytiskni odpoved s vysledkem - aby prošlo testem
#print(jmeno, "Tvoje BMI je", bmi, kategorie)

# lepší výstup
print(jmeno, "Tvoje BMI je", round(bmi, 1), kategorie)