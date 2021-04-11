# -*- coding: utf-8 -*-
"""test_classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Klj-Q55amPlAWjEBHJEkeDUZYGhGOTSU
"""

from tensorflow.keras.models import load_model


import numpy as np

from google.colab import files
uploaded = files.upload()

from google.colab import files
uploaded = files.upload()

model=load_model('skin_cancer_conv2d.h5')

import tensorflow as tf

image = '.jpg'

import cv2

def prepare(image):
  IMG_SIZE=384
  img_array = cv2.imread('.jpg', cv2.IMREAD_COLOR)
  new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
  return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)


y=model.predict([prepare('.jpg')])

print(y)

score = y[0]

# Commented out IPython magic to ensure Python compatibility.
print(
    "This is %.2f percent chance malignant and %.2f benine."
#     %(100*(1-score),100*score)
)
