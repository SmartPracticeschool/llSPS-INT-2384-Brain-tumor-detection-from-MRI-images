# -*- coding: utf-8 -*-
"""CNN_trial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/SmartPracticeschool/llSPS-INT-2384-Brain-tumor-detection-from-MRI-images/blob/master/CNN_trial.ipynb
"""

!pip install tensorflow

import tensorflow as tf

print(tf.__version__)

#importing libraries
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten

#initialising the model
model=Sequential()

#add convolution layer
model.add(Convolution2D(32,(3,3),input_shape=(64,64,3),activation='relu'))

#add maxpooling layer
model.add(MaxPooling2D(pool_size=(2,2)))

#add flattening layer
model.add(Flatten())

#add hidden layer
model.add(Dense(128,activation='relu'))

#add output layer
model.add(Dense(1,activation='sigmoid'))

#Preprocessing images
from keras.preprocessing.image import ImageDataGenerator
train_datagen=ImageDataGenerator(rescale=1./255,shear_range=0.2,horizontal_flip=True,zoom_range=0.2)
test_datagen=ImageDataGenerator(rescale=1./255)



from google.colab import drive
drive.mount('/content/drive')

x_train=train_datagen.flow_from_directory(r'/content/drive/My Drive/brain_tumor_dataset/Train_data',target_size=(64,64),batch_size=32,class_mode='binary')

x_test=test_datagen.flow_from_directory(r'/content/drive/My Drive/brain_tumor_dataset/Test_data',target_size=(64,64),batch_size=32,class_mode='binary')

print(x_train.class_indices)

#compiling model
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=[tf.keras.metrics.Precision()])

model.fit_generator(x_train,steps_per_epoch=6,epochs=9,validation_data=x_test,validation_steps=2)

model.save('cnn.h5')

