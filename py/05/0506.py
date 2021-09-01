import cv2
import matplotlib.pyplot as plt

bgr = cv2.imread('./py/05/data/lenna.jpg')

hist01 = cv2.calcHist([bgr], [0, 1], None, [32, 32], [0, 256, 0, 256])
plt.title('hist01')
plt.ylim(0, 31)
plt.imshow(hist01, interpolation="nearest")
plt.show()

hist02 = cv2.calcHist([bgr], [0, 2], None, [32, 32], [0, 256, 0, 256])
plt.title('hist02')
plt.ylim(0, 31)
plt.imshow(hist02, interpolation="nearest")
plt.show()

hist12 = cv2.calcHist([bgr], [1, 2], None, [32, 32], [0, 256, 0, 256])
plt.title('hist12')
plt.ylim(0, 31)
plt.imshow(hist12, interpolation="nearest")
plt.show()