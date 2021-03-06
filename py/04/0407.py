import cv2

src = cv2.imread('./py/04/data/lenna.jpg', cv2.IMREAD_GRAYSCALE)
roi = cv2.selectROI(src)
print('roi =', roi)

img = src[roi[1]:roi[1] + roi[3],
          roi[0]:roi[0] + roi[2]]
    
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()