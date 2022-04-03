import pandas as pd
df = pd.read_csv('inputs1.csv')

dataset = df.values
X = dataset[:,0:6]
Y = dataset[:,6]
from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)
from sklearn.model_selection import train_test_split
X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size=0.3)
X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)
X_test=X_scale
Y_test=Y
print(X_train.shape, X_val.shape, X_test.shape, Y_train.shape, Y_val.shape, Y_test.shape)
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras import regularizers
model = Sequential([
    Dense(1000, activation='relu', kernel_regularizer=regularizers.l2(0.01), input_shape=(6,)),
    Dropout(0.1),
    Dense(1000, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    Dropout(0.3),
    Dense(1000, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    Dropout(0.5),
    Dense(1, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
              
hist = model.fit(X_train, Y_train,
          batch_size=158, epochs=10,
          validation_data=(X_val, Y_val))

model.evaluate(X_test, Y_test)[1]

model.save("model1.h5")
