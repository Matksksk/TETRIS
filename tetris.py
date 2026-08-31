import pygame
import random
    
pygame.init()

LARGURA_TELA, ALTURA_TELA = 500, 600
TAMANHO_BLOCO = 30

LARGURA_TABULEIRO = 10 * TAMANHO_BLOCO
ALTURA_TABULEIRO = 20 * TAMANHO_BLOCO

POSICAO_TABULEIRO_X = (LARGURA_TELA - LARGURA_TABULEIRO) // 2
POSICAO_TABULEIRO_Y = (ALTURA_TELA - ALTURA_TABULEIRO) // 2

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Meu Tetris")
pontos=0

tabuleiro = [[0 for coluna in range(10)] for linha in range(20)]


def desenhar_tabuleiro():
    for linha in range(20):
        for coluna in range(10):

            x = POSICAO_TABULEIRO_X + coluna * TAMANHO_BLOCO
            y = POSICAO_TABULEIRO_Y + linha * TAMANHO_BLOCO

            pygame.draw.rect(
                tela,
                (30, 30, 30),
                (x, y, TAMANHO_BLOCO, TAMANHO_BLOCO),
                1
            )
            if tabuleiro[linha][coluna] != 0:
                pygame.draw.rect(
                    tela,
                    (0, 0, 255),
                    (x + 1, y + 1,
                     TAMANHO_BLOCO - 2,
                     TAMANHO_BLOCO - 2)
                )
def verificar_eventos():
    global rodando

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
def verificar_linhas():
    linhas_completas = 0

    for linha in tabuleiro:
        if linha == [1] * 10:
            linhas_completas += 1

    return linhas_completas
def pontos():
    linhas_completas=verificar_linhas(linhas_completas)
    if linhas_completas==1:
        pontos+=100
    elif    

def cor():
    cores=[
        [(25,25,112)],
        [(245,0,0)],
        [(0,255,0)],
        [(0,255,255)],
        [(0,0,205)],
        [(255,255,0)],
        [(255,69,0)]
        ]
    cor=random.choice(cores)
    return cor
def pecas():
        pecas = [
        
        [[1, 1, 1, 1]],
        
        
        [[1, 1],
         [1, 1]],

        [
            [0, 1, 0],
            [1, 1, 1]
        ],

        # L
        [
            [1, 0],
            [1, 0],
            [1, 1]
        ],

        # Z
        [
            [1, 1, 0],
            [0, 1, 1]
        ]
        ]
        peca=random.choice(pecas)
        cor=cor()
        return peca,cor
def gerar_blocos():
    peca=pecas()
    cor=pecas()
    pygame.draw.rect(
        tela,
        cor,
        (x*(TAMANHO_BLOCO*4), y, TAMANHO_BLOCO, TAMANHO_BLOCO)
    )
rodando = True

##Rodar jogo
while rodando:

    verificar_eventos()

    tela.fill((0, 0, 0))

    desenhar_tabuleiro()

    pygame.display.update()
    
    tempo_anterior = 0
    velocidade = 500


pygame.quit()
