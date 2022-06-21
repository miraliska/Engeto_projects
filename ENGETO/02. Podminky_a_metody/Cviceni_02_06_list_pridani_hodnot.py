# Vytvoření prázdného seznamu "kandidati"
kandidati = list()

# Výpis prázdného seznamu
print("Kandidáti na začátku:", kandidati)

# Vytvoření seznamu "zamestnanci"
zamestnanci = ["František", "Anna", "Jakub", "Klára"]

# Výpis seznamu "zamestnanci"
print("Zaměstnanci na začátku:",zamestnanci)

# Přidání nových jmen
kandidati.append("Bruno")
kandidati.append("Anežka")

# Výpis aktualizovaného obsahu "kandidati"
print("Nová jména přidána do kandidati:", kandidati)

# Vlož string na index
zamestnanci.insert(1, kandidati[0])

# Výpis seznamu "zamestnanci"
print("Nová jména přidána do zaměstnanci:", zamestnanci)