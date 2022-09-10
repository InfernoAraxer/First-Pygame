import pygame;
from gameObject import GameObject
from player import Player
from enemy import Enemy

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
        self.treasure = GameObject(0, (self.window_height_scale * -.425), self.window_width, self.window_height, 'assets/treasure.png', 1/15);

        self.player = Player(0, (self.window_height_scale * .425), self.window_width_scale, self.window_height_scale, 'assets/player.png', 1/15, 2.5);

        self.level = 1.0;
        self.reset_map();

    def reset_map(self):
        self.player = Player(0, (self.window_height_scale * .425), self.window_width_scale, self.window_height_scale, 'assets/player.png', 1/15, 2.5);

        speed = 1.5 + self.level;

        if self.level >= 4.0:
            self.enemies = [
                Enemy(0, (self.window_height_scale * .225), self.window_width_scale, self.window_height_scale, 'assets/enemy.png', 1/15, speed, 2, 2),
                Enemy((self.window_width_scale * .25), 0, self.window_width_scale, self.window_height_scale, 'assets/enemy.png', 1/15, speed, 2, 2),
                Enemy((self.window_width_scale * -.25), (self.window_height_scale * -.225), self.window_width_scale, self.window_height_scale, 'assets/enemy.png', 1/15, speed, 3, 1),
            ]
        elif self.level >= 2.0:
            self.enemies = [
                Enemy(0, (self.window_height_scale * .225), self.window_width_scale, self.window_height_scale, 'assets/enemy.png', 1/15, speed, 2, 2),
                Enemy((self.window_width_scale * -.25), (self.window_height_scale * -.225), self.window_width_scale, self.window_height_scale, 'assets/enemy.png', 1/15, speed, 3, 1),
            ]
        else:
            self.enemies = [
                Enemy(0, (self.window_height_scale * .225), self.window_width_scale, self.window_height_scale, 'assets/enemy.png', 1/15, speed, 2, 2),
            ]

    def draw_objects(self):

        self.game_window.fill(self.window_rgb_color);

        self.game_window.blit(self.background.image, (self.background.x, self.background.y));
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y));
        self.game_window.blit(self.player.image, (self.player.x, self.player.y));

        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y));

        pygame.display.update();

    def detect_collision(self, object_1, object_2):
        if object_1.y > (object_2.y + object_2.image.get_height()):
            return False;
        elif object_2.y > (object_1.y + object_1.image.get_height()):
            return False;

        if object_1.x > (object_2.x + object_2.image.get_width()):
            return False;
        elif object_2.x > (object_1.x + object_1.image.get_width()):
            return False;

        return True;

    def move_objects(self, player_direction):
            self.player.move(player_direction);
            
            for enemy in self.enemies:
                enemy.move();

    def check_if_collided(self):
        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                self.level = 1.0;
                return True;

        if self.detect_collision(self.player, self.treasure):
            self.level += 0.5;
            return True;
        return False;

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
            self.move_objects(player_direction);

            # Update Display
            self.draw_objects();

            # Detect Collisions
            if self.check_if_collided():
                self.reset_map();

            self.clock.tick(60);