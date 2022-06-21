# Vytvoř proměnnou "týden", která obsahuje jednotlivé dny v týdnu malými písmeny
tyden = ["pondělí", "úterý", "středa",
         "čtvrtek", "pátek", "sobota", "neděle"]

# Uživatel vybere číslo
cislo = input("Vyber den v týdnu podle jeho čísla (1 - pondělí): ", )

# Ověř, jestli jde o číselný znak a jde o hodnotu <1, 7>
if cislo.isdigit() and int(cislo) > 0 and int(cislo) < 8:

    # ... pokud ano, získej první písmeno vybraného dne a ulož jej do proměnné
    den = tyden[int(cislo) - 1]
    prvni_pismeno_dne = den[0]

    # ... získej tip uživatele na první písmeno vybraného dne
    tip = input("Jakým písmenem začíná tento den? ", )

    # Ověř, že písmeno dne v proměnné "tyden" a "prvni_pismeno_dne"
    if prvni_pismeno_dne == tip:

        # ... pokud jsou shodné
        print("Správné písmeno!")

        # ... pokud jsou různé
    else:
        print("Špatné písmeno!")

    # ... pokud ne, upozorni na chybný vstup
else:
    print("Špatná vstupní hodnota!")