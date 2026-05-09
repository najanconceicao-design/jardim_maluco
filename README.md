# garden_alive

2. Descrição Geral

o jogo será um jogo 2d de plataforma. Para o público juvenil adolescente.
o ambiente do jogo irá se passar em um jardin gigantesco com obstáculos característicos de um jardin e com o adendo de ter flores carnívoras e violentas.
a Ideia do game, é mistura a gameplay dinâmica de matar inimigos diversos, junto com plataforma. enquanto o jogo mostra o passado do protagonista e acaba transformando a estética cartoonesca para algo mais pertubador.

3. Objetivo do Jogo

O jogador terá que OBRIGATORIAMENTE derrotar todos os inimigos e concluir os objetivos para passar de mundo/fase.
e o objetivo do jogo será passar pelas 3 fases até chegar na última e derrotar o boss final e assim revelar a verdade e por termina a lore do protagonista.

4. Personagem Principal

O personagem é um jardineiro famoso pelo seu trabalho impecável e rápido, nunca precisando de equipamento pesado ou veneno, ele sempre  consegue fazer um trabalho ótimo com ferramentas básicas.
O personagem irá andar em 3 direções, para esquerda e direita com as setas do teclado e para cima com o botão espaço. Além disso ele tera 3 de vida, 2 estados podendo alterna entre eles e velocidade de movimentação básica.

5. Inimigos e Obstáculos
Deve descrever:

Todos os inimigos de jogo serão plantas, nunca saindo de seu lugares, mas ainda sendo letais sendo de longa a curta distância.

Plantas de curta distância:
São plantas que só atacaram se o player, se  chegar em sua área de alcance, cada ataque terá um tempo de carregamento antes de poder  atacar de novo. Mas se o player for atacado e for atingido, ele sofrera dano. Entretanto, o player não tomara dano se passar por dentro das plantas, mas só durante o tempo de carregamento entre os ataques.

Plantas de longo alcance:
São plantas que lançaram projéteis(suas pétalas) em direção ao player, tento uma área de visão muito maior podendo ver o player de longe, se o projétil antinger o player, player tomara dano. seus projéteis podem variar de velocidade dependendo da planta. Cada projetel também terá um tempo de recargar, ( não podendo transforma planta em um fuzil). 

Plantas especiais: 
Serão plantas únicas com mecânicas especiais, que também atacaram o player mas de formas diferentes das outras.

Como se derrota as plantas? 
Existe 2 formas de matar plantas, Cortando elas com a tesoura gigante ou regando elas. Porém as plantas só podem morrer para um tipo, esse tipo irá aparecer na cabeças delas como um ícone, exemplo:

Tem uma planta de longo alcance, mas na cabeça dela tem um ícone de regador. O jogador só poderá neutralizar aquela flor regando ela.

6. Cenário (Mapa)

O ambiente do jogo será tematizado em um jardim, logo todos os obstáculos (além das plantas) serão objetos característicos de um jardim, cortadores de grama, piscinas, arbustos, gnomos, casa dos pets, etc...
O jogo não ter vai itens coletaveis pelo mapa.
O objetivo final será chegar no fim do jardim, onde está um túmulo e o boss.

7. Sistema de Pontuação

O jogador ganhara ponto a cada inimigo derrotado. Cada planta derrotada  valer 5 pontos.

8. Sistema de Vida

A quantidade de vida inicial do player será 3, ele perdera vida a cada ataque que sofrer das plantas malignas. O jogador pode recuperar vida achando certas plantas curativas que quando regadas te dão +1 vida. Quando a vida do player acabar,
O jogo irá mostra a tela de game over com a opção de ir  por "menu" ou "continuar", caso o player decide "continuar" o jogador retornará para o começo de cada fase.

9.  Controles

A - para esquerda
D - para a direta
SPACE - para pular
R- para trocar de modo ( modo tesoura gigante e modo regador)
T - menu
Botão do mouse - para atacar

10. Fluxo do Jogo

O jogo ira comeca em um tutorial básico em que ensina como mudar de modos, como matar e o parkour.
Após a introdução começará a primeira fase, sendo a parte da frente do jardim, onde terá os inimigos que atacam de forma lenta a o parkour é complexo o suficiente para o player pegar o jeito. O resto do jogo irá se desenrola com a velocidade de ataque dos inimigos aumentando além do número deles aumentarem e o parkour fica difícil, a cada final de fase irá se contar um pequeno trecho do passado do protagonista onde o jogador terá que montar e resolver mentalmente. Se para ser derrotado no jogo você tem que morrer pra qualquer inimigo durante o jogo, na cutcene de derrota, o protagonista desiste de chegar até o fim e vai embora, mas para vencer o jogo, o player tem que chegar até o fim e derrotar o boss, se o player ganhar do boss mostra a última cutcene e termina o jogo.

11. Regras do Jogo

- jogador não pode atravessar o chão e nem atravessar por dentro dos obstáculos ( exceto as plantas) 

-os projéteis das plantas lançadores não podem atravessar o chão e nem outros obstáculos. O projéteis tem que sumir quando batem em alguma colisão que não seja o player

-quando o player estiver regando uma planta, ele deve esperar uma barrinha que aparece na cabeça das plantas encher,  ele não poderá sair de perto.

-planta que estão sendo regadas não podem atacar o player

-os obstáculos não podem ser impossíveis de completar para o player.

-o tempo de recargar dos ataques dos inimigos e do player  devem ser coerentes, não podendo ser super rápidos ou lentos demais.

-os inimigos só podem atacar o player quando ele estiver em sua área de alcance.

12. Estrutura do Projeto

-startgame.py
      -começar o jogo

-settings.py
      -configurar o jogo 

-personagens.py
      -código do player
      -código dos inimigos

-map.py
      -desenhar e montar o mapa

13. Funcionalidades Mínimas

-movimentação do player
-base do mapa
-colisão 
-mecânica dos ataques dos nimigos de curto alcance

14.  Melhorias Futuras

- mecânicas únicas para as plantas

-design dos mapas

-história 
