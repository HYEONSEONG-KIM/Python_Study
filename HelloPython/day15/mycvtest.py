import cv2

rgb_image = cv2.imread('5.png',0)
crop_image = cv2.resize(rgb_image, dsize=(28, 28), interpolation=cv2.INTER_AREA)

print(crop_image)

