# Fashion Image Classifier API

This project provides a Flask API for classifying fashion items in images using a pre-trained TensorFlow Keras model. The model is based on the Fashion MNIST dataset, which includes 10 different categories such as T-shirts/tops, Trousers, Pullovers, Dresses, Coats, Sandals, Shirts, Sneakers, Bags, and Ankle boots.

## Features

- Image classification using a deep learning model.
- REST API to submit images and receive predicted categories.
- Simple and intuitive responses including prediction accuracy.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.8+
- Docker (for containerization and deployment)

## Installation

Follow these steps to get your development environment running:

1. Clone the repository:

   git clone https://github.com/yourusername/fashion-image-classifier.git

2. Navigate to the project directory:

    cd fashion-image-classifier

3. Install the required Python libraries:  

    pip install -r requirements.txt


## Running Locally

    python app.py


## Using Docker

    docker build -t fashion-classifier .
    docker run -p 5000:5000 fashion-classifier

## Making a prediction

To make a prediction, send a POST request to the /predict endpoint with an image file:

curl -X POST -F "file=@path_to_your_image.jpg" http://localhost:5000/predict


## License

Distributed under the MIT License. See LICENSE for more information.
