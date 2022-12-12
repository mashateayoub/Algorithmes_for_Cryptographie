import DES

# Exemple de test : Le teste est fait a l'aide du exemple mentionee dans le pdf "The DES Algorithm Illustrated"
# PART 1 : Generating Keys
k = "0001001100110100010101110111100110011011101111001101111111110001"
k56 = DES.arrayToChar(DES.permuter(k, DES.PC1))
ci = k56[:28]
di = k56[28:]
keys = []
for i in range(0, 16):
    ck = DES.arrayToChar(DES.decaler(ci, DES.DKEY[i]))
    dk = DES.arrayToChar(DES.decaler(di, DES.DKEY[i]))
    ki = DES.arrayToChar(DES.permuter(ck + dk, DES.PC2))
    ci = ck
    di = dk
    print("C" + str(i + 1) + " : ", ci)
    print("D" + str(i + 1) + " : ", di)
    keys.append(ki)

# PART 2 : Cyphering message
message = "0000000100100011010001010110011110001001101010111100110111101111"
ip = DES.arrayToChar(
    DES.permuter(message, DES.IP)
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
    Rk = DES.arrayToChar(
        DES.XOR(
            Li,
            DES.arrayToChar(
                DES.permuter(
                    DES.arrayToChar(
                        DES.S_B(
                            DES.XOR(DES.arrayToChar(DES.permuter(Ri, DES.E)), keys[i])
                        )
                    ),
                    DES.P,
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

y = DES.arrayToChar(DES.permuter(R[15] + L[15], DES.IPI))
print("\n Le message chiffree apres les 16 iterations: ", y, len(y))
