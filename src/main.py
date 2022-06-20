import cv2
import numpy as np
import matplotlib.pyplot as plt


def removeHighFreq(img, size):
    h, w = img.shape[0:2]
    h1, w1 = int(h/2), int(w/2)
    img[h1 - int(size/2):h1+int(size/2), w1 - int(size/2):w1 + int(size/2)] = 0
    return img


def removeLowFreq(img, size):
    h, w = img.shape[0:2]
    h1, w1 = int(h/2), int(w/2)
    img[:(h1 - int(size/2)), :] = 0
    img[(h1 + int(size/2)):, :] = 0
    img[:, :(w1 - int(size/2))] = 0
    img[:, (w1 + int(size/2)):] = 0
    return img


def highPassFiltering(img):

    img = cv2.imread(img)
    gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    img_fft = np.fft.fftshift(np.fft.fft2(thresh))

    dft_shift = removeHighFreq(img_fft, 350)

    idft_shift = np.fft.ifftshift(dft_shift)
    ifimg = np.fft.ifft2(idft_shift)
    ifimg = np.abs(ifimg)
    ifimg = np.float32(ifimg)

    plt.imshow(ifimg, 'gray')
    plt.show()


if __name__ == "__main__":

    highPassFiltering('../data/Lenna.png')