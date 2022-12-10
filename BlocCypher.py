import numpy as np
import cv2


def ECB(image):
    res = []
    for i in image:
        res.append(Permute(i))
    return np.array(res)


def CBC(image, IV):
    res = []
    t = 0
    b = []
    for i in image:
        if t == 0:
            b = XOR(list(i), IV)
            res.append(b)
        else:
            b = XOR(list(i), b)
            res.append(b)
        t += 1

    return np.array(res)


def Permute(Bloc):
    res = []
    for i in range(0, len(Bloc)):
        if i == 0:
            res.append(Bloc[len(Bloc) - 1])
        else:
            res.append(Bloc[i - 1])

    return res


def XOR(bloc1, bloc2):
    res = []
    for i in range(0, len(bloc1)):
        if bloc1[i] == bloc2[i]:
            res.append(0)
        elif bloc1[i] != bloc2[i]:
            res.append(255)

    return res


if __name__ == "__main__":
    image = cv2.imread("A.jpg", 0)
    ret, img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    imgcy = ECB(img)
    cv2.imshow(
        "image chifree avec ECB (pas de grande changementm: decalaga de tt la ligne par un seule pixel ) : ",
        imgcy,
    )
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    IV = [0 for i in range(0, 360)]  # message initiale (un vecteur des 0 )
    imgcy1 = CBC(img, IV)
    cv2.imshow("image chifree avec CBC : ", np.uint8(imgcy1))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
