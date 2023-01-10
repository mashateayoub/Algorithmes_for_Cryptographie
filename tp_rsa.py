def premier(n):
    # si n n'est pas divisible par tous les nombre entre lui et 2 ==> n est premier
    if n < 2:
        return " est non-premier"
    for i in range(2, n):
        if n % i == 0:
            return " est non-premier"
    return " est premier "


def est_premier(n):
    # si n n'est pas divisible par tous les nombre entre lui et 2 ==> n est premier
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def factoriser(n):
    # On commence par vérifier si le nombre est pair
    if n % 2 == 0:
        return (2, n // 2)

    # Si le nombre est impair, on cherche un nombre premier qui soit un diviseur de n
    for i in range(3, n, 2):
        if n % i == 0 and est_premier(i):
            return (i, n // i)

    # Si aucun nombre premier n'a été trouvé, c'est que n est premier
    return (n, 1)


def chiffrer(m, e, N):
    return pow(m, e) % N


def euclide_etendu(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


if __name__ == "__main__":

    # # exercice 2
    # for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    #     print(i, premier(i))

    # print(17, factoriser(17))

    # # exercice 3
    # # Pour encoder un message m avec la clé publique de Bob,
    # #  il faut utiliser l'algorithme RSA et appliquer la formule suivante : c = m^e mod N
    # # Où c est le message chiffré, m est le message à chiffrer, e est l'exposant de la clé publique de Bob et N est le modulo de la clé publique de Bob.

    # # Dans notre cas, m = 15, e = 3 et N = 187. Appliquons la formule :
    # # c = 15^3 mod 187
    # #   = 15 * 15 * 15 mod 187
    # #   = 3375 mod 187
    # #   = 9
    # # Le message chiffré est donc c = 9.

    # message = 15
    # exposant = 3
    # modulo = 187

    # message_chiffre = chiffrer(message, exposant, modulo)
    # print(message_chiffre)

    print(euclide_etendu(500, 25))
