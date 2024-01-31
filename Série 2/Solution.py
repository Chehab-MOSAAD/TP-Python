#Writer: Chehab MOSAAD - 1A Informatique - Programmation en python – Série 2

print("Bonjour, \n C'est le TD Programmation en python – Série 2 (Fait par: Chehab MOSAAD)")

while True:
  print("\nMenu des exercices :")
  print("1. Exercice 1 - Affichage des Caractères d’une Chaîne")
  print("2. Exercice 2 - Affichage des Éléments d’une Liste")
  print("3. Exercice 3 - Vérification un Nombre Palindrome")
  print("4. Exercice 4 - Compteur des Nombres Spéciaux")
  print("5. Exercice 5 - Validation des Séquences ADN")
  print("6. Quitter\n")

  choix = input("Choisissez un exercice (1, 2, ... ,5 ou 6 pour quitter) : ")

  if choix == '1':
    chaine = input("Entrez une chaîne : ")
    while not chaine.isalpha():
        print("Veuillez entrer une chaîne de caractères (pas de chiffres).")
        chaine = input("Entrez une chaîne : ")
    
    for caractere in chaine:
        print(caractere)

  elif choix == '2':
    liste = input("Entrez une liste d'éléments séparés par des espaces : ").split(',')
    for element in liste:
        print(element)

  elif choix == '3':
    nombre = input("Entrez un nombre : ")
    if nombre == nombre[::-1]:
        print("Oui, ce nombre est palindrome.")
    else:
        print("Non, ce nombre n'est pas palindrome.")

  elif choix == '4':
    compteur = 0
    numbers_found = []
    
    for v in range(1, 100000):
        chiffres = [int(x) for x in str(v)]
        somme = sum(chiffres)
        produit = 1
        for chiffre in chiffres:
            produit *= chiffre
        if somme == produit:
            compteur += 1
            numbers_found.append(v)
    
    print("Nombre d'entiers naturels respectant la propriété :", compteur)
    print("Les nombres trouvés sont :", numbers_found)
  
  elif choix == '5':
    def est_valide(chaine):
        # Vérifier si la chaîne est valide (composée uniquement de "a", "t", "g" ou "c").
        return all(caractere in "atgc" for caractere in chaine)
    
    def sequence_dans_chaine(chaine, sequence):
        # Vérifier si la séquence se trouve dans la chaîne.
        return sequence in chaine
    
    # Programme principal
    chaine_saisie = input("Entrez une chaîne : ")
    sequence_saisie = input("Entrez une séquence : ")
    
    if est_valide(chaine_saisie):
        print("La chaîne est valide.")
        if sequence_dans_chaine(chaine_saisie, sequence_saisie):
            print("La séquence se trouve dans la chaîne.")
        else:
            print("La séquence ne se trouve pas dans la chaîne.")
    else:
        print("La chaîne n'est pas valide.")

  elif choix == '6':
      print("Au revoir !")
      break
    
  else:
      print("Choix invalide. Veuillez choisir un exercice valide (1, 2, ... ,5 ou 6 pour quitter).")
  