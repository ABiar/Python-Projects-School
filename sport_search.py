

def menu() :
	while True :
		print("Que voulez-vous faire ? \n")
		print("0 - Quitter")
		print("1 - Rechercher")
		print("2 - Ajouter un sport")
		choix = int(input())
		if(choix == 1):
			print("Recherche")
		if(choix == 2):
			print("Ajouter")
		if(choix == 0):
			break

def addToFile(sport,equipe,ville):
	file = open("open_CSV.csv","a")
	file.write("{};{};{} \n" .format(sport, equipe, ville))
	file.close()


def getSport():
	while True :
		addNew = input("Voulez vous ajouter un nouveau sport ?\n")
		if(addNew.lower() == "non"):
			break
		elif(addNew.lower() == "oui") :
			sport = ("\n Sport : ")
			equipe = ("\n Equipe : ")
			ville = ("\n Ville/Pays")