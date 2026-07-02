#Plataformas
import pygame

class Plataforma:
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

    def desenhar(self, tela):
        pygame.draw.rect(tela, (34, 139, 34), (self.x, self.y, self.largura, self.altura))  # verde