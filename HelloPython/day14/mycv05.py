import cv2



# gray_scale 이미지 불러오기
gray_image = cv2.imread('img/kakao.png', 0) # 인수를 0으로 전달하면 gray 이미지가 로드된다.
# gray 이미지 보기
cv2.imshow('kakao', gray_image)
cv2.imwrite('kakao_gray.jpg', gray_image)
cv2.waitKey(0)
print(gray_image)

