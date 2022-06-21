# Uživatel zadá libovolné slovo a uloží jej do proměnné "slovo"
slovo = str(input("Zadej své slovo:", ))

# Zjistí délku slova a uloží ji do proměnné "delka_slova"
delka_slova = len(slovo)

# Pokud je hodnota v proměnné "delka_slova" větší než 5
if delka_slova >= 5:
    print("Délka slova", slovo, "je", delka_slova, "znaků.")

# ...pokud je hodnota v proměnné "delka_slova" větší než 1 a menší než 4
elif delka_slova > 1 and delka_slova <= 4:
    print("Slovo", slovo, "obsahuje", delka_slova, "znaků.")

# ...pokud je hodnota v proměnné "delka_slova" přesně 1 znak
elif delka_slova == 1:
    print(slovo, "obsahuje", delka_slova, "znak.")

# ...pokud je hodnota v proměnné "delka_slova" přesně 0 znaků
else:
    print("Nebylo zadáno žádné slovo")
