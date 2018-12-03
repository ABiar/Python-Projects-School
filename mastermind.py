from random import *
import time

#On commence par créer une liste de chiffre de 0 à 9

liste1 = ['0','1','2', '3', '4','5','6','7','8','9']
lCombi = 4
liste2 = liste1

#A l'aide de la liste créée juste avant on génére un liste aléatoire de ces caractères

def geneCombiSecrete():	
	combinS = ""
	for i in range(0, lCombi) :
		indexListe = randint(0, len(liste1) - 1)
		combinS = combinS + liste2[indexListe]
	return combinS

#Ensuite on demande au joueur de rentrer sa combinaison tout en vérifiant qu'elle contient bien 4 chiffres
	
def demande():
	combiJ = input("Entrez votre combinaison\n")
	if(len(combiJ) != lCombi) :
		print("La combinaison doit contenir 4 chiffres\n")
		return -1
	else : 
		return combiJ

#On comapare la combinaison et on indique ce qui est juste et ce qui est faux

def comparaison(combiJ,combinS):
	for i in range(0, len(combiJ)) :
		if(combiJ[i] == combinS[i]):
			print("le chiffre " + combiJ[i] +  " est bien placé ")
		else :
			print("Le chiffre " + combiJ[i] + " est incorrect")
		

starttime = time.time()
count = 0			
combi = geneCombiSecrete()	
while(count != 8) :
	combiJoueur = demande()
	comparaison(combiJoueur , combi)
	count = count +1
	if(count == 8 ) :
		print("Vous avez atteint la limite d'éssais")
		break
	if(combiJoueur == combi ) : 
		print("Bravo tu as gagné la combinaison était bien : " + combi)
		print("Vous avez mis : %s secondes"  %(time.time()- starttime))		
		print("Vous avez effectué : " + str(count) + " éssais" )
		break
	else :
		print("Réessayes")
		

	