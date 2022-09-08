import pygame;
from gameObject import GameObject
from player import Player

class gameClass:

    def __init__(self, width, height):

        # Game Window
        self.window_width = width;
        self.window_height = height;
        self.window_rgb_color = (0, 0, 0);

        self.game_window = pygame.display.set_mode((self.window_width, self.window_height));

        self.clock = pygame.time.Clock();

        self.window_height_scale = self.window_height;
        self.window_width_scale = self.window_width;

        if self.window_width > self.window_height:
            self.window_width_scale = self.window_height;
        else:
            self.window_height_scale = self.window_width;

        self.background = GameObject(0, 0, self.window_width, self.window_height, 'assets/background.png', 1);
        self.treasure = GameObject(0, 0, self.window_width, self.window_height, 'assets/treasure.png', 1/15);

        self.player = Player(0, 0, self.window_width_scale, self.window_height_scale, 'assets/player.png', 1/15, 10);

    def draw_objects(self):

        self.game_window.fill(self.window_rgb_color);

        self.game_window.blit(self.background.image, (self.background.x, self.background.y));
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y/7.5));
        self.game_window.blit(self.player.image, (self.player.x, self.player.y + (self.window_height * .425)));


    def run_game_loop(self):
        player_direction = 0;
        
        while True:
            
            # Handle Events
            events = pygame.event.get();
            for event in events:
                if event.type == pygame.QUIT:
                    return;
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction = -1;
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1;
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0;
            # Execute Logic
            self.player.move(player_direction);

            # Update Display
            self.draw_objects();

            pygame.display.update();

            self.clock.tick(60);