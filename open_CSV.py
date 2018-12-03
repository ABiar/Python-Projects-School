def readFile():
	file = open("open_CSV.csv","r")
	for line in file:
		tab = line.split(";")
		print("{}, {}, {}, {}".format(tab[0],tab[1],tab[2],tab[3]))
	file.close()

def addToFile(nom,prenom,email,age):
	file = open("open_CSV.csv","a")
	file.write("{};{};{};{} \n" .format(nom , prenom, email,age))
	file.close()

def getUserInfo():
	while True :
		addNew = input("Voulez vous ajouter un nouvel utilisateur ?\n")
		if(addNew.lower() == "non"):
			break
		elif(addNew.lower() == "oui") :
			nom = input("\n Nom:")
			prenom = input("\n Prénom:")
			email = input("\n Email:")
			age = input("\n Age :")

			addToFile(nom,prenom,email,age)



readFile()

getUserInfo()

readFile()