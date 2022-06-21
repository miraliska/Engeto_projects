# Zadané seznamy "kandidati" a "zamestnanci"
kandidati = ['Bruno', 'Anežka']
zamestnanci = ['František', 'Bruno', 'Anna', 'Jakub', 'Klára']

# Odstranění stringu "Bruno" ze seznamu "kandidati"
kandidati.remove("Bruno")

# Výpis zbývajícího obsahu v seznamu "kandidati"
print(kandidati)

# Opakovat třikrát jméno "Anežka" uvnitř seznamu "kandidati"
kandidati.append("Anežka")
kandidati.append("Anežka")

# Výpis zopakovaného stringu v "kandidati"
print(kandidati)

# Spojení seznamů "kandidati" a "zamestnanci"
zamestnanci = zamestnanci + kandidati

# Výpis spojených seznamů
print(zamestnanci)
