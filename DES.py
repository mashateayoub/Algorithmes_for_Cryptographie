import utilsDES


def CypherDES(message, k):
    # Exemple de test : Le teste est fait a l'aide du exemple mentionee dans le pdf "The DES Algorithm Illustrated"
    # PART 1 : Generating Keys
    # k = "0001001100110100010101110111100110011011101111001101111111110001"
    k56 = utilsDES.arrayToChar(utilsDES.permuter(k, utilsDES.PC1))
    ci = k56[:28]
    di = k56[28:]
    keys = []
    for i in range(0, 16):
        ck = utilsDES.arrayToChar(utilsDES.decaler(ci, utilsDES.DKEY[i]))
        dk = utilsDES.arrayToChar(utilsDES.decaler(di, utilsDES.DKEY[i]))
        ki = utilsDES.arrayToChar(utilsDES.permuter(ck + dk, utilsDES.PC2))
        ci = ck
        di = dk
        keys.append(ki)

    # PART 2 : Cyphering message
    # message = "0000000100100011010001010110011110001001101010111100110111101111"
    ip = utilsDES.arrayToChar(
        utilsDES.permuter(message, utilsDES.IP)
    )  # 1100110000000000110011001111111111110000101010101111000010101010 (coorecte)
    L0 = ip[:32]  # 1100 1100 0000 0000 1100 1100 1111 1111
    R0 = ip[32:]  # 1111 0000 1010 1010 1111 0000 1010 1010
    Li = L0
    Ri = R0
    R = []
    L = []
    for i in range(0, 16):
        print("\n Iteration n", i + 1, ":")
        print("\nK" + str(i + 1) + " : ", keys[i], len(keys[i]))
        Rk = utilsDES.arrayToChar(
            utilsDES.XOR(
                Li,
                utilsDES.arrayToChar(
                    utilsDES.permuter(
                        utilsDES.arrayToChar(
                            utilsDES.S_B(
                                utilsDES.XOR(
                                    utilsDES.arrayToChar(
                                        utilsDES.permuter(Ri, utilsDES.E)
                                    ),
                                    keys[i],
                                )
                            )
                        ),
                        utilsDES.P,
                    )
                ),
            )
        )
        Lk = Ri
        Ri = Rk
        Li = Lk
        print("Message : ", Li + Ri)
        R.append(Rk)
        L.append(Lk)

    y = utilsDES.arrayToChar(utilsDES.permuter(R[15] + L[15], utilsDES.IPI))
    print("\n Le message chiffree apres les 16 iterations: ", y, len(y))
    return y
    # le message a trouver: 1000010111101000000100110101010000001111000010101011010000000101


def decypherDES(message, k):
    return 0
