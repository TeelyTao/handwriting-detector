Hand-Writing Detector

This Python project lets you interact with a pre-trained model for handwritten digit recognition (0-9). Draw a digit and get instant results with confidence scores!
Features

    Interactive Drawing: Draw digits using your mouse or touchpad.
    Instant Results: Press spacebar to see the predicted digit with confidence percentages.
    Pre-Trained Model: Leverages a pre-trained model for accurate predictions.

Requirements

    Python 3.11 or 3.12
    pygame
    tensorflow
    keras
    numpy

Installation

    Clone or download the repository.
    Install dependencies:

    pip install pygame tensorflow keras numpy


Usage

    Run the script:
    python mnist.py
Draw a digit (0-9) in the window.
Press spacebar to see the prediction:
    Confidence scores (0-99%) for each digit (0-9).
    Highlighted predicted digit with the highest confidence will be shown below the array.
