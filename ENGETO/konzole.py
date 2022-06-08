muj_slovnik = {}
inicialy = {"jmeno": "Matouš", "prijmeni": "Pakoš" }
kontakty = {"mobil": "+420582582582", "email": "matous@matous.cz" }
muj_slovnik["jmeno"] = inicialy
muj_slovnik["kontakt"] = kontakty
print(muj_slovnik)
print(muj_slovnik["kontakt"])
print(muj_slovnik["kontakt"]["mobil"])
print(muj_slovnik["kontakt"]["email"])
print(muj_slovnik.items())