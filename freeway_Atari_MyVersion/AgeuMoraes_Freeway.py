
import pygame # Módulo para desenvolver jogos
import random # Módulo para aleatóriedade
import os # Módulo para operações do sistema


#Funções do programa
def caminho_arquivo(caminho_relativo_arquivo):
    # Caminho atual dos arquivos
    caminho_atual = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(caminho_atual, caminho_relativo_arquivo)

def upload_imagem(caminho_imagem):
    return pygame.image.load(caminho_imagem)
    
def dimensiona_imagem(imagem, dimensoes):
    return pygame.transform.scale(imagem, dimensoes)
    
def mensagem_tela_inicial(mensagem):
    return fonte.render(mensagem, True, (0, 0, 0), (255, 255, 255))
    
def coordenadas_na_tela_inicial(frase, coordenadas):
    tela_inicial.blit(frase, coordenadas)

def coordenadas_na_janela(imagem, coordenadas):
    return janela.blit(imagem, coordenadas)
    
def formata_quadrado(x_carro, soma_posicao):
    return pygame.draw.rect(janela, (0, 0, 0), (x_carro, y_carro + soma_posicao, 50, 30))

def formata_circulo(cor_rgb, posicao, tamanho):
    return pygame.draw.circle(janela, cor_rgb, posicao, tamanho)
    
def verifica_colisao(retangulo_carro, objeto_de_colisao):
    variavel_controle = False
    # Verifica a colisão entre o círculo de colisão e os retângulos dos carros
    if retangulo_carro.colliderect(objeto_de_colisao):
        variavel_controle = True
        # Aplicando o efeito sonoro
        efeito_sonoro_colisao.play()
        return variavel_controle
    
def posicao_galinha(x,y):
    return (x,y)

# Inicia o jogo
pygame.init()


# VARIÁVEIS DA TELA INCIAL
# Tela inicial do jogo
tela_inicial = pygame.display.set_mode((1300, 700))
tela_inicial_aberta = True
caminho_relativo_estrada_desfocada = caminho_arquivo('Recursos_Jogo/estradaJogoDesfocada.png')
imagem_estrada_desfocada = upload_imagem(caminho_relativo_estrada_desfocada)
imagem_inicial = dimensiona_imagem(imagem_estrada_desfocada, (1300, 700))

fonte = pygame.font.Font(None, 50)
mensagem_tela = "Olá, mundo!"
mensagem_tutorial1 = "Esse é um jogo multiplayer, cujo o objetivo é obter"
mensagem_tutorial2 = "o maior número de travessias dentro de 1 minuto"
mensagem_tutorial3 = "Pressione a tecla 'Enter' para iniciar o jogo!"
mensagem_tutorial4 = "Boa sorte! Que vença o melhor!!!"
cumprimento = mensagem_tela_inicial(mensagem_tela)
instrucao1 = mensagem_tela_inicial(mensagem_tutorial1)
instrucao2 = mensagem_tela_inicial(mensagem_tutorial2)
instrucao3 = mensagem_tela_inicial(mensagem_tutorial3)
instrucao4 = mensagem_tela_inicial(mensagem_tutorial4)

# VARIÁVEIS DO JOGO

# Caminho relativo dos arquivos
caminho_relativo_efeito_colisao = caminho_arquivo('Recursos_Jogo/oh-my-god-meme.mp3')
caminho_relativo_efeito_pontuacao = caminho_arquivo('Recursos_Jogo/cavalo-rodrigo-faro.mp3')
caminho_relativo_som_fundo = caminho_arquivo('Recursos_Jogo/que-isso-meu-filho-calma-vai-dar-namoro.mp3')
caminho_relativo_imagem_fundo = caminho_arquivo("Recursos_Jogo/estradaJogo.jpeg")
caminho_relativo_carro_esquerda = caminho_arquivo("Recursos_Jogo/carroJogoEsquerda.png")
caminho_relativo_carro_direita = caminho_arquivo("Recursos_Jogo/carroJogoDireita.png")
caminho_relativo_galinha_direita = caminho_arquivo("Recursos_Jogo/galinhaJogoViradaDireita.png")
caminho_relativo_galinha_esquerda = caminho_arquivo("Recursos_Jogo/galinhaJogoViradaEsquerda.png")

