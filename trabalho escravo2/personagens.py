# personagens
import pygame

class Jardineiro:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.vel_x = 0
        self.vel_y = 0
        self.vel = 6
        self.direcao_x = 0
        self.direcao_y = 0
        
        self.jump_force = -15
        self.gravidade = 0.8
        self.chao = False

        self.largura = 45
        self.altura = 75
        self.cor = (255, 255, 255)
        self.modo = "regador"

         # Vida e status
        self.vida_maxima = 150
        self.vida = self.vida_maxima
        self.vidas = 3
        self.invulneravel = False
        self.tempo_invulneravel = 0
        self.pontuacao = 0

    def mover(self, direcao):
        if direcao == 'a':
            self.pos_x -= 1
        elif direcao == 'd':
            self.pos_x +=1
        elif direcao == 's':
            self.pos_y -=1
        elif direcao == 'w':
            self.pos_y += 1

    def update(self, keys, screen_width, screen_height, plataformas=None):
        if plataformas is None:
            plataformas = []
                 
        # Movimento horizontal
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.vel_x = -self.vel
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.vel_x = self.vel

        # Gravidade
        self.vel_y += self.gravidade
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

        # Invulnerabilidade
        if self.invulneravel:
            self.tempo_invulneravel -= 1
            if self.tempo_invulneravel <= 0:
                self.invulneravel = False

        # Colisão com plataformas (simplificada)
        self.chao = False
        for plat in plataformas:
            if self.vel_y >= 0:
                if (self.pos_x + self.largura > plat.x and
                    self.pos_x < plat.x + plat.largura and
                    self.pos_y + self.altura >= plat.y and
                    self.pos_y + self.altura - self.vel_y < plat.y):

                    self.pos_y = plat.y - self.altura
                    self.vel_y = 0
                    self.chao = True
                    break
        
        # Limites da tela
        if self.pos_x < 0:
            self.pos_x = 0
        if self.pos_x + self.largura > screen_width:
            self.pos_x = screen_width - self.largura

        # Caiu do mapa
        if self.pos_y > screen_height + 100:
            self.tomar_dano(999)
    
    def tomar_dano(self, quantidade):
        if not self.invulneravel:
            self.vida -= quantidade
            self.invulneravel = True
            self.tempo_invulneravel = 45
            
            if self.vida <= 0:
                self.morrer()

    def morrer(self):
        if self.vidas > 0:
            self.vidas -= 1
            self.vida = self.vida_maxima
            self.pos_x = 100
            self.pos_y = 300
            print(f"💀 Você virou adubo! Vidas restantes: {self.vidas}")
        else:
            print("💀 Hoje as plantas estão bem alimentadas...")
    
    def desenhar(self, tela):
        pygame.draw.circle(tela,(255,255,0),(self.pos_x,self.pos_y),20)

class Projetil:
    def __init__(self, x, y, direcao):
        self.x = x
        self.y = y
        self.velocidade = 8
        self.direcao = direcao
        self.largura = 15
        self.altura = 15
        self.dano = 20
        self.cor = (0, 255, 100)

    def update(self):
        self.x += self.velocidade * self.direcao

class planta_longa:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largura = 60
        self.altura = 65
        self.vida = 60
        self.vida_max = 60
        self.alcance_ataque = 275
        self.cooldown_ataque = 0
        self.cooldown_max = 105
        self.projetils = []
        self.estado = "idle"

    def update(self, jardineiro, plataformas=[]):
        if self.cooldown_ataque > 0:
            self.cooldown_ataque -= 1

        distancia = abs(jardineiro.pos_x - self.x)

        if distancia < self.alcance_ataque and self.cooldown_ataque == 0:
            self.atacar(jardineiro.pos_x > self.x)
            self.cooldown_ataque = self.cooldown_max

        # Atualiza projéteis
        for proj in self.projetils[:]:
            proj.update()
            if proj.x < -50 or proj.x > 1200:
                self.projetils.remove(proj)

    def atacar(self, para_direita):
        self.estado = "atacando"
        boca_x = self.x + 50 if para_direita else self.x + 10
        boca_y = self.y + 30
        direcao = 1 if para_direita else -1
        self.projetils.append(Projetil(boca_x, boca_y, direcao))

    def tomar_dano(self, quantidade):
        self.vida -= quantidade
        if self.vida <= 0:
            self.morrer()

    def morrer(self):
        print("🌿 Erva daninha podada!")


class planta_corpo_a_corpo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largura = 60
        self.altura = 65
        self.vida = 90
        self.vida_max = 90
        self.alcance_ataque = 85
        self.cooldown_ataque = 0
        self.cooldown_max = 55
        self.estado = "idle"
        self.dano = 20

    def update(self, jardineiro, plataformas=[]):
        if self.cooldown_ataque > 0:
            self.cooldown_ataque -= 1

        distancia = abs(jardineiro.pos_x - self.x)

        if distancia < self.alcance_ataque and self.cooldown_ataque == 0:
            self.atacar(jardineiro)
            self.cooldown_ataque = self.cooldown_max

    def atacar(self, jardineiro):
        self.estado = "atacando"
        if hasattr(jardineiro, 'tomar_dano'):
            jardineiro.tomar_dano(self.dano)

    def tomar_dano(self, quantidade):
        self.vida -= quantidade
        if self.vida <= 0:
            self.morrer()

    def morrer(self):
        print("🌿 Erva daninha podada!")
