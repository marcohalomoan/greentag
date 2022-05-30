import cv2
import numpy as np
import os
import io
import sys
import tensorflow as tf
import PySimpleGUI as sg
from PIL import Image

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 2
TEST_SIZE = 0.4
file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

def main():
    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])


    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Build user interface
    layout = [
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Image"),
            sg.Button("Validate")
        ],
    ]
    window = sg.Window("Image Viewer", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                image.thumbnail((640, 480))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
        if event == "Validate":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                result = process(filename, model)
                if result == 'secured':
                    sg.theme('Green')
                else:
                    sg.theme('DarkRed1')
                sg.popup(result)
    window.close()

# Use the model to predict new image
def process(image, model):
    img2 = cv2.imread(image)
    img2 = cv2.resize(img2, (IMG_WIDTH, IMG_HEIGHT))
    array_img = np.array([img2])
    """
    Output of '1.0' means secured, '0.0' means not secured
    return the result to main() function
    """
    if int(model.predict(array_img)[0][1]) == 1:
        result = 'secured'
    else:
        result = 'not secured'
    return result

def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    folders = [f[0] for f in os.walk(data_dir)]
    images = []
    labels = []
    folders.remove('greentag')
    for folder in folders:
        files = [f for f in os.listdir(folder)]
        for image in files:
            img = cv2.imread(f'{folder}\{image}')
            img = cv2.resize(img,(IMG_WIDTH, IMG_HEIGHT))
            images.append(img)
            labels.append(folder.replace('greentag\\',''))
    return tuple([images, labels])

def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """

    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(
            64, (3, 3), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
        ),

        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        tf.keras.layers.Conv2D(
            64, (3, 3), activation="relu",
        ),

        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        tf.keras.layers.Flatten(),

        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.5),

        tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
    ])
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=["accuracy"]
    )
    return model

if __name__ == "__main__":
    main()
