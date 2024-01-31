#Writer: Chehab MOSAAD - 1A STRI
#TP1 Informatique - Programmation en python – Série 1

print("Bonjour, \n C'est le TD Programmation en python – Série 1 (Fait par: Chehab MOSAAD)")

while True:
  print("\nMenu des exercices :")
  print("1. Exercice 1 - Saisie d'un entier entre 0 et 20")
  print("2. Exercice 2 - Calcul de Mention")
  print("3. Exercice 3 - Statistiques de Classe")
  print("4. Exercice 4 - Moyenne de Classe")
  print("5. Exercice 5 - Somme des Pairs")
  print("6. Exercice 6 - Fonction f(x)")
  print("7. Exercice 7 - Tri par Insertion")
  print("8. Exercice 8 - Gestion des Employés")
  print("9. Quitter\n")

  choix = input("Choisissez un exercice (1, 2, ... ,8 ou 9 pour quitter) : ")

  if choix == '1':
    while True:
          valeur = int(input("Entrez un entier entre 0 et 20 : "))
          if 0 <= valeur <= 20:
              print("L'entrée est valide!")
              break
          else:
              print("La valeur doit être dans l'intervalle de 0 à 20.")

  elif choix == '2':
    # Demande à l'utilisateur de saisir une note entre 0 et 20
    while True:
      note = int(input("Entrez une note entre 0 et 20 : "))
      if 0 <= note <= 20:
        break
      else:
        print("La valeur doit être dans l'intervalle de 0 à 20.")
    
    # Vérifie la mention correspondante
    if 0 <= note < 10:
        mention = "Insuffisant"
    elif 10 <= note < 12:
        mention = "Passable"
    elif 12 <= note < 14:
        mention = "AB"
    elif 14 <= note < 16:
        mention = "B"
    else:
        mention = "TB"
    
    # Affiche la mention correspondante
    print("La mention est :", mention)

  elif choix == '3':
    # Initialisation des variables
    total_notes = 0 
    min_note = 20
    max_note = 0
    reussis = 0
    
    # Saisie des notes pour 10 étudiants
    for i in range(1, 11):
        note = int(input(f"Entrez la note de l'étudiant {i} : "))
        
        # Vérifie si la note est valide
        if 0 <= note <= 20:
            total_notes += note  # Ajoute la note à la somme totale
            
            if note < min_note:
                min_note = note  # Met à jour la note minimale
            
            if note > max_note:
                max_note = note  # Met à jour la note maximale
            
            if note >= 10:
                reussis += 1  # Incrémente le compteur des réussites
        else:
            print("La note doit être comprise entre 0 et 20. Réessayez.")
            i -= 1
    
    # Calcul de la moyenne de la classe
    moyenne_classe = total_notes / 10
    
    # Affichage des résultats
    print("Moyenne de la classe : ", moyenne_classe)
    print("Note minimale : ", min_note)
    print("Note maximale : ", max_note)
    print("Nombre d'étudiants ayant réussi : ", reussis)

  elif choix == '4':
    # Initialisation des variables
    total_notes = 0
    notes = []
    indices_reussis = []
    
    # Saisie des notes pour 10 étudiants
    for i in range(1, 11):
        note = int(input(f"Entrez la note de l'étudiant {i} (entre 0 et 20) : "))
        
        # Vérifie si la note est valide (entre 0 et 20)
        if 0 <= note <= 20:
            total_notes += note  # Ajoute la note à la somme totale
            notes.append(note)  # Ajoute la note à la liste des notes
            
            if note >= total_notes / i:
                indices_reussis.append(i - 1)  # Ajoute l'indice de l'étudiant ayant réussi
        else:
            print("La note doit être comprise entre 0 et 20. Réessayez.")
            i -= 1
    
    # Calcul de la moyenne de la classe
    moyenne_classe = total_notes / 10
    
    # Affichage des résultats
    print("Moyenne de la classe : ", moyenne_classe)
    
    # Vérifie s'il y a des étudiants ayant une note supérieure ou égale à la moyenne
    if len(indices_reussis) > 0:
        print("Nombre d'étudiants ayant une note ≥ à la moyenne : ", len(indices_reussis))
        print("Indices correspondant à ces étudiants :", indices_reussis)
    else:
        print("Aucun étudiant n'a une note ≥ à la moyenne de la classe.")

  elif choix == '5':
    # Demande à l'utilisateur de saisir un nombre
    nb = int(input("Entrez un nombre : "))
    
    # Initialise la somme à zéro
    somme = 0
    
    # Calcule la somme
    for i in range(0, nb, 2):
        somme += i
    
    # Affiche la somme
    print("La somme est :", somme)

  elif choix == '6':
    #Exercice 6
    # Définition de la fonction f(x)
    def f(x):
        return 2 * x**3 + x - 5
    
    # Saisie des bornes et du pas
    BorneInf = int(input("Entrez la borne inférieure : "))
    BorneSup = int(input("Entrez la borne supérieure : "))
    Pas = int(input("Entrez la valeur du pas : "))
    
    # Calcul et affichage des valeurs de la fonction
    print("Valeurs de la fonction f(x) :")
    x = BorneInf
    while x <= BorneSup:
        valeur = f(x)
        print("f(", x, ") = ", valeur)
        x += Pas

  elif choix == '7':
    # Définition de la fonction de tri par insertion
    def tri_insertion(liste):
        for i in range(1, len(liste)):
            cle = liste[i]
            j = i - 1
            while j >= 0 and cle < liste[j]:
                liste[j + 1] = liste[j]
                j -= 1
            liste[j + 1] = cle
    
    # Saisie de la liste d'entiers à trier
    n = int(input("Entrez la taille de la liste : "))
    liste = []
    for i in range(n):
      element = int(input(f"Entrez l'élément {i+1} : "))
      liste.append(element)
      
    # Appel de la fonction de tri par insertion
    tri_insertion(liste)
    
    # Affichage de la liste triée
    print("Liste triée :", liste)

  elif choix == '8':
    # Définition de la fonction de saisie d'un employé
    def saisie_employe():
        nom = input("Entrez le nom de l'employé : ")
        prenom = input("Entrez le prénom de l'employé : ")
        salaire = float(input("Entrez le salaire annuel de l'employé en euros : "))
        anciennete = int(input("Entrez l'ancienneté de l'employé en années : "))
        return {"nom": nom, "prenom": prenom, "salaire": salaire, "anciennete": anciennete}
    
    # Définition de la fonction de mise à jour des salaires et primes
    def mise_a_jour_salaire(employes):
        for employe in employes:
            employe["salaire"] *= 1.02  # Augmente le salaire de 2%
            if employe["anciennete"] > 4:
                employe["salaire"] += 200  # Ajoute une prime de 200 euros
    
    # Saisie de la base d'employés
    base_employes = []
    n = int(input("Entrez le nombre d'employés dans la base : "))
    for i in range(n):
        employe = saisie_employe()
        base_employes.append(employe)
    
    # Mise à jour des salaires et primes
    mise_a_jour_salaire(base_employes)
    
    # Créez une fonction pour extraire la valeur 'anciennete' du dictionnaire employé
    def obtenir_anciennete(employe):
        return employe["anciennete"]
    
    # Triez la liste base_employes en fonction de anciennete
    base_employes.sort(key=obtenir_anciennete)
    
    # Affichez les noms des employés dans l'ordre croissant de leur ancienneté
    print("Noms des employés embauchés du plus ancien au plus récent :")
    for employe in base_employes:
        print(employe["prenom"], employe["nom"])

  elif choix == '9':
    print("Au revoir !")
    break
  
  else:
    print("Choix invalide. Veuillez choisir un exercice valide (1, 2, ... ,8 ou 9 pour quitter).")
