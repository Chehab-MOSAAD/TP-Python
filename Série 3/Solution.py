#Writer: Chehab MOSAAD - 1A Informatique - Programmation en python – Série 3

print("Bonjour, \n C'est le TD Programmation en python – Série 3 (Fait par: Chehab MOSAAD)")

while True:
  print("\nMenu des exercices :")
  print("1. Exercice 1 - Vérification d'une adresse IP")
  print("2. Exercice 2 - Conversion en binaire")
  print("3. Exercice 3 - Vérification de l'appartenance au réseau")
  print("4. Exercice 4 - Calcul du nombre d'adresses IP uniques")
  print("5. Exercice 5 - Calcul des plages d'adresses")
  print("6. Quitter\n")

  choix = input("Choisissez un exercice (1, 2, ... ,5 ou 6 pour quitter) : ")

  if choix == '1':
    while True:
      adresse = input("Entrez une adresse IP au format V.X.Y.Z : ")
      if '.'in adresse and all(i.isdigit() for i in adresse.split('.')):
          parties = adresse.split('.')
          if len(parties) != 4:
              print("Adresse IP invalide: elle doit avoir 4 parties.")
          else:
              is_valid = True
              for partie in parties:
                  if not 0 <= int(partie) <= 255:
                      is_valid = False
                      print("Adresse IP invalide: chaque partie doit être entre 0 et 255.")
                      break
              if is_valid:
                  print("Adresse IP valide:", adresse)
                  break
      else:
          print("Adresse IP invalide: elle doit contenir uniquement des chiffres.")
      
  elif choix == '2':
    adresse = input("Entrez une adresse IP au format V.X.Y.Z : ")
    parties = adresse.split('.')
    binaire = ''
    while True:
      if len(parties) != 4:
        print("Adresse IP invalide: elle doit avoir 4 parties.")
        break
      
      for partie in parties:
          if not 0 <= int(partie) <= 255:
            print("Adresse IP invalide: chaque partie doit être entre 0 et 255.")
            break
        
      for partie in parties:
          binaire += format(int(partie), '08b')
      print("Adresse IP en binaire:", binaire)
      break
  
  elif choix == '3':
    adresse_ip = input("Entrez une adresse IP au format V.X.Y.Z : ")
    masque = input("Entrez le masque de sous-réseau au format V.X.Y.Z : ")
    reseau = input("Entrez l'adresse d'un réseau au format V.X.Y.Z : ")

    ip_octets = list(map(int, adresse_ip.split('.')))
    masque_octets = list(map(int, masque.split('.')))
    reseau_octets = list(map(int, reseau.split('.')))
    
    for i in range(4):
        if (ip_octets[i] & masque_octets[i]) != reseau_octets[i]:
            print("L'adresse IP n'appartient pas au réseau.")
    
    print("L'adresse IP appartient au réseau.")

  elif choix == '4':
    def calcul_nb_adresses_ip():
      masque = input("Entrez le masque de sous-réseau au format V.X.Y.Z : ")
      nb_bits_un = masque.count('1')
      nb_adresses = 2^(32 - nb_bits_un)
      print("Nombre d'adresses IP uniques possibles:", nb_adresses)

    calcul_nb_adresses_ip()
  
  elif choix == '5':
    def calcul_plage_adresses():
      adresse_ip = input("Entrez une adresse IP au format V.X.Y.Z : ")
      masque = input("Entrez le masque de sous-réseau au format V.X.Y.Z : ")
  
      ip_octets = list(map(int, adresse_ip.split('.')))
      masque_octets = list(map(int, masque.split('.')))
      
      reseau = []
      for i in range(4):
          reseau.append(ip_octets[i] & masque_octets[i])
      
      diffusion = []
      for i in range(4):
          diffusion.append(reseau[i] | (255 - masque_octets[i]))
      
      print("Première adresse valable:", ".".join(map(str, reseau)))
      print("Dernière adresse valable:", ".".join(map(str, diffusion)))
      print("Adresse de diffusion:", ".".join(map(str, diffusion)))

    calcul_plage_adresses()
    
  elif choix == '6':
      print("Au revoir !")
      break
    
  else:
      print("Choix invalide. Veuillez choisir un exercice valide (1, 2, ... ,5 ou 6 pour quitter).")
    