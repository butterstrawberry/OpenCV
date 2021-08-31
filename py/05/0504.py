import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('./py/05/data/lenna.jpg', cv2.IMREAD_GRAYSCALE)

hist1 = cv2.calcHist(images=[src], channels=[0], mask=None, histSize=[32], ranges=[0, 256])
hist2 = cv2.calcHist(images=[src], channels=[0], mask=None, histSize=[256], ranges=[0, 256])

hist1 = hist1.flatten()
hist2 = hist2.flatten()

plt.title('hist1: binX = np.arrange(32)')
plt.plot(hist1, color='r')
binX = np.arange(32)
plt.bar(binX, hist1, width=1, color='b')
plt.show()

plt.title('hist1: binX = np.arrange(32)*8')
binX = np.arange(32) * 8
plt.plot(binX, hist1, color='r')
plt.bar(binX, hist1, width=8, color='b')
plt.show()

plt.title('hist2: binX = np.arrange(256)')
plt.plot(hist2, color='r')
binX = np.arange(256)
plt.bar(binX, hist2, width=1, color='b')
plt.show()