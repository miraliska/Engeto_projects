# ceník
mercedes = 150_000
rolls_royce = '400000'
vybava = 50_000

rolls_royce=int(rolls_royce)
dva_mercedesy = 2 * mercedes
merc_a_rolls = mercedes + rolls_royce
dva_rollsy_s_vybavou = 2 * (rolls_royce + vybava)
mercik_s_vybavou = mercedes + vybava
sleva_merc = input("Jaká bude sleva na Mercedes? ", )
merc_se_slevou = mercedes - int(sleva_merc)
print("Sleva na mercedes je: ", sleva_merc)
print("Cena za dva Mercedesy je: ", dva_mercedesy)
print("Cena za Mercedes a Rolls-Royce: ", merc_a_rolls)
print("Cena za dva Rolls-Royce s příplatkovou výbavou: ", dva_rollsy_s_vybavou)
print("Cena za Mercedes s příplatkovou výbavou: ", mercik_s_vybavou)
print("Cena za Mercedes po slevě: ", merc_se_slevou)