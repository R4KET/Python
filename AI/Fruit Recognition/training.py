# -*- coding: utf-8 -*-
"""trainingfv.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oq4Hp6cCo1R07SGuFkYxItIM5H0TguVk

#Importowanie zestawu danych
"""

from google.colab import drive
drive.mount('/content/drive')

"""#Importowanie bibliotek"""

import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

"""#Wstępne przetwarzanie danych

##Trening Przetwarzanie wstępne obrazu
"""

training_set = tf.keras.utils.image_dataset_from_directory(
    '/content/drive/MyDrive/FVR/train',
    labels = 'inferred',
    label_mode = 'categorical',
    class_names = None,
    color_mode = 'rgb',
    batch_size = 32,
    image_size = (64, 64),
    shuffle = True,
    seed = None,
    validation_split = None,
    subset = None,
    interpolation = 'bilinear',
    follow_links = False,
    crop_to_aspect_ratio = False
    )

# Ścieżka do katalogu zawierającego podkatalogi z obrazami dla każdej klasy
dataset_path = '/content/drive/MyDrive/FVR/train'

# Zbieranie nazw katalogów i liczby obrazów w każdym z nich
class_labels = []
class_counts = []

for class_name in os.listdir(dataset_path):
    class_dir = os.path.join(dataset_path, class_name)
    if os.path.isdir(class_dir):
        num_images = len(os.listdir(class_dir))
        class_labels.append(class_name)
        class_counts.append(num_images)

# Tworzenie wykresu
plt.figure(figsize=(10, 8))
plt.bar(class_labels, class_counts)
plt.xlabel('Klasy')
plt.ylabel('Ilość obrazów')
plt.title('Rozkład ilości obrazów na klasę w zbiorze treingowym')
plt.xticks(rotation=90)  # Obracanie etykiet dla lepszej czytelności
plt.show()

"""##Weryfikacja Przetwarzanie wstępne obrazu"""

validation_set = tf.keras.utils.image_dataset_from_directory(
    '/content/drive/MyDrive/FVR/validation',
    labels="inferred",
    label_mode="categorical",
    class_names=None,
    color_mode="rgb",
    batch_size=32,
    image_size=(64, 64),
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    interpolation="bilinear",
    follow_links=False,
    crop_to_aspect_ratio=False
)

# Ścieżka do katalogu zawierającego podkatalogi z obrazami dla każdej klasy
dataset_path = '/content/drive/MyDrive/FVR/validation'

# Zbieranie nazw katalogów i liczby obrazów w każdym z nich
class_labels = []
class_counts = []

for class_name in os.listdir(dataset_path):
    class_dir = os.path.join(dataset_path, class_name)
    if os.path.isdir(class_dir):
        num_images = len(os.listdir(class_dir))
        class_labels.append(class_name)
        class_counts.append(num_images)

# Tworzenie wykresu
plt.figure(figsize=(10, 8))
plt.bar(class_labels, class_counts)
plt.xlabel('Klasy')
plt.ylabel('Ilość obrazów')
plt.title('Rozkład ilości obrazów na klasę w zbiorze walidacyjnym')
plt.xticks(rotation=90)  # Obracanie etykiet dla lepszej czytelności
plt.show()

"""#Budowanie modelu CNN"""

cnn = tf.keras.models.Sequential()

"""##Budowanie warstwy konwulsji"""

cnn.add(tf.keras.layers.Conv2D(filters = 64, kernel_size = 3, activation = 'relu', input_shape = [64, 64, 3]))
cnn.add(tf.keras.layers.MaxPool2D(pool_size = 2, strides = 2))

cnn.add(tf.keras.layers.Conv2D(filters = 64, kernel_size = 3, activation = 'relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size = 2, strides = 2))

cnn.add(tf.keras.layers.Dropout(0.5)) #To avoid overfitting

cnn.add(tf.keras.layers.Flatten())

cnn.add(tf.keras.layers.Dense(units = 128, activation = 'relu'))

#Output Layer
cnn.add(tf.keras.layers.Dense(units = 36, activation = 'softmax'))

"""##Faza kompilacji i treningu"""

cnn.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

from keras.callbacks import ModelCheckpoint, EarlyStopping
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
model_checkpoint = ModelCheckpoint('best_model_CNN.h5', monitor='val_loss', save_best_only=True)

training_history = cnn.fit(
    x=training_set,
    validation_data=validation_set,
    epochs=50,
    callbacks=[early_stopping, model_checkpoint]
)

cnn.save('trained_model_v2.h5')

training_history.history #Return Dictionary of history

#Recording History in json
import json
with open('training_hist.json','w') as f:
  json.dump(training_history.history,f)

print(training_history.history.keys())

"""##Dokładność obliczeniowa modelu osiągnięta na zestawie walidacyjnym"""

print("Validation Set Accuracy: {} %".format(training_history.history['val_accuracy'][-1]*100))

"""#Wizualizacja dokładności

##Wizualizacja treningu
"""

training_history.history['accuracy']

epochs = [i for i in range(1, len(training_history.history['accuracy']) + 1)]
plt.plot(epochs,training_history.history['accuracy'], color = 'red')
plt.xlabel('Epoki')
plt.ylabel('Dokładność')
plt.title('Wizualizacja treningu dokładności')
plt.show()

"""##Dokładność walidacji"""

plt.plot(epochs, training_history.history['val_accuracy'], color = 'blue')
plt.xlabel("Numer Epoki")
plt.ylabel("Dokładność")
plt.title("Wizualizacja wyników dokładności walidacji")
plt.show()

training_loss = training_history.history['loss']
validation_loss = training_history.history['val_loss']

# Liczba epok
epochs = range(1, len(training_loss) + 1)

# Tworzenie wykresu
plt.figure(figsize=(10, 6))
plt.plot(epochs, training_loss, 'b-', label='Strata treningowa')
plt.plot(epochs, validation_loss, 'g-', label='Strata walidacyjna')
plt.title('Strata treningowa i walidacyjna na przestrzeni epok')
plt.xlabel('Epoki')
plt.ylabel('Strata')
plt.legend()
plt.show()