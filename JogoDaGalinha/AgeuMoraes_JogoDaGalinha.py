# Módulo para desenvolver jogos
import pygame
# Módulo para aleatóriedade
import random
import os


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
    telaInicial.blit(frase, coordenadas)

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
        efeitoSonoroColisao.play()
        return variavel_controle
    
def posicao_galinha(x,y):
    return (x,y)

# Inicia o jogo
pygame.init()


# VARIÁVEIS DA TELA INCIAL
# Tela inicial do jogo
telaInicial = pygame.display.set_mode((1300, 700))
telaInicialAberta = True
caminhoRelativoEstradaDesfocada = caminho_arquivo('estradaJogoDesfocada.png')
imagemEstradaDesfocada = upload_imagem(caminhoRelativoEstradaDesfocada)
imagemInicial = dimensiona_imagem(imagemEstradaDesfocada, (1300, 700))

fonte = pygame.font.Font(None, 50)
mensagemTela = "Olá, mundo!"
mensagemTutorial1 = "Esse é um jogo multiplayer, cujo o objetivo é obter"
mensagemTutorial2 = "o maior número de travessias dentro de 1 minuto"
mensagemTutorial3 = "Pressione a tecla 'Enter' para iniciar o jogo!"
mensagemTutorial4 = "Boa sorte! Que vença o melhor!!!"
cumprimento = mensagem_tela_inicial(mensagemTela)
instrucao1 = mensagem_tela_inicial(mensagemTutorial1)
instrucao2 = mensagem_tela_inicial(mensagemTutorial2)
instrucao3 = mensagem_tela_inicial(mensagemTutorial3)
instrucao4 = mensagem_tela_inicial(mensagemTutorial4)

# VARIÁVEIS DO JOGO

# Caminho relativo dos arquivos
caminhoRelativoEfeitoColisao = caminho_arquivo('oh-my-god-meme.mp3')
caminhoRelativoEfeitoPontuacao = caminho_arquivo('cavalo-rodrigo-faro.mp3')
caminhoRelativoSomFundo = caminho_arquivo('que-isso-meu-filho-calma-vai-dar-namoro.mp3')
caminhoRelativoImagemFundo = caminho_arquivo("estradaJogo.jpeg")
caminhoRelativoCarroEsquerda = caminho_arquivo("carroJogoEsquerda.png")
caminhoRelativoCarroDireita = caminho_arquivo("carroJogoDireita.png")
caminhoRelativoGalinhaDireita = caminho_arquivo("galinhaJogoViradaDireita.png")
caminhoRelativoGalinhaEsquerda = caminho_arquivo("galinhaJogoViradaEsquerda.png")

# Efeito sonoro
efeitoSonoroColisao = pygame.mixer.Sound(caminhoRelativoEfeitoColisao)
# Efeito sonoro
efeitoSonoroPontuacao = pygame.mixer.Sound(caminhoRelativoEfeitoPontuacao)
# Efeito sonoro
pygame.mixer.music.load(caminhoRelativoSomFundo)

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
imagem = upload_imagem(caminhoRelativoImagemFundo)

# Redimensionando para ficar do tamanho da tela
imagem_fundo = dimensiona_imagem(imagem, (largura, altura))

# Trazendo as imagens dos carros
carroPista1 = upload_imagem(caminhoRelativoCarroEsquerda)
carroTamanho1 = dimensiona_imagem(carroPista1, (56.6, 33.1))

# Trazendo as imagens dos carros
carroPista2 = upload_imagem(caminhoRelativoCarroDireita)
carroTamanho2 = dimensiona_imagem(carroPista2, (56.6, 33.1))

# Ponto inicial dos carros
pontoInicialDireita = 1400
pontoInicialEsquerda = -50

# Carros tendo as suas posições iniciais definidas
x_carro1, x_carro2, x_carro3 = pontoInicialEsquerda, pontoInicialEsquerda, pontoInicialEsquerda
x_carro4, x_carro5, x_carro6= pontoInicialDireita, pontoInicialDireita, pontoInicialDireita

y_carro = 233


# Trazendo a imagem da galinha para o python
galinha = upload_imagem(caminhoRelativoGalinhaDireita)
# Redimensionando a galinha
galinhaTamanho = dimensiona_imagem(galinha, (35.2, 42.52))
# Posicionando a galinha
galinha_x = 300
galinha_y = 450
# Variáevl que determina a velocidade de um objeto
velocidadeGalinha = 5


