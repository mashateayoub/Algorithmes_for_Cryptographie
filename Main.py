import Cesar
import Affine
import Vignere


if __name__ == "__main__":
    print("Donner une Chaine de caracteres en miniscule sans espaces :")
    ch = input()
    ch1 = Cesar.cesar(ch)
    print("Le resultat de l'algorithme de cesar : ", ch1)

    ch2 = Affine.affine(ch, 19, 6)
    print("Le resultat de l'algorithme Affine : ", ch2)

    dech = Affine.dechiffrerAfine(ch2, 19, 6)
    print(
        "Le resultat de l'algorithme Affine (dechiffrement de " + str(ch2) + "): ", dech
    )

    ch3 = Vignere.chiffrerVig(ch, "id")
    print("Le resultat de l'algorithme vigenere : ", ch3)
