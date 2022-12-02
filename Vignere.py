import string


def chiffrerVig(ch, c):
    alphabet = list(string.ascii_lowercase)

    msgE = ch
    msgR = ""
    j = 0
    for i in range(0, len(msgE)):
        pos = alphabet.index(msgE[i])
        temp = alphabet.index(c[j % len(c)])
        print(msgE[i], c[j % len(c)])
        msgR = msgR + alphabet[(pos + temp) % len(alphabet)]
        j = j + 1

    return msgR
