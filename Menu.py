# menu.py
import pygame
import sys

pygame.init()

LARGURA = 800
ALTURA = 600
PRETO = 0,0,0
CURSOR = 0,128,0
BRANCO = (255, 255, 255)
VERDE_CLARO = 144,238,144
CINZA = (180, 180, 180)
tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Menu - Jardinagem infinita")
relogio = pygame.time.Clock()

fonte_titulo = pygame.font.SysFont("arial", 80, bold=True)
fonte_botao = pygame.font.SysFont("arial", 40, bold=True)
fonte_info = pygame.font.SysFont("arial", 28)


class Botao:
    def __init__(self, x, y, largura, altura, texto, cor=VERDE_CLARO):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.cor = cor
        self.cor_hover = CURSOR

    def desenhar(self, superficie, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            cor_atual = self.cor_hover
        else:
            cor_atual = self.cor

        pygame.draw.rect(superficie, cor_atual, self.rect, border_radius=25)
        
        texto_surf = fonte_botao.render(self.texto, True, BRANCO)
        texto_rect = texto_surf.get_rect(center=self.rect.center)
        superficie.blit(texto_surf, texto_rect)

    def clique(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

botao_jogar = Botao(LARGURA//2 - 150, 220, 300, 70, "Jogar")
botao_opcoes = Botao(LARGURA//2 - 150, 310, 300, 70, "Creditos")
botao_sair = Botao(LARGURA//2 - 150, 400, 300, 70, "Sair")

estado_atual = "menu"
rodando = True

while rodando:
    mouse_pos = pygame.mouse.get_pos()  

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if estado_atual == "menu":
                if botao_jogar.clique(mouse_pos):
                    estado_atual = "jogo"
                    print(">>> Iniciando o jogo!")
                
                elif botao_opcoes.clique(mouse_pos):
                    print(">>> Abrindo menu de OPÇÕES")
                
                elif botao_sair.clique(mouse_pos):
                    print(">>> Saindo do jogo...")
                    rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                if estado_atual == "jogo":
                    estado_atual = "menu"  
                    print("<<< Voltando ao menu")
                else:
                    rodando = False 
    
    tela.fill(PRETO)
    
    if estado_atual == "menu":
        titulo = fonte_titulo.render("MEU JOGO", True, BRANCO)
    titulo_rect = titulo.get_rect(center=(LARGURA//2, 120))
    tela.blit(titulo, titulo_rect)
    
    subtitulo = fonte_info.render("Menu Principal", True, CINZA)
    subtitulo_rect = subtitulo.get_rect(center=(LARGURA//2, 175))
    tela.blit(subtitulo, subtitulo_rect)
    
    botao_jogar.desenhar(tela, mouse_pos)
    botao_opcoes.desenhar(tela, mouse_pos)
    botao_sair.desenhar(tela, mouse_pos)
    
    instrucao = fonte_info.render("Clique nos botões com o mouse", True, CINZA)
    instrucao_rect = instrucao.get_rect(center=(LARGURA//2, 520))
    tela.blit(instrucao, instrucao_rect)
    
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
sys.exit()
