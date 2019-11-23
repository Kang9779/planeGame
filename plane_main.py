import pygame
from plane_sprites import *


class PlaneGame(object):
    '''飞机大战主游戏'''

    def __init__(self):
        print("游戏初始化")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()

    def __create_sprites(self):
        pass

    def start_game(self):
        print("游戏开始...")
        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()
        
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            

    def __check_collide(self):
        pass
    def __update_sprites(self):
        pass

    @staticmethod
    def __game_over():
        print("游戏结束!")
        pygame.quit()
        exit()





if __name__ == "__main__":

    game = PlaneGame()

    game.start_game()
