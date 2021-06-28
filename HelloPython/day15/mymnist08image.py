# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import keras
import cv2

# MNIST 데이터셋 불러오기
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 이미지 데이터 준비하기 (모델에 맞는 크기로 바꾸고 0과 1사이로 스케일링)
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

# 레이블을 범주형으로 인코딩
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

rgb_image = cv2.imread('5.png',0)
crop_image = cv2.resize(rgb_image, dsize=(28, 28), interpolation=cv2.INTER_AREA)

crop_image = crop_image.reshape((1, 28 * 28))
crop_image = crop_image.astype('float32') / 255

model = keras.models.load_model("mnist.h5")

predictions = model.predict(crop_image)

print(predictions[0].argmax())