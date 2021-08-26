import cv2

img = cv2.imread('./py/04/data/lena.jpg')

img[100:400, 200:300, 0] = 255
img[100:400, 300:400, 1] = 255
img[100:400, 400:500, 2] = 255 

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()