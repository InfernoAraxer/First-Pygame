import pygame
from gameClass import gameClass

pygame.init();

# Game Code
window = pygame.display.Info();
game = gameClass(800, 800);
game.run_game_loop();

pygame.quit();
quit();