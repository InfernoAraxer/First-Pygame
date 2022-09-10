from turtle import left, right
from gameObject import GameObject

class Enemy(GameObject):
    
    def __init__(self, x, y, width, height, image_path, scale, speed, right_block, left_block):
        super().__init__(x, y, width, height, image_path, scale);

        self.speed = speed;
        self.left_block = left_block;
        self.right_block = right_block;

    def move(self):
        if (self.x >= self.width - self.image.get_width() - (self.width * self.left_block/15)):
            self.speed = -self.speed;
        elif (self.x <= self.width*self.right_block/15):
            self.speed = abs(self.speed);
        
        self.x += self.speed;

    