import string
import numpy as np


def cypher(ch, key):
    """Fonction de chiffremenet de PlayFair"""
    alphabet = list(string.ascii_lowercase)
    msg = ch
    M = KeyMatrix(key)
    print("La Matrice : ", M)
    cy = ""
    i = 0
    while i < len(msg):
        c1 = msg[i]
        c2 = msg[i + 1] if (i + 1) < len(msg) else "x"
        i1, j1 = search(M, c1)
        i2, j2 = search(M, c2)
        if i1 == i2:
            cy = cy + M[i1][(j1 + 1) % 5]
            cy = cy + M[i1][(j2 + 1) % 5]
        elif j1 == j2:
            cy = cy + M[(i1 + 1) % 5][j1]
            cy = cy + M[(i2 + 1) % 5][j1]

        elif j1 != j2 and i1 != i2:
            cy = cy + M[i1][j2]
            cy = cy + M[i2][j1]

        i = i + 2

    return cy


def decypher(ch, key):
    """Fonction de dechiffremenet de PlayFair"""
    alphabet = list(string.ascii_lowercase)
    msg = ch
    M = KeyMatrix(key)
    cy = ""
    i = 0
    while i < len(msg):
        c1 = msg[i]
        c2 = msg[i + 1] if (i + 1) < len(msg) else "x"
        i1, j1 = search(M, c1)
        i2, j2 = search(M, c2)
        if i1 == i2:
            cy = cy + M[i1][(j1 - 1) % 5]
            cy = cy + M[i1][(j2 - 1) % 5]
        elif j1 == j2:
            cy = cy + M[(i1 - 1) % 5][j1]
            cy = cy + M[(i2 - 1) % 5][j1]

        elif j1 != j2 and i1 != i2:
            cy = cy + M[i1][j2]
            cy = cy + M[i2][j1]

        i = i + 2

    return cy


def KeyMatrix(key):
    """Fonction de construction de la matrice """
    ls = []
    alphabet = list(reversed(list(string.ascii_lowercase)))
    for i in key:
        if i not in ls:
            ls.append(i)

    while len(ls) <= 24:
        c = alphabet.pop()
        if c not in ls and c != "w":
            ls.append(c)

    M = [[] for _ in range(5)]
    r = 0
    t = 0
    for i in ls:
        M[r].append(i)
        t += 1
        if t == 5:
            r += 1
            t = 0

    return M


def search(M, char):
    """Fonction de recherche des indices dans la matrice"""
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == char:
                return i, j


if __name__ == "__main__":
    ch = input("Entrer une chaine (en miniscule sans espace) : ")
    key = input("Entrer une cle (en miniscule sans espace) : ")
    print("Le resultat de chiffrement de Playfair est : ", cypher(ch, key))
    print(
        "Le resultat de dechiffrement de Playfair est : ",
        decypher(cypher(ch, key), key),
    )
