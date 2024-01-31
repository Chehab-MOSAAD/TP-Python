#Writer: Chehab MOSAAD - 1A Informatique - Programmation en python – Série 4

print(
    "Bonjour, \n C'est le TD Programmation en python – Série 4 (Fait par: Chehab MOSAAD)"
)

while True:
  print("\nMenu des exercices :")
  print("1. Exercice 1 - Le chiffrement affine")
  print("2. Exercice 2 - Le chiffre de Vigenère")
  print("3. Quitter\n")

  choix = input("Choisissez un exercice (1, 2 ou 3 pour quitter) : ")

  if choix == '1':

    def cle_valide(a, b):
      r = a % 26
      while r != 0:
        a = 26
        b = r
        r = a % b
      return b == 1

    def chiffrer1(texte, a, b):
      if not cle_valide(a, b):
        return "Clé invalide"
      texte = texte.upper()
      texte_chiffre = ""
      for c in texte:
        if c.isalpha():
          x = ord(c) - ord('A')
          y = (a * x + b) % 26
          c_chiffre = chr(y + ord('A'))
          texte_chiffre += c_chiffre
        else:
          texte_chiffre += c
      return texte_chiffre

    def cle_dechiffrement(a, b):
      if not cle_valide(a, b):
        return "Clé invalide"
      r = a % 26
      u = 1
      v = 0
      while r != 0:
        q = a // b
        a = b
        b = r
        r = a % b
        u, v = v, u - q * v
      a_prime = u % 26
      b_prime = (-a_prime * b) % 26
      return a_prime, b_prime

    def dechiffrer1(texte, a, b):
      if not cle_valide(a, b):
        return "Clé invalide"
      a_prime, b_prime = cle_dechiffrement(a, b)
      texte_dechiffre = chiffrer1(texte, a_prime, b_prime)
      return texte_dechiffre

    texte = input("Entrez le texte en clair à chiffrer : ")
    a = int(input("Entrez la cle de chiffrement (a) : "))
    b = int(input("Entrez la cle de chiffrement (b) : "))

    cryptogramme = chiffrer1(texte, a, b)
    print("Le Cryptogramme :", cryptogramme)

    if not cle_valide(a, b):
      print("Clé invalide")
    else:
      x, y = cle_dechiffrement(a, b)
      print("La cle de déchiffrement est :", x, y)

      texte_dechiffre = dechiffrer1(cryptogramme, a, b)
      print("Le texte déchiffré :", texte_dechiffre)

  elif choix == '2':
    # Fonction qui génére la clé à partir du mot clé en clair
    def generer_cle(texte, mot_cle):
      cle = ""
      i = 0
      for lettre in texte:
        if lettre.isalpha():
          cle += mot_cle[i]
          i = (i + 1) % len(mot_cle)
        else:
          cle += lettre
      return cle

    # Fonction qui chiffre un texte en clair avec une clé
    def chiffrer(texte, cle):
      cryptogramme = ""
      for i in range(len(texte)):
        lettre_texte = texte[i]
        lettre_cle = cle[i]
        if lettre_texte.isalpha():
          decalage = (ord(lettre_texte.upper()) - ord('A') +
                      ord(lettre_cle.upper()) - ord('A')) % 26
          if lettre_texte.isupper():
            cryptogramme += chr(ord('A') + decalage)
          else:
            cryptogramme += chr(ord('a') + decalage)
        else:
          cryptogramme += lettre_texte
      return cryptogramme

    # Fonction qui déchiffre un cryptogramme avec une clé
    def dechiffrer(cryptogramme, cle):
      texte = ""
      for i in range(len(cryptogramme)):
        lettre_cryptogramme = cryptogramme[i]
        lettre_cle = cle[i]
        if lettre_cryptogramme.isalpha():
          decalage = (ord(lettre_cryptogramme.upper()) - ord('A') -
                      (ord(lettre_cle.upper()) - ord('A')) + 26) % 26
          if lettre_cryptogramme.isupper():
            texte += chr(ord('A') + decalage)
          else:
            texte += chr(ord('a') + decalage)
        else:
          texte += lettre_cryptogramme
      return texte

    texte = input("Entrez le texte en clair à chiffrer : ")
    mot_cle = input("Entrez le mot clé pour générer la clé de chiffrement : ")

    cle = generer_cle(texte, mot_cle)
    print("La clé de chiffrement :", cle)

    cryptogramme = chiffrer(texte, cle)
    print("Le Cryptogramme :", cryptogramme)

    texte_dechiffre = dechiffrer(cryptogramme, cle)
    print("Le texte déchiffré :", texte_dechiffre)

  elif choix == '3':
    print("Au revoir !")
    break

  else:
    print(
        "Choix invalide. Veuillez choisir un exercice valide (1, 2 ou 3 pour quitter)."
    )
