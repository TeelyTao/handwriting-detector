import pygame
import tensorflow as tf
import keras
import numpy as np
from pygame.locals import *
pygame.init()
SCREEN_WIDTH = 279
SCREEN_HEIGHT = 279
color = (0, 0, 0, 255)  # Black background (adjust for transparency if needed)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
run = True
drawing = False
mnist = True
input=[]
screen.fill(color)
while run:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == MOUSEBUTTONUP:
            drawing = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                for j in range (28):
                    for i in range(28):
                        colourin = screen.get_at(((i * 10) + 5, (j * 10) + 5))
                        realcolour = (colourin[0] / 255)
                        input.append(realcolour)
                run = False            
    if drawing:
        mouse_position = pygame.mouse.get_pos()
        mouse_position = list(mouse_position)
        mouse_position[0] = (mouse_position[0] -(mouse_position[0] % 10))
        mouse_position[1] = (mouse_position[1] - (mouse_position[1] % 10))
        mouse = pygame.Rect(mouse_position[0], mouse_position[1], 10, 10)
        # Draw the rectangle after clearing the screen
        # Draw the red rectangle
        pygame.draw.rect(screen, (255, 255, 255), mouse)
    # Update the display after drawing
pygame.quit()
new_model = tf.keras.models.load_model('keras_mnist.keras')
input_numpy = np.array(input)
input_numpy = np.expand_dims(input_numpy, axis=0)
predictions = new_model.predict(input_numpy)
np.set_printoptions(formatter={'float_kind':'{:f}'.format})
confidences = []
for i in predictions:
   confidences.append(i * 100)
print(confidences)
maxa = np.argmax(confidences)
print(maxa)

