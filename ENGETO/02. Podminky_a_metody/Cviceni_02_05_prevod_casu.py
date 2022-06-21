# Zadej časový údaj ve formátu "15:41" do proměnné "time"
time = input("Zadej čas ve formátu hh:mm : ", )

# Hodnotu v proměnné rozděl na list hodnot a ulož do proměnné "time_vals"
time_vals = list(time.split(':'))

# Vytvoř proměnné "hours" and "mins", kterým přiřadíš hodnoty z "time_vals"
hours = time_vals[0]
mins = time_vals[1]

# Pokud je hodnota v "hours" větší jak 12, převeď na příslušný string
if int(hours) == 00:
    adjusted_hours = 12
    daytime = "AM"
elif int(hours) == 12:
    adjusted_hours = 0
    daytime = "PM"
elif int(hours) > 12:
    adjusted_hours = int(hours) - 12
    daytime = "PM"

    # ... jinak ponech hodnotu původní
else:
    daytime = "AM"

# Označ denní dobu a ulož "AM"/"PM" do proměnné "daytime"

# Vypiš převedený čas s doplňující větou
if adjusted_hours == 0:
    print("Převedený čas je: ", hours, ":", mins, daytime)
else:
    print("Převedený čas je: ", adjusted_hours, ":", mins, daytime)