# Trazendo a imagem da galinha para tela e redimensionando
outraGalinhaTamanho = dimensiona_imagem(galinha, (35.2, 42.52))
# Posicionando a galinha
outraGalinha_x = 940
outraGalinha_y = 450
# Variáevl que determina a velocidade de um objeto
velocidadeOutraGalinha = 5

# Valores variáveis para definir a velocidade dos carros posteriormente
valores = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# Definindo as velocidades
velocidadeCarro1 = random.choice(valores)
velocidadeCarro2 = random.choice(valores)
velocidadeCarro3 = random.choice(valores)
velocidadeCarro4 = random.choice(valores)
velocidadeCarro5 = random.choice(valores)
velocidadeCarro6 = random.choice(valores)

# Contador que posteriormente contará a pontuação galinha 1
contadorGalinha = 0
# Contador que posteriormente contará a pontuação galinha 2
contadorOutraGalinha = 0

# Contador de tempo
contadorTempo = 0

# Trazendo a imagem da galinha para o python
galinhaViradaDireita = upload_imagem(caminhoRelativoGalinhaDireita)

# Trazendo a galinha virada para a direita
galinhaViradaEsquerda = upload_imagem(caminhoRelativoGalinhaEsquerda)

# Galinha virada para a direita
galinhaVencedoraDireita = galinhaViradaDireita
# Galinha virada para a esquerda
galinhaVencedoraEsquerda = galinhaViradaEsquerda

tempoTotal = 60
posicaoTempoX = 1195
posicaoTempoY = 38