# Efeito sonoro
efeito_sonoro_colisao = pygame.mixer.Sound(caminho_relativo_efeito_colisao)
efeito_sonoro_pontuacao = pygame.mixer.Sound(caminho_relativo_efeito_pontuacao)
pygame.mixer.music.load(caminho_relativo_som_fundo)

# Dimensões de tela de jogo
largura = 1300
altura = 700

# Abre a janela pygame e dimensiona
janela = pygame.display.set_mode((largura, altura))

# Título da tela
pygame.display.set_caption("JOGO DA GALINHA (QUEM FAZ MAIS PONTOS DENTRO DE 1 MINUTO???)")

# Variável verdadeira
janela_aberta = True

# Buscando a imagem de fundo
imagem = upload_imagem(caminho_relativo_imagem_fundo)

# Redimensionando para ficar do tamanho da tela
imagem_fundo = dimensiona_imagem(imagem, (largura, altura))

# Trazendo as imagens dos carros
carro_pista1 = upload_imagem(caminho_relativo_carro_esquerda)
carro_tamanho1 = dimensiona_imagem(carro_pista1, (56.6, 33.1))

carro_pista2 = upload_imagem(caminho_relativo_carro_direita)
carro_tamanho2 = dimensiona_imagem(carro_pista2, (56.6, 33.1))

# Ponto inicial dos carros
ponto_inicial_direita = 1400
ponto_inicial_esquerda = -50

# Carros tendo as suas posições iniciais definidas
x_carro1, x_carro2, x_carro3 = ponto_inicial_esquerda, ponto_inicial_esquerda, ponto_inicial_esquerda
x_carro4, x_carro5, x_carro6= ponto_inicial_direita, ponto_inicial_direita, ponto_inicial_direita

y_carro = 233


# Trazendo a imagem da galinha para o python
galinha = upload_imagem(caminho_relativo_galinha_direita)
# Redimensionando a galinha
galinha_tamanho = dimensiona_imagem(galinha, (35.2, 42.52))
# Posicionando a galinha
galinha_x = 300
galinha_y = 450
# Variáevl que determina a velocidade de um objeto
velocidade_galinha = 5


# Trazendo a imagem da galinha para tela e redimensionando
outra_galinha_tamanho = dimensiona_imagem(galinha, (35.2, 42.52))
# Posicionando a galinha
outra_galinha_x = 940
outra_galinha_y = 450
# Variáevel que determina a velocidade de um objeto
velocidade_outra_galinha = 5

# Valores variáveis para definir a velocidade dos carros posteriormente
valores = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# Definindo as velocidades
velocidade_carro1 = random.choice(valores)
velocidade_carro2 = random.choice(valores)
velocidade_carro3 = random.choice(valores)
velocidade_carro4 = random.choice(valores)
velocidade_carro5 = random.choice(valores)
velocidade_carro6 = random.choice(valores)

# Contadores que posteriormente contarão as pontuações das galinhas 1 e 2
contador_galinha = 0
contador_outra_galinha = 0

# Contador de tempo
contador_tempo = 0

# Trazendo a imagem da galinha para o python
galinha_virada_direita = upload_imagem(caminho_relativo_galinha_direita)

# Trazendo a galinha virada para a direita
galinha_virada_esquerda = upload_imagem(caminho_relativo_galinha_esquerda)

# Galinha virada para a direita
galinha_vencedora_direita = galinha_virada_direita
# Galinha virada para a esquerda
galinha_vencedora_esquerda = galinha_virada_esquerda

tempo_total = 60
posicao_tempo_x = 1195
posicao_tempo_y = 38

