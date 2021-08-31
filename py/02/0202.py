import cv2

imageFile = './py/02/data/lenna.jpg'
img = cv2.imread(imageFile)
cv2.imwrite('./py/02/data/Lenna.bmp', img)
cv2.imwrite('./py/02/data/Lenna.png', img)
cv2.imwrite('./py/02/data/Lenna2.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
cv2.imwrite('./py/02/data/Lenna2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])