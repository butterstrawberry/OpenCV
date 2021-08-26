import cv2

imageFile = './py/02/data/lena.jpg'
img = cv2.imread(imageFile)
cv2.imwrite('./py/02/data/Lena.bmp', img)
cv2.imwrite('./py/02/data/Lena.png', img)
cv2.imwrite('./py/02/data/Lena2.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
cv2.imwrite('./py/02/data/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])