from gameObject import GameObject

class Player(GameObject):

    def __init__(self, x, y, width, height, image_path, scale, speed):
        super().__init__(x, y, width, height, image_path, scale);

        self.speed = speed;

    def move(self, direction):
        self.y += (direction * self.speed);
