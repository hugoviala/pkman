import pygame
import pkmath
import pkcolor

class Player:
    """ class to handle all the details about a player entity """
    def __init__(self, x, y, w, h):
        self.p = pkmath.v2(x, y)
        self.dp = pkmath.v2(0, 0)
        self.w = w
        self.h = h


def updateAndRender(user_input, window_surface,
                    player):
    """ update the game and render the current frame """
    # TODO(hugo): maybe consider acceleration and equations of motion
    # for a better game feel
    player.dp = pkmath.v2(0, 0)
    if user_input.move_up:
        player.dp = pkmath.add(player.dp, pkmath.v2(0, -50))
    if user_input.move_down:
        player.dp = pkmath.add(player.dp, pkmath.v2(0, 50))
    if user_input.move_left:
        player.dp = pkmath.add(player.dp, pkmath.v2(-50, 0))
    if user_input.move_right:
        player.dp = pkmath.add(player.dp, pkmath.v2(50, 0))
    player.p = pkmath.add(player.p, pkmath.times(user_input.dt, player.dp))
    player_rect = pygame.Rect(player.p.x, player.p.y, player.w, player.h)
    window_surface.fill(pkcolor.red, player_rect)
    return (player.p.x, player.p.y)