# Tela incial do jogo sendo mantida aberta
while telaInicialAberta:
    pygame.time.delay(10)
    coordenadas_na_tela_inicial(imagemInicial, (0, 0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            telaInicialAberta = False
            janela_aberta = False

    # identifica a tecla pressionada pelo usuário
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_RETURN] or comandos[pygame.K_KP_ENTER]:
        telaInicialAberta = False
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
        galinha_y -= velocidadeGalinha
    if comandos[pygame.K_s] and galinha_y != 450:
        galinha_y += velocidadeGalinha
    if comandos[pygame.K_a] and galinha_x != 0:
        galinha_x -= velocidadeGalinha
    if comandos[pygame.K_d] and galinha_x != 1250:
        galinha_x += velocidadeGalinha
    if comandos[pygame.K_w] and galinha_y == 180:
        # Posicionando a galinha no começo
        galinha_x, galinha_y = 300, 450
        # Contador que será utilizado para somar a pontuação do jogador
        contadorGalinha += 1
        # Aplicando o efeito sonoro
        efeitoSonoroPontuacao.play()

    # COndicionais para a locomoção de objetos através do teclado sendo atribuidas ao jogador 2
    if comandos[pygame.K_UP] and outraGalinha_y != 180:
        outraGalinha_y -= velocidadeOutraGalinha
    if comandos[pygame.K_DOWN] and outraGalinha_y != 450:
        outraGalinha_y += velocidadeOutraGalinha
    if comandos[pygame.K_LEFT] and outraGalinha_x != 0:
        outraGalinha_x -= velocidadeOutraGalinha
    if comandos[pygame.K_RIGHT] and outraGalinha_x != 1250:
        outraGalinha_x += velocidadeOutraGalinha
    if comandos[pygame.K_UP] and outraGalinha_y == 180:
        outraGalinha_x, outraGalinha_y = 940, 450
        # Contador que será utilizado para somar a pontuação do jogodor
        contadorOutraGalinha += 1
        # Aplicando o efeito sonoro
        efeitoSonoroPontuacao.play()

    # Contador de tempo para resetar o jogo(equivalente a 1 minuto)
    contadorTempo += 41.5
    if contadorTempo > 1000:
        contadorTempo = 0
        tempoTotal -= 1

    # Condicional para resetar o jogo
    if tempoTotal == -3:
        # Posicionando das galinhas no começo
        galinha_x, galinha_y = 300, 450
        outraGalinha_x, outraGalinha_y = 940, 450
        # Contadores serão resetados
        contadorGalinha = 0
        contadorOutraGalinha = 0
        tempoTotal = 60
        pygame.display.update()

    # Movimentando os carros da esquerda para a direita
    x_carro1 += velocidadeCarro1
    x_carro2 += velocidadeCarro2
    x_carro3 += velocidadeCarro3
    # Movimentando os carros da direita para a esquerda
    x_carro4 -= velocidadeCarro4
    x_carro5 -= velocidadeCarro5
    x_carro6 -= velocidadeCarro6

    # Traz a imagem de fundo para a tela e posiciona ela nas coordenadas do canto superior esquerdo da tela
    coordenadas_na_janela(imagem_fundo, (0, 0))

    fonte = pygame.font.Font(None, 60)
    # Mensagem de vitória
    mensagemVencedora = "GALINHA VENCEDORA!!!"
    # Formatação da mensagem
    mensagemVencedoraFormatada = fonte.render(mensagemVencedora, True, (255, 255, 0), (76, 76, 76))

    # Condicionais que determinam as mensagens de vitória derrota ou empate
    if contadorGalinha > contadorOutraGalinha and tempoTotal <= 0:
        # Posicionanado a mensagem de vitória na tela
        coordenadas_na_janela(mensagemVencedoraFormatada, (650, 260))
    if contadorOutraGalinha > contadorGalinha and tempoTotal <= 0:
        # Posicionanado a mensagem de vitória na tela
        coordenadas_na_janela(mensagemVencedoraFormatada, (130, 260))
    if contadorGalinha == contadorOutraGalinha and tempoTotal <= 0:
        # Determina o empate no jogo
        mensagemEmpate = "EMPATE!!!"
        # Formata a mensagem
        mensagemEmpateFormatada = fonte.render(mensagemEmpate, True, (255, 255, 255), (0, 50, 0))
        # Posicionanado a mensagem de empate na tela
        coordenadas_na_janela(mensagemEmpateFormatada, (550, 80))

    # Retângulos que ficam embaixo dos carros parar criar sombra(os valores inseridos na função é a soma da diferença de cada quadrado)
    retanguloCarro1 = formata_quadrado(x_carro1, 5)
    retanguloCarro2 = formata_quadrado(x_carro2, 41)
    retanguloCarro3 = formata_quadrado(x_carro3, 77)
    retanguloCarro4 = formata_quadrado(x_carro4, 139)
    retanguloCarro5 = formata_quadrado(x_carro5, 176)
    retanguloCarro6 = formata_quadrado(x_carro6, 209)

    # Colocando os carros no jogo
    carro1 = coordenadas_na_janela(carroTamanho1, (x_carro1, y_carro))
    carro2 = coordenadas_na_janela(carroTamanho1, (x_carro2, y_carro + 36))
    carro3 = coordenadas_na_janela(carroTamanho1, (x_carro3, y_carro + 72))
    carro4 = coordenadas_na_janela(carroTamanho2, (x_carro4, y_carro + 134))
    carro5 = coordenadas_na_janela(carroTamanho2, (x_carro5, y_carro + 171))
    carro6 = coordenadas_na_janela(carroTamanho2, (x_carro6, y_carro + 204))

    if contadorGalinha > contadorOutraGalinha and tempoTotal <= 0:
        # Colocando a imagem grande da galinha vencedora na tela
        coordenadas_na_janela(galinhaVencedoraDireita, (1, 181))
        # Posicionando a galinha
        outraGalinha_y = 1400
        galinha_y = 1400

    if contadorOutraGalinha > contadorGalinha and tempoTotal <= 0:
        # Colocando a imagem grande da galinha vencedora na tela
        coordenadas_na_janela(galinhaVencedoraEsquerda, (670, 181))
        # Posicionando a galinha
        outraGalinha_y = 1400
        galinha_y = 1400

    if contadorGalinha == contadorOutraGalinha and tempoTotal <= 0:
        # Colocando a imagem grande da galinha vencedora na tela
        coordenadas_na_janela(galinhaVencedoraDireita, (1, 181))
        # Colocando a imagem grande da galinha vencedora na tela
        coordenadas_na_janela(galinhaVencedoraEsquerda, (670, 181))
        # Posicionando a galinha
        outraGalinha_y = 1400
        galinha_y = 1400

    # Transformando o número contado em string
    contadorEmString = str(contadorGalinha)
    contadorEmString2 = str(contadorOutraGalinha)

    fonte = pygame.font.Font(None, 100)
    # Escrevendo o número da pontuação da galinha 1
    pontuacaoGalinha = contadorEmString
    # Dando a cor de fundo e letra
    textoPontuacaoGalinha = fonte.render(pontuacaoGalinha, True, (255, 255, 255), (0, 50, 0))

    # Escrevendo o número da pontuação da galinha 2
    pontuacaoOutraGalinha = str(contadorEmString2)
    # Dando a cor de fundo e letra
    textoPontuacaoOutraGalinha = fonte.render(pontuacaoOutraGalinha, True, (255, 255, 255), (0, 50, 0))

    # Colocando o temporizador na tela e o círculo que fica atrás dele
    if tempoTotal >= 0:
        # Círculo para colocar o tempo
        formata_circulo((0, 100, 0), (1235, 70), 60)
        tempo = str(tempoTotal)
        tempoNaTela = fonte.render(tempo, True, (255, 255, 255), (0, 100, 0))
        coordenadas_na_janela(tempoNaTela, (posicaoTempoX, posicaoTempoY))

    # Ajustando a posição do temporizador, para quando ele sair de dezena para unidade, não ficar torto
    if tempoTotal == 9:
        posicaoTempoX += 0.8

    # Voltando o tempo para a sua posição original
    if tempoTotal == -1:
        posicaoTempoX -= 0.8

    # Rodando efeito sonoro
    if tempoTotal == 1:
        pygame.mixer.music.play()

    # Mostrando a contabilização dos pontos da galinha 1 na tela em forma de mensagem
    coordenadas_na_janela(textoPontuacaoGalinha, (300, 50))

    # Mostrando a contabilização dos pontos da galinha 2 na tela em forma de mensagem
    coordenadas_na_janela(textoPontuacaoOutraGalinha, (940, 50))

    # Desenha o círculo nos pés da galinha
    sombraGalinha = formata_circulo((50, 50, 50), (posicao_galinha(galinha_x + 25, galinha_y + 40)), 10)
    # Mostrando a imagem da galinha na tela
    coordenadas_na_janela(galinhaTamanho, (posicao_galinha(galinha_x, galinha_y)))

    # Desenha o círculo nos pés da outra galinha
    sombraOutraGalinha = formata_circulo((50, 50, 50), (posicao_galinha(outraGalinha_x + 25, outraGalinha_y + 40)), 10)
    # Mostrando a imagem da outra galinha na tela
    coordenadas_na_janela(outraGalinhaTamanho, (posicao_galinha(outraGalinha_x, outraGalinha_y)))


    # Verifica a colisão entre o círculo de colisão da galinha e os retângulos dos carros
    if verifica_colisao(retanguloCarro1, sombraGalinha) or verifica_colisao(retanguloCarro2, sombraGalinha) or\
    verifica_colisao(retanguloCarro3, sombraGalinha) or verifica_colisao(retanguloCarro4, sombraGalinha) or\
    verifica_colisao(retanguloCarro5, sombraGalinha) or verifica_colisao(retanguloCarro6, sombraGalinha):
        # Posicionando a galinha no começo
        galinha_x, galinha_y = 300, 450

    # Outra Galinha
    # Verifica a colisão entre o círculo de colisão da outra galinha e os retângulos dos carros
    if verifica_colisao(retanguloCarro1, sombraOutraGalinha) or verifica_colisao(retanguloCarro2, sombraOutraGalinha) or\
    verifica_colisao(retanguloCarro3, sombraOutraGalinha) or verifica_colisao(retanguloCarro4, sombraOutraGalinha) or\
    verifica_colisao(retanguloCarro5, sombraOutraGalinha) or verifica_colisao(retanguloCarro6, sombraOutraGalinha):
        # Posicionando a galinha no começo
        outraGalinha_x, outraGalinha_y = 940, 450

    # Estruturas de repetição que definem o ponto final, aonde os carro deve voltar
    if x_carro1 >= 1400:
        x_carro1 = pontoInicialEsquerda
        velocidadeCarro1 = random.choice(valores)
    if x_carro2 >= 1400:
        x_carro2 = pontoInicialEsquerda
        velocidadeCarro2 = random.choice(valores)
    if x_carro3 >= 1400:
        x_carro3 = pontoInicialEsquerda
        velocidadeCarro3 = random.choice(valores)
    if x_carro4 <= -50:
        x_carro4 = pontoInicialDireita
        velocidadeCarro4 = random.choice(valores)
    if x_carro5 <= -50:
        x_carro5 = pontoInicialDireita
        velocidadeCarro5 = random.choice(valores)
    if x_carro6 <= -50:
        x_carro6 = pontoInicialDireita
        velocidadeCarro6 = random.choice(valores)

    # Atualiza a tela
    pygame.display.update()

# Sai do jogo
pygame.quit()
