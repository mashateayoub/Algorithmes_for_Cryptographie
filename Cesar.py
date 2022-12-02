import string


def cesar(ch):
    alphabet = list(string.ascii_lowercase)

    msgE = ch
    msgR = ""

    k = int(input("donnnez le K :"))
    for i in range(0, len(msgE)):
        pos = alphabet.index(msgE[i])
        msgR = msgR + alphabet[(pos + k) % len(alphabet)]

    return msgR

