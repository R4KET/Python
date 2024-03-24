import sys
import pygame

class BlueSky:
    
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Blue Sky")
        self.screen = pygame.display.set_mode((1024, 768))
        self.bg_color = (0, 0, 255)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()


if __name__ == '__main__':
    game = BlueSky()
    game.run_game()