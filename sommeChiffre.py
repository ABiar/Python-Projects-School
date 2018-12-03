maxdem = int(input("Entrez le nombre de chiffres que vous voulez additionner\n"))


def sommeChiffre(max) :
	somme1 =  0
	for i in range(0,max ):
		somme1 = somme1 + i
	print(somme1)

def sommePair(max):
	somme2 = 0
	for i in range(0,max):
		if(i%2 == 0):
			somme2 = somme2 + i
	print(somme2)

def sommeImpair(max):
	somme3 = 0
	for i in range(0,max):
		if(i%2 == 1):
			somme3 = somme3 + i
	print(somme3)

sommeChiffre(maxdem)
sommePair(maxdem)
sommeImpair(maxdem)