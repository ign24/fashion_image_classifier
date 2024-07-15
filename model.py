import numpy as np
from PIL import Image
import tensorflow as tf

def load_and_train_model():
    fashion_mnist = tf.keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


    train_images = train_images / 255.0
    test_images = test_images / 255.0


    train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
    test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))


    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])


    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])


    model.fit(train_images, train_labels, epochs=10, validation_split=0.2)


    model.save('model_fashion_mnist.h5')

    return model

def load_model():

    return tf.keras.models.load_model('model_fashion_mnist.h5')

def process_image(file):
    image = Image.open(file.stream).convert('L')
    image = image.resize((28, 28))
    image_array = np.array(image) / 255.0
    image_array = image_array.reshape((1, 28, 28, 1))

    model = load_model()
    predictions = model.predict(image_array)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    confidence = np.max(predictions)

    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    return {
        'predicted_class': class_names[predicted_class_index],
        'confidence': float(confidence),
    }

if __name__ == '__main__':
    model, accuracy = load_and_train_model()
