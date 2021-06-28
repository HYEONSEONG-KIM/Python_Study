import cv2

# rgb 이미지 불러오기
rgb_image = cv2.imread('img/iu.jpg')
dst = cv2.resize(rgb_image, dsize=(100, 100), interpolation=cv2.INTER_AREA)
dst2 = cv2.resize(rgb_image, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)


# rgb 이미지 보기
#cv2.imshow('kakao', rgb_image)
cv2.imshow('kakao', dst)
cv2.waitKey(0) 
print(rgb_image)

