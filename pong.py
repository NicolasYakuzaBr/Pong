import pygame
import random

pygame.init()

largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Pong")
fps = pygame.time.Clock()

# Definindo as cores
preto = (0, 0, 0)
branco = (255, 255, 255)

# Definindo a posição inicial das raquetes
posicao_jogador = [20, altura_tela // 2 - 50]
posicao_computador = [largura_tela - 40, altura_tela // 2 - 50]

# Definindo a posição inicial da bola
posicao_bola = [largura_tela // 2, altura_tela // 2]
velocidade_bola = [random.choice([-5, 5]), random.choice([-5, 5])]
tamanho_bola = 10

# Definindo o tamanho das raquetes
tamanho_raquete = [20, 100]

def desenhar_objetos():
    tela.fill(preto)
    pygame.draw.rect(tela, branco, (posicao_jogador[0], posicao_jogador[1], tamanho_raquete[0], tamanho_raquete[1]))
    pygame.draw.rect(tela, branco, (posicao_computador[0], posicao_computador[1], tamanho_raquete[0], tamanho_raquete[1]))
    pygame.draw.circle(tela, branco, posicao_bola, tamanho_bola)

def atualizar_posicao():
    # Movendo a bola
    posicao_bola[0] += velocidade_bola[0]
    posicao_bola[1] += velocidade_bola[1]

    # Verificando colisões com as bordas da tela
    if posicao_bola[1] <= tamanho_bola or posicao_bola[1] >= altura_tela - tamanho_bola:
        velocidade_bola[1] = -velocidade_bola[1]
    if posicao_bola[0] <= tamanho_bola or posicao_bola[0] >= largura_tela - tamanho_bola:
        velocidade_bola[0] = -velocidade_bola[0]

    # Verificando colisões com as raquetes
    if posicao_jogador[1] <= posicao_bola[1] <= posicao_jogador[1] + tamanho_raquete[1] and posicao_jogador[0] + tamanho_raquete[0] >= posicao_bola[0] >= posicao_jogador[0]:
        velocidade_bola[0] = -velocidade_bola[0]
    if posicao_computador[1] <= posicao_bola[1] <= posicao_computador[1] + tamanho_raquete[1] and posicao_computador[0] <= posicao_bola[0] <= posicao_computador[0] + tamanho_raquete[0]:
        velocidade_bola[0] = -velocidade_bola[0]

    # Movendo a raquete do jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        posicao_jogador[1] -= 5
    if keys[pygame.K_DOWN]:
        posicao_jogador[1] += 5

    # Mantendo a raquete do jogador dentro da tela
    if posicao_jogador[1] < 0:
        posicao_jogador[1] = 0
    if posicao_jogador[1] > altura_tela - tamanho_raquete[1]:
        posicao_jogador[1] = altura_tela - tamanho_raquete[1]

    # Movendo a raquete do computador
    if posicao_bola[1] < posicao_computador[1] + tamanho_raquete[1] // 2:
        posicao_computador[1] -= 5
    if posicao_bola[1] > posicao_computador[1] + tamanho_raquete[1] // 2:
        posicao_computador[1] += 5

    # Mantendo a raquete do computador dentro da tela
    if posicao_computador[1] < 0:
        posicao_computador[1] = 0
    if posicao_computador[1] > altura_tela - tamanho_raquete[1]:
        posicao_computador[1] = altura_tela - tamanho_raquete[1]

def desenhar():
    # Desenhando a tela
    tela.fill(preto)

    # Desenhando a bola
    pygame.draw.circle(tela, branco, posicao_bola, tamanho_bola)

    # Desenhando as raquetes
    pygame.draw.rect(tela, branco, (posicao_jogador[0], posicao_jogador[1], tamanho_raquete[0], tamanho_raquete[1]))
    pygame.draw.rect(tela, branco, (posicao_computador[0], posicao_computador[1], tamanho_raquete[0], tamanho_raquete[1]))

    # Desenhando a linha do meio
    pygame.draw.line(tela, branco, (largura_tela // 2, 0), (largura_tela // 2, altura_tela))

    # Atualizando a tela
    pygame.display.update()

run = True
while run:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False

    desenhar_objetos()
    desenhar()
    atualizar_posicao()
    fps.tick(60)
    pygame.display.update()
pygame.quit()
