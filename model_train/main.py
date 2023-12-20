import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers.legacy import Adam
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/dataset/jakarta_transport.csv', delimiter=';')

# Drop rows with NaN values
df.dropna(inplace=True)
unique_modes = df['Mode'].unique()
print(unique_modes)

# Encode the 'Mode' column
label_encoder = LabelEncoder()
df['Mode'] = label_encoder.fit_transform(df['Mode'])

# Define features and target
X = df[['Distance', 'TravelTime']]
y = df['Mode']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
np.save('scaler.npy', scaler)

# Deep learning model
model = Sequential()
model.add(Dense(256, input_dim=2, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(32, activation='gelu'))
model.add(Dense(5, activation='softmax'))


class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if (logs.get('accuracy') > 0.75 and logs.get('val_accuracy') > 0.75):
            print("\nTarget accuracy acquired, stopping...")
            self.model.stop_training = True


customCallback = myCallback()

model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])

# Train the model and store training history
history = model.fit(X_train, y_train, epochs=1000, batch_size=64, validation_split=0.2, callbacks=[customCallback])

# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {accuracy * 100:.2f}%')

# Save the model
model.save('ImprovedTransportModel.h5')

# Plot training history
plt.figure(figsize=(12, 6))

# Plot training & validation accuracy values
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Validation'], loc='upper left')

# Plot training & validation loss values
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Train', 'Validation'], loc='upper left')

plt.tight_layout()

# Save the plot
plt.savefig('training_history_plot.png')

plt.show()
