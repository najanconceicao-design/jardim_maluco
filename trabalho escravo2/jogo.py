# jogo
import pygame
import sys
from personagens import Jardineiro
from plataforma import Plataforma

class Jogo:
    def __init__(self):
        pygame.init()
        self.largura = 900
        self.altura = 600
        
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Jardineiro - Plataforma")
        
        self.rodando = True
        self.clock = pygame.time.Clock()
        
        self.jardineiro = Jardineiro(150, 200)
        
        self.plataformas = [
            Plataforma(0, 550, 900, 50),        
            Plataforma(200, 420, 180, 25),
            Plataforma(500, 320, 180, 25),
            Plataforma(150, 220, 120, 25),
            Plataforma(650, 450, 150, 25),
        ]

    def verificar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False

    def atualizar(self):
        teclas = pygame.key.get_pressed()
        self.jardineiro.update(teclas, self.largura, self.altura, self.plataformas)

    def desenhar(self):
        self.tela.fill((25, 25, 45))

        for plataforma in self.plataformas:
            plataforma.desenhar(self.tela)

        self.jardineiro.desenhar(self.tela)

        pygame.display.flip()

    def iniciar(self):
        while self.rodando:
            self.verificar_eventos()
            self.atualizar()
            self.desenhar()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    jogo = Jogo()
    jogo.iniciar()