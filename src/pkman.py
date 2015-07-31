import pygame
import input
import game

if __name__ == "__main__":

    pygame.init()
    clock = pygame.time.Clock()
    window_size = (700, 500)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("PKMAN")
    game_running = True
    user_input = input.UserInput()
    window_surface = pygame.display.get_surface()
    player_x = 100
    player_y = 100
    player_w = 30
    player_h = 30
    while game_running:
        user_input.reset()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            else:
                user_input.processEvent(event)
        screen.fill((255, 255, 255))
        # TODO(hugo): should the flip be at that moment ?
        (player_x, player_y) = game.updateAndRender(
            user_input, window_surface,
            player_x, player_y, player_w, player_h)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
