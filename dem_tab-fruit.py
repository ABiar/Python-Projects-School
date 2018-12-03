tableau1 = []
tableau2 = []

def demande(tab):
	ask = 0
	while(ask != "Fini"):
		ask = input("Saisissez un fruit. \n Ecrivez 'Fini' lorsque vous ne voulez plus ajouter de fruit.\n  ")
		if(ask == "Fini"):
			break
		else :
			tab.append(ask)
	return tab

def check(tab1, tab2):
	for i in range(0,len(tab1)):
			a = len(tab1[i])
			if(a > 4) :
				tab2.append(tab1[i])
	return tab2
				

tabIni = demande(tableau1)
print(tabIni)
tabFin = check(tableau1, tableau2)
print(tabFin)