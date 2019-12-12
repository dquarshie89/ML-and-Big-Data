import tensorflow as tf
#config = tf.ConfigProto()
#config.gpu_options.allow_growth = True
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D

######
#Load MNIST data and split train and test
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
#Look at the dimensions of the train data
X_train.shape #60,000 images with 28x28 pixels

######
#Show a image preview 
image_num = 50000
plt.imshow(X_train[image_num], cmap='Greys')
#Show image label
print(y_train[image_num]) 

######
#Reshaping the array to 4-dims so that it can work with the Keras
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)

# Normalizing the RGB codes by dividing it to the max RGB value.
X_train = X_train.astype('float32')/255.0
X_test = X_test.astype('float32')/255.0
#Show new shape
print('x_train shape:', X_train.shape)
#print('Number of images in x_train', X_train.shape[0])
#print('Number of images in x_test', X_test.shape[0])

#######
##Build CNN
input_shape = (28, 28, 1)
# Creating the model and adding layers
model = Sequential()
model.add(Conv2D(28, kernel_size=(3,3), input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2)))
#Flatten the 2D arrays in order to get fully connected layers
model.add(Flatten()) 
model.add(Dense(128, activation=tf.nn.relu))
model.add(Dropout(0.2))
model.add(Dense(10,activation=tf.nn.softmax))

#####
#Compile and fit the model 
model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])
model.fit(x=X_train,y=y_train, epochs=15)

#####
#Evaluate
model.evaluate(X_test, y_test)

prediction_image = 4444
plt.imshow(X_test[prediction_image].reshape(28, 28),cmap='Greys')
pred = model.predict(X_test[prediction_image].reshape(1, 28, 28, 1))
print(pred.argmax())
