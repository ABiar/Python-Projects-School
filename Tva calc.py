#demande de prix par l'utilisateur
HT = input("Prix Hors taxe :\n ")
HT = float(HT)
#calculer le prix avec taxe
tva = HT * 0.80
ttc = HT + tva
print("tva = "+ str(tva))
print("Prix ttc = "+str(ttc))
input("pause...")
