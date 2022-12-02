import math


def encryptMessage(key, msg):
    ciphertext = [""] * key
    for column in range(key):
        currentIndex = column
        while currentIndex < len(msg):
            ciphertext[column] += msg[currentIndex]
            currentIndex += key
    return "".join(ciphertext)


def decryptMessage(key, msg):
    numOfColumns = int(math.ceil(len(msg) / float(key)))
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(msg)
    plaintext = [""] * numOfColumns
    column = 0
    row = 0

    for symbol in msg:
        plaintext[column] += symbol
        column += 1
        if (column == numOfColumns) or (
            column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes
        ):
            column = 0
            row += 1

    return "".join(plaintext)


if __name__ == "__main__":
    # Crypting Test
    print("Crypting Test : \n")
    myMessage = "Spruch 60. Von VESTA An STEIN. QUEEN MARY am Elften eins acht Uhr MEZ von Dampfer CAMPEIRO auf hoehe RECIFE gemeldet."
    myKey = 19
    ciphertext = encryptMessage(myKey, myMessage)
    print(ciphertext)
    print("\n")

    # DeCrypting Test
    print("DeCrypting Test : \n")
    myMessage = "SAAamhep RcpotrAYhfe.un tehc a rehSmU   T hCR6EErAE0Il MC.NfMPI .tEEFV eZIEoQn R nU vOg Eeo eVEinamENn ueS sDflTM a d"
    myKey = 19
    plaintext = decryptMessage(myKey, myMessage)
    print(plaintext)

