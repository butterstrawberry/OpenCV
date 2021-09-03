import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('./py/05/data/lenna.jpg', cv2.IMREAD_GRAYSCALE)
dst = cv2.equalizeHist(src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

plt.title('Grayscale histogram of lenna.jpg')

hist1 = cv2.calcHist(images=[src], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
plt.plot(hist1, color='b', label='hist1 in src')

hist2 = cv2.calcHist(images=[dst], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
plt.plot(hist2, color='r', alpha=0.7, label='hist2 in dst')
plt.legend(loc='best')
plt.show()