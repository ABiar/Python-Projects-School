liste = ["Chien", "Loup", "Poule", "Tigre", "Canaris"]
def search():
	guess = input("Quel animal cherchez-vous ? \n")
	if(guess == liste):
		print("{} est dans le tableau".format(guess))
	else:
		print("{} n'est pas dans le tableau".format(guess))
		add(guess)

def add(guess ):
	answer = input("Voulez-vous l'ajouter ? \n")
	if(answer == "oui" ):
		liste.append(guess)



search()
print(liste)

