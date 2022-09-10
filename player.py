from tkinter import Scale
from gameObject import GameObject

class Player(GameObject):

    def __init__(self, x, y, width, height, image_path, scale, speed):
        super().__init__(x, y, width, height, image_path, scale);

        self.speed = speed;

    def move(self, direction):
        # print(self.y, (self.height - self.image.get_height()))
        if (self.y >= self.height - self.image.get_height()) and direction is 1:
            return
        elif (self.y <= 0) and direction is -1:
            return
        
        self.y += (direction * self.speed);

