import pygame

class GameObject:

    def __init__(self, x, y, width, height, image_path, scale):
        image = pygame.image.load(image_path);
        self.image = pygame.transform.scale(image, (width*scale, height*scale));

        self.x = x + (width - self.image.get_width())//2;
        self.y = y + (height - self.image.get_height())//2;
        self.width = self.image.get_width();
        self.height = self.image.get_height();