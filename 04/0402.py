import cv2

img = cv2.imread('C:/Users/jeong/Desktop/Folder/coding/cv/04/data/lena.jpg', cv2.IMREAD_GRAYSCALE)
print('img.shape = ', img.shape)

img = img.flatten()
print('img.shape = ', img.shape)

img = img.reshape(-1, 512, 512)
print('img.shape = ', img.shape)

cv2.imshow('img', img[0])
cv2.waitKey()
cv2.destroyAllWindows()