# Tela incial do jogo sendo mantida aberta
while tela_inicial_aberta:
    pygame.time.delay(10)
    coordenadas_na_tela_inicial(imagem_inicial, (0, 0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            tela_inicial_aberta = False
            janela_aberta = False

    # identifica a tecla pressionada pelo usuário
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_RETURN] or comandos[pygame.K_KP_ENTER]:
        tela_inicial_aberta = False
    coordenadas_na_tela_inicial(cumprimento, (555, 150))
    coordenadas_na_tela_inicial(instrucao1, (250, 250))
    coordenadas_na_tela_inicial(instrucao2, (255, 300))
    coordenadas_na_tela_inicial(instrucao3, (300, 400))
    coordenadas_na_tela_inicial(instrucao4, (390, 500))
    pygame.display.update()

# Estrutura de repetição para mantêr a janela aberta
while janela_aberta:
    # Executa um delay de 30 mílisegundos
    pygame.time.delay(30)
    # Para cada evento que ocorre no pygame ele cria uma iteração de verificação
    for evento in pygame.event.get():
        # Condicional que verifica se a ação do usuario foi de fechar a janela
        if evento.type == pygame.QUIT:
            # Retorna falso para a variável e encerra o loop while
            janela_aberta = False

    # identifica a tecla pressionada pelo usuário
    comandos = pygame.key.get_pressed()
    # Condicionais para a locomoção de objetos através do teclado sendo atribuidas ao jogador 1
    if comandos[pygame.K_w] and galinha_y != 180:
        galinha_y -= velocidade_galinha
    if comandos[pygame.K_s] and galinha_y != 450:
        galinha_y += velocidade_galinha
    if comandos[pygame.K_a] and galinha_x != 0:
        galinha_x -= velocidade_galinha
    if comandos[pygame.K_d] and galinha_x != 1250:
        galinha_x += velocidade_galinha
    if comandos[pygame.K_w] and galinha_y == 180:
        # Posicionando a galinha no começo
        galinha_x, galinha_y = 300, 450
        # Contador que será utilizado para somar a pontuação do jogador
        contador_galinha += 1
        # Aplicando o efeito sonoro
        efeito_sonoro_pontuacao.play()

    # COndicionais para a locomoção de objetos através do teclado sendo atribuidas ao jogador 2
    if comandos[pygame.K_UP] and outra_galinha_y != 180:
        outra_galinha_y -= velocidade_outra_galinha
    if comandos[pygame.K_DOWN] and outra_galinha_y != 450:
        outra_galinha_y += velocidade_outra_galinha
    if comandos[pygame.K_LEFT] and outra_galinha_x != 0:
        outra_galinha_x -= velocidade_outra_galinha
    if comandos[pygame.K_RIGHT] and outra_galinha_x != 1250:
        outra_galinha_x += velocidade_outra_galinha
    if comandos[pygame.K_UP] and outra_galinha_y == 180:
        outra_galinha_x, outra_galinha_y = 940, 450
        # Contador que será utilizado para somar a pontuação do jogodor
        contador_outra_galinha += 1
        # Aplicando o efeito sonoro
        efeito_sonoro_pontuacao.play()

    # Contador de tempo para resetar o jogo(equivalente a 1 minuto)
    contador_tempo += 41.5
    if contador_tempo > 1000:
        contador_tempo = 0
        tempo_total -= 1

    # Condicional para resetar o jogo
    if tempo_total == -3:
        # Posicionando das galinhas no começo
        galinha_x, galinha_y = 300, 450
        outra_galinha_x, outra_galinha_y = 940, 450
        # Contadores serão resetados
        contador_galinha = 0
        contador_outra_galinha = 0
        tempo_total = 60
        pygame.display.update()

    # Movimentando os carros da esquerda para a direita
    x_carro1 += velocidade_carro1
    x_carro2 += velocidade_carro2
    x_carro3 += velocidade_carro3
    # Movimentando os carros da direita para a esquerda
    x_carro4 -= velocidade_carro4
    x_carro5 -= velocidade_carro5
    x_carro6 -= velocidade_carro6

    # Traz a imagem de fundo para a tela e posiciona ela nas coordenadas do canto superior esquerdo da tela
    coordenadas_na_janela(imagem_fundo, (0, 0))

    fonte = pygame.font.Font(None, 60)
    # Mensagem de vitória
    mensagem_vencedora = "GALINHA VENCEDORA!!!"
    # Formatação da mensagem
    mensagem_vencedora_formatada = fonte.render(mensagem_vencedora, True, (255, 255, 0), (76, 76, 76))

    # Condicionais que determinam as mensagens de vitória derrota ou empate
    if contador_galinha > contador_outra_galinha and tempo_total <= 0:
        # Posicionanado a mensagem de vitória na tela
        coordenadas_na_janela(mensagem_vencedora_formatada, (650, 260))
    if contador_outra_galinha > contador_galinha and tempo_total <= 0:
        # Posicionanado a mensagem de vitória na tela
        coordenadas_na_janela(mensagem_vencedora_formatada, (130, 260))
    if contador_galinha == contador_outra_galinha and tempo_total <= 0:
        # Determina o empate no jogo
        mensagem_empate = "EMPATE!!!"
        # Formata a mensagem
        mensagem_empate_formatada = fonte.render(mensagem_empate, True, (255, 255, 255), (0, 50, 0))
        # Posicionanado a mensagem de empate na tela
        coordenadas_na_janela(mensagem_empate_formatada, (550, 80))

    # Retângulos que ficam embaixo dos carros parar criar sombra(os valores inseridos na função é a soma da diferença de cada quadrado)
    retangulo_carro1 = formata_quadrado(x_carro1, 5)
    retangulo_carro2 = formata_quadrado(x_carro2, 41)
    retangulo_carro3 = formata_quadrado(x_carro3, 77)
    retangulo_carro4 = formata_quadrado(x_carro4, 139)
    retangulo_carro5 = formata_quadrado(x_carro5, 176)
    retangulo_carro6 = formata_quadrado(x_carro6, 209)

    # Colocando os carros no jogo
    carro1 = coordenadas_na_janela(carro_tamanho1, (x_carro1, y_carro))
    carro2 = coordenadas_na_janela(carro_tamanho1, (x_carro2, y_carro + 36))
    carro3 = coordenadas_na_janela(carro_tamanho1, (x_carro3, y_carro + 72))
    carro4 = coordenadas_na_janela(carro_tamanho2, (x_carro4, y_carro + 134))
    carro5 = coordenadas_na_janela(carro_tamanho2, (x_carro5, y_carro + 171))
    carro6 = coordenadas_na_janela(carro_tamanho2, (x_carro6, y_carro + 204))

    if contador_galinha > contador_outra_galinha and tempo_total <= 0:
        # Colocando a imagem grande da galinha vencedora na tela
        coordenadas_na_janela(galinha_vencedora_direita, (1, 181))
        # Posicionando a galinha
        outra_galinha_y = 1400
        galinha_y = 1400

    if contador_outra_galinha > contador_galinha and tempo_total <= 0:
        # Colocando a imagem grande da galinha vencedora na tela
        coordenadas_na_janela(galinha_vencedora_esquerda, (670, 181))
        # Posicionando a galinha
        outra_galinha_y = 1400
        galinha_y = 1400

    if contador_galinha == contador_outra_galinha and tempo_total <= 0:
        # Colocando a imagem grande da galinha vencedora na tela
        coordenadas_na_janela(galinha_vencedora_direita, (1, 181))
        # Colocando a imagem grande da galinha vencedora na tela
        coordenadas_na_janela(galinha_vencedora_esquerda, (670, 181))
        # Posicionando a galinha
        outra_galinha_y = 1400
        galinha_y = 1400

    # Transformando o número contado em string
    contador_em_string = str(contador_galinha)
    contador_em_string2 = str(contador_outra_galinha)

    fonte = pygame.font.Font(None, 100)
    # Escrevendo o número da pontuação da galinha 1
    pontuacao_galinha = contador_em_string
    # Dando a cor de fundo e letra
    texto_pontuacao_galinha = fonte.render(pontuacao_galinha, True, (255, 255, 255), (0, 50, 0))

    # Escrevendo o número da pontuação da galinha 2
    pontuacao_outra_galinha = str(contador_em_string2)
    # Dando a cor de fundo e letra
    texto_pontuacao_outra_galinha = fonte.render(pontuacao_outra_galinha, True, (255, 255, 255), (0, 50, 0))

    # Colocando o temporizador na tela e o círculo que fica atrás dele
    if tempo_total >= 0:
        # Círculo para colocar o tempo
        formata_circulo((0, 100, 0), (1235, 70), 60)
        tempo = str(tempo_total)
        tempo_na_tela = fonte.render(tempo, True, (255, 255, 255), (0, 100, 0))
        coordenadas_na_janela(tempo_na_tela, (posicao_tempo_x, posicao_tempo_y))

    # Ajustando a posição do temporizador, para quando ele sair de dezena para unidade, não ficar torto
    if tempo_total == 9:
        posicao_tempo_x += 0.8

    # Voltando o tempo para a sua posição original
    if tempo_total == -1:
        posicao_tempo_x -= 0.8

    # Rodando efeito sonoro
    if tempo_total == 1:
        pygame.mixer.music.play()

    # Mostrando a contabilização dos pontos da galinha 1 na tela em forma de mensagem
    coordenadas_na_janela(texto_pontuacao_galinha, (300, 50))

    # Mostrando a contabilização dos pontos da galinha 2 na tela em forma de mensagem
    coordenadas_na_janela(texto_pontuacao_outra_galinha, (940, 50))

    # Desenha o círculo nos pés da galinha
    sombra_galinha = formata_circulo((50, 50, 50), (posicao_galinha(galinha_x + 25, galinha_y + 40)), 10)
    # Mostrando a imagem da galinha na tela
    coordenadas_na_janela(galinha_tamanho, (posicao_galinha(galinha_x, galinha_y)))

    # Desenha o círculo nos pés da outra galinha
    sombra_outra_galinha = formata_circulo((50, 50, 50), (posicao_galinha(outra_galinha_x + 25, outra_galinha_y + 40)), 10)
    # Mostrando a imagem da outra galinha na tela
    coordenadas_na_janela(outra_galinha_tamanho, (posicao_galinha(outra_galinha_x, outra_galinha_y)))


    # Verifica a colisão entre o círculo de colisão da galinha e os retângulos dos carros
    if verifica_colisao(retangulo_carro1, sombra_galinha) or verifica_colisao(retangulo_carro2, sombra_galinha) or\
    verifica_colisao(retangulo_carro3, sombra_galinha) or verifica_colisao(retangulo_carro4, sombra_galinha) or\
    verifica_colisao(retangulo_carro5, sombra_galinha) or verifica_colisao(retangulo_carro6, sombra_galinha):
        # Posicionando a galinha no começo
        galinha_x, galinha_y = 300, 450

    # Outra Galinha
    # Verifica a colisão entre o círculo de colisão da outra galinha e os retângulos dos carros
    if verifica_colisao(retangulo_carro1, sombra_outra_galinha) or verifica_colisao(retangulo_carro2, sombra_outra_galinha) or\
    verifica_colisao(retangulo_carro3, sombra_outra_galinha) or verifica_colisao(retangulo_carro4, sombra_outra_galinha) or\
    verifica_colisao(retangulo_carro5, sombra_outra_galinha) or verifica_colisao(retangulo_carro6, sombra_outra_galinha):
        # Posicionando a galinha no começo
        outra_galinha_x, outra_galinha_y = 940, 450

    # Estruturas de repetição que definem o ponto final, aonde os carro deve voltar
    if x_carro1 >= 1400:
        x_carro1 = ponto_inicial_esquerda
        velocidade_carro1 = random.choice(valores)
    if x_carro2 >= 1400:
        x_carro2 = ponto_inicial_esquerda
        velocidade_carro2 = random.choice(valores)
    if x_carro3 >= 1400:
        x_carro3 = ponto_inicial_esquerda
        velocidade_carro3 = random.choice(valores)
    if x_carro4 <= -50:
        x_carro4 = ponto_inicial_direita
        velocidade_carro4 = random.choice(valores)
    if x_carro5 <= -50:
        x_carro5 = ponto_inicial_direita
        velocidade_carro5 = random.choice(valores)
    if x_carro6 <= -50:
        x_carro6 = ponto_inicial_direita
        velocidade_carro6 = random.choice(valores)

    # Atualiza a tela
    pygame.display.update()

# Sai do jogo
pygame.quit()
