# Vstup uživatele
slovo = input("Zadej slovo:",)
otoceny = slovo[::-1]
if otoceny == slovo:
    print("Slovo '", slovo, "' je palindrom")
else:
    print("Slovo '", slovo, "' není palindrom")
