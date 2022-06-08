#########################################################
print("Cvičení: Spojování stringů")
# Ulož libovolné jméno a vypiš jej
jmeno = input("Zadej jméno:")
print("Ukládám \"" ,jmeno, "\" do jména...")

# Ulož libovolné příjmení a vypiš jej
prijmeni = input("Zadej příjmení:")
print("Ukládám \"" ,prijmeni, "\" do příjmení...")

# Vytvoř proměnnou "cele_jmeno" obsahující mezeru a vypiš její obsah
cele_jmeno = jmeno + " " + prijmeni
print("celé jméno:", cele_jmeno)

# Vytvoř a vypiš hodnotu délky uložené proměnné "cele_jmeno"
delka_jmena =len(cele_jmeno)
print("Délka jména:", delka_jmena)

# Vypiš celé jméno ohraničené oddělovači
print("="*delka_jmena)
print(cele_jmeno)
print("="*delka_jmena)

print("*"*100)