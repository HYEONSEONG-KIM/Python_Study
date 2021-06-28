import cv2

# rgb 이미지 불러오기
rgb_image = cv2.imread('img/iu.jpg')


cropped_img = rgb_image[180:350,180:350]


# rgb 이미지 보기
cv2.imshow('kakao', cropped_img)
cv2.waitKey(0) 
print(rgb_image)

