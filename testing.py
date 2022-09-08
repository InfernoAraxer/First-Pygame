import pygame

pygame.init();

# Game Code

# Game Window
window = pygame.display.Info();
window_width = 1738; #window.getWidth();
window_height = 501; #window.getHeight();
window_rgb_color = (0, 0, 0);

game_window = pygame.display.set_mode((window_width, window_height));

clock = pygame.time.Clock();

background_image = pygame.image.load('assets/background.png');
treasure_image = pygame.image.load('assets/treasure.png');

window_height_scale = window_height;
window_width_scale = window_width;

if window_width > window_height:
    window_width_scale = window_height;
else:
    window_height_scale = window_width;

background_image = pygame.transform.scale(background_image, (window_width_scale, window_height_scale));
treasure_image = pygame.transform.scale(treasure_image, (window_width_scale/15, window_height_scale/15));

def run_game_loop():

    while True:

        # Handle Events
        events = pygame.event.get();
        for event in events:
            if event.type == pygame.QUIT:
                return;
            
        # Execute Logic
        

        # Update Display
        game_window.fill(window_rgb_color);

        background_width_padding = ((window_width-background_image.get_width())//2);
        background_height_padding = ((window_height-background_image.get_height())//2);

        treasure_width_padding = ((window_width-treasure_image.get_width())//2);
        treasure_height_padding = ((window_height-treasure_image.get_height())//2);

        game_window.blit(background_image, (background_width_padding, background_height_padding));
        game_window.blit(treasure_image, (treasure_width_padding, treasure_height_padding/7.5));

        pygame.display.update();

        clock.tick(60);


# class GameObject:
#     def __init__(self, x_position, y_position):
#         self.x_position = x_position;
#         self.y_position = y_position;

run_game_loop();

pygame.quit();
quit();