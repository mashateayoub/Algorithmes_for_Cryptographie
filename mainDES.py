import DES
import utilsDES
import string

# Chaine a chiffrer
ch = "welcometomorroco"
k = "clededes"
alphabet = list(string.ascii_lowercase)
binch = ""
for i in ch:
    binch += utilsDES.bin8(alphabet.index(i))

# Blocs binaires du 64 bits du chaine :
blocs = [binch[i : i + 64] for i in range(0, len(binch), 64)]
# cle en binaire :
bink = ""
for t in k:
    bink += utilsDES.bin8(alphabet.index(t))


# Chiffrement DES des blocs 64 bits
ci = []
for j in blocs:
    print("\n bloc ", str(blocs.index(j) + 1))
    ci.append(DES.CypherDES(j, bink))
print('\nChiffrement du message "' + ch + '" : ', utilsDES.arrayToChar(ci))

# Deschiffrement DES des blocs 64 bits
# di = []
# for l in ci:
#     print("\n bloc ", str(ci.index(l) + 1))
#     di.append(DES.decypherDES(l, bink))
# print('\nDechiffrement du message "' + ch + '" : ', utilsDES.arrayToChar(ci))
