import cv2

rgb_image = cv2.imread('5.png')
dst = cv2.resize(rgb_image, dsize=(28, 28), interpolation=cv2.INTER_AREA)

cv2.imshow()