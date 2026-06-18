# jogo
from personagens import Jardineiro, planta_longa, planta_corpo_a_corpo
import pygame

class Jogo:
    def __init__(self):
        pygame.init
        self.largura = 580
        self.altura = 580
        
        self.tela = pygame.display.set_mode((self.altura,self.largura))
        self.rodando = True 
        self.clock=pygame.time.Clock()
        self.jardineiro = Jardineiro(200,200)
    
    def verificar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando=False
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_LEFT]:
            self.jardineiro.mover('a')
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_RIGHT ]:
            self.jardineiro.mover('d')
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_UP]:
            self.jardineiro.mover('s')
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_DOWN]:
            self.jardineiro.mover('w')
    
    def iniciar(self):
        while self.rodando:
            self.verificar_eventos()
            self.desenhar()
            self.clock.tick(60)