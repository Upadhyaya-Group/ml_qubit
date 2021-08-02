
#import tensorflow. (We are probably gonna need it!)
import tensorflow as tf



#say hello to confirm working import and printing
print("hello world!");


#load the mnist dataset, a commonly used database of hand-drawn digits. We will use this as our sample training and validation data
mnist = tf.keras.datasets.mnist


#convert the samples from integer values (0 to 255) into floating points (0.0 to 1.0)
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0


#build the model by stacking layers; choose optimizer and loss function. Here we set the activation function to a 'relu'
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

# get the predictions for the second datapoint
predictions = model(x_train[:1]).numpy()

# print the raw predictions for that datapoint. Note that these are "logits" or "log-odds" scores, which is related to the probability, 
# and also is the inverse of the sigmoid function
print("logits prediction: ");
print(predictions);

# we can use the softmax function to convert these logits to probabilities for each preciction class
print("odds prediction: ");
print(tf.nn.softmax(predictions).numpy());


# since the model is untrained we expect basically random values for each class, which is what we get



# get the loss function as a SparseCategoricalCrossentropy loss from tf.keras.losses. 
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True);


'''
from https://www.tensorflow.org/tutorials/quickstart/beginner

"This loss is equal to the negative log probability of the true class: It is zero if the model is sure of the correct class.

This untrained model gives probabilities close to random (1/10 for each class), so the initial loss should be close to -tf.math.log(1/10) ~= 2.3."
'''

# display loss
print("loss:");
print(loss_fn(y_train[:1], predictions).numpy());

# the loss is relatively large, because like we said earlier, the model is untrained



# compile the model to allow for optimization ( in this case we are using adam ) for increased model training and evaluation efficiency
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])



# train the model over 5 epochs (repetitions)
model.fit(x_train, y_train, epochs=5)


# test the performance of the model ( usually would be over a validation or test set )
model.evaluate(x_test,  y_test, verbose=2)

# the model is now trained to ~98% accuracy. Pretty good!



# you can wrap the trained model and attatch a softmax to it if you want it to return probabilities
probability_model = tf.keras.Sequential([
  model,
  tf.keras.layers.Softmax()
])
