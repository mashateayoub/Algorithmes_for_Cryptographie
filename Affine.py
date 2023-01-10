import string


def affine(ch, k1, k2):
    alphabet = list(string.ascii_lowercase)

    msgE = ch
    msgR = ""
    for i in range(0, len(msgE)):
        pos = alphabet.index(msgE[i])
        msgR = msgR + alphabet[(pos * k1 + k2) % len(alphabet)]

    return msgR


def dechiffrerAfine(ch, k1, k2):
    alphabet = list(string.ascii_lowercase)

    msgR = ch
    msgE = ""
    r, u, v = IEE(26, k1)
    for i in range(0, len(msgR)):
        c = alphabet.index(msgR[i])
        msgE = msgE + alphabet[(v % 26) * (c - k2) % 26]

    return msgE


def IEE(a, b):
    r = a
    r1 = b
    u = 1
    v = 0
    u1 = 0
    v1 = 1
    q = 0
    rs = 0
    vs = 0
    us = 0
    while r1 != 0:
        q = int(r / r1)
        rs = r
        vs = v
        us = u
        r = r1
        u = u1
        v = v1
        r1 = rs - q * r1
        u1 = us - q * u1
        v1 = vs - q * v1

    return (r, u, v)


if __name__ == "__main__":
    print(IEE(500, 25))
