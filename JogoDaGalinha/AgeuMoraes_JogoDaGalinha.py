# Módulo para desenvolver jogos
import pygame
# Módulo para aleatóriedade
import random
import os

# Inicia o jogo
pygame.init()

# Caminho atual dos arquivos
caminhoAtual = os.path.abspath(os.path.dirname(__file__))

# VARIÁVEIS DA TELA INCIAL
# Tela inicial do jogo
telaInicial = pygame.display.set_mode((1300, 700))
telaInicialAberta = True
caminhoRelativoEstradaDesfocada = os.path.join(caminhoAtual, 'estradaJogoDesfocada.png')
imagemEstradaDesfocada = pygame.image.load(caminhoRelativoEstradaDesfocada)
imagemInicial = pygame.transform.scale(imagemEstradaDesfocada, (1300, 700))

fonte = pygame.font.Font(None, 50)
mensagemTela = "Olá, mundo!"
mensagemTutorial1 = "Esse é um jogo multiplayer, cujo o objetivo é obter"
mensagemTutorial2 = "o maior número de travessias dentro de 1 minuto"
mensagemTutorial3 = "Pressione a tecla 'Enter' para iniciar o jogo!"
mensagemTutorial4 = "Boa sorte! Que vença o melhor!!!"
cumprimento = fonte.render(mensagemTela, True, (0, 0, 0), (255, 255, 255))
instrucao1 = fonte.render(mensagemTutorial1, True, (0, 0, 0), (255, 255, 255))
instrucao2 = fonte.render(mensagemTutorial2, True, (0, 0, 0), (255, 255, 255))
instrucao3 = fonte.render(mensagemTutorial3, True, (0, 0, 0), (255, 255, 255))
instrucao4 = fonte.render(mensagemTutorial4, True, (0, 0, 0), (255, 255, 255))

# VARIÁVEIS DO JOGO

# Caminho relativo dos arquivos
caminhoRelativoEfeitoColisao = os.path.join(caminhoAtual, 'oh-my-god-meme.mp3')
caminhoRelativoEfeitoPontuacao = os.path.join(caminhoAtual, 'cavalo-rodrigo-faro.mp3')
caminhoRelativoSomFundo = os.path.join(caminhoAtual, 'que-isso-meu-filho-calma-vai-dar-namoro.mp3')
caminhoRelativoImagemFundo = os.path.join(caminhoAtual, "estradaJogo.jpeg")
caminhoRelativoCarroEsquerda = os.path.join(caminhoAtual, "carroJogoEsquerda.png")
caminhoRelativoCarroDireita = os.path.join(caminhoAtual, "carroJogoDireita.png")
caminhoRelativoGalinhaDireita = os.path.join(caminhoAtual, "galinhaJogoViradaDireita.png")
caminhoRelativoGalinhaEsquerda = os.path.join(caminhoAtual, "galinhaJogoViradaEsquerda.png")

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
imagem = pygame.image.load(caminhoRelativoImagemFundo)

# Redimensionando para ficar do tamanho da tela
imagem_fundo = pygame.transform.scale(imagem, (largura, altura))

# Trazendo as imagens dos carros
carroPista1 = pygame.image.load(caminhoRelativoCarroEsquerda)
carroTamanho1 = pygame.transform.scale(carroPista1, (56.6, 33.1))

# Trazendo as imagens dos carros
carroPista2 = pygame.image.load(caminhoRelativoCarroDireita)
carroTamanho2 = pygame.transform.scale(carroPista2, (56.6, 33.1))

# Ponto inicial dos carros
pontoInicialDireita = 1400
pontoInicialEsquerda = -50

# Carros tendo as suas posições iniciais definidas
x_carro1 = pontoInicialEsquerda
x_carro2 = pontoInicialEsquerda
x_carro3 = pontoInicialEsquerda
x_carro4 = pontoInicialDireita
x_carro5 = pontoInicialDireita
x_carro6 = pontoInicialDireita

y_carro = 233


# Trazendo a imagem da galinha para o python
galinha = pygame.image.load(caminhoRelativoGalinhaDireita)
# Redimensionando a galinha
galinhaTamanho = pygame.transform.scale(galinha, (35.2, 42.52))
# Posicionando a galinha
galinha_x = 300
galinha_y = 450
# Variáevl que determina a velocidade de um objeto
velocidadeGalinha = 5


# Trazendo a imagem da galinha para tela e redimensionando
outraGalinha = pygame.transform.scale(galinha, (35.2, 42.52))
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
galinhaViradaDireita = pygame.image.load(caminhoRelativoGalinhaDireita)

# Trazendo a galinha virada para a direita
galinhaViradaEsquerda = pygame.image.load(caminhoRelativoGalinhaEsquerda)

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
    telaInicial.blit(imagemInicial, (0, 0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            telaInicialAberta = False
            janela_aberta = False

    # identifica a tecla pressionada pelo usuário
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_RETURN] or comandos[pygame.K_KP_ENTER]:
        telaInicialAberta = False
    telaInicial.blit(cumprimento, (555, 150))
    telaInicial.blit(instrucao1, (250, 250))
    telaInicial.blit(instrucao2, (255, 300))
    telaInicial.blit(instrucao3, (300, 400))
    telaInicial.blit(instrucao4, (390, 500))
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
    janela.blit(imagem_fundo, (0, 0))

    # Tamanho da fonte 36
    fonte = pygame.font.Font(None, 60)
    # Mensagem de vitória
    mensagemVencedora = "GALINHA VENCEDORA!!!"
    # Formatação da mensagem
    mensagemVencedoraFormatada = fonte.render(mensagemVencedora, True, (255, 255, 0), (76, 76, 76))

    # Condicionais que determinam as mensagens de vitória derrota ou empate
    if contadorGalinha > contadorOutraGalinha and tempoTotal <= 0:
        # Posicionanado a mensagem de vitória na tela
        janela.blit(mensagemVencedoraFormatada, (650, 260))
    if contadorOutraGalinha > contadorGalinha and tempoTotal <= 0:
        # Posicionanado a mensagem de vitória na tela
        janela.blit(mensagemVencedoraFormatada, (130, 260))
    if contadorGalinha == contadorOutraGalinha and tempoTotal <= 0:
        # Determina o empate no jogo
        mensagemEmpate = "EMPATE!!!"
        # Formata a mensagem
        mensagemEmpateFormatada = fonte.render(mensagemEmpate, True, (255, 255, 255), (0, 50, 0))
        # Posicionanado a mensagem de empate na tela
        janela.blit(mensagemEmpateFormatada, (550, 80))

    # Retângulos que ficam embaixo dos carros parar criar sombra
    retanguloCarro1 = pygame.draw.rect(janela, (0, 0, 0), (x_carro1, y_carro + 5, 50, 30))
    retanguloCarro2 = pygame.draw.rect(janela, (0, 0, 0), (x_carro2, y_carro + 41, 50, 30))
    retanguloCarro3 = pygame.draw.rect(janela, (0, 0, 0), (x_carro3, y_carro + 77, 50, 30))
    retanguloCarro4 = pygame.draw.rect(janela, (0, 0, 0), (x_carro4, y_carro + 139, 50, 30))
    retanguloCarro5 = pygame.draw.rect(janela, (0, 0, 0), (x_carro5, y_carro + 176, 50, 30))
    retanguloCarro6 = pygame.draw.rect(janela, (0, 0, 0), (x_carro6, y_carro + 209, 50, 30))

    # Colocando os carros no jogo
    carro1 = janela.blit(carroTamanho1, (x_carro1, y_carro))
    carro2 = janela.blit(carroTamanho1, (x_carro2, y_carro + 36))
    carro3 = janela.blit(carroTamanho1, (x_carro3, y_carro + 72))
    carro4 = janela.blit(carroTamanho2, (x_carro4, y_carro + 134))
    carro5 = janela.blit(carroTamanho2, (x_carro5, y_carro + 171))
    carro6 = janela.blit(carroTamanho2, (x_carro6, y_carro + 204))

    if contadorGalinha > contadorOutraGalinha and tempoTotal <= 0:
        # Colocando a imagem grande da galinha vencedora na tela
        janela.blit(galinhaVencedoraDireita, (1, 181))
        # Posicionando a galinha
        outraGalinha_y = 1400
        galinha_y = 1400

    if contadorOutraGalinha > contadorGalinha and tempoTotal <= 0:
        # Colocando a imagem grande da galinha vencedora na tela
        janela.blit(galinhaVencedoraEsquerda, (670, 181))
        # Posicionando a galinha
        outraGalinha_y = 1400
        galinha_y = 1400

    if contadorGalinha == contadorOutraGalinha and tempoTotal <= 0:
        # Colocando a imagem grande da galinha vencedora na tela
        janela.blit(galinhaVencedoraDireita, (1, 181))
        # Colocando a imagem grande da galinha vencedora na tela
        janela.blit(galinhaVencedoraEsquerda, (670, 181))
        # Posicionando a galinha
        outraGalinha_y = 1400
        galinha_y = 1400

    # Transformando o número contado em string
    contadorEmString = str(contadorGalinha)
    contadorEmString2 = str(contadorOutraGalinha)

    # tamanho da fonte 36
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
        pygame.draw.circle(janela, (0, 100, 0), (1235, 70), 60)
        tempo = str(tempoTotal)
        tempoNaTela = fonte.render(tempo, True, (255, 255, 255), (0, 100, 0))
        janela.blit(tempoNaTela, (posicaoTempoX, posicaoTempoY))

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
    janela.blit(textoPontuacaoGalinha, (300, 50))

    # Mostrando a contabilização dos pontos da galinha 2 na tela em forma de mensagem
    janela.blit(textoPontuacaoOutraGalinha, (940, 50))

    # Desenha o círculo nos pés da galinha
    sombraGalinha = pygame.draw.circle(janela, (50, 50, 50), (galinha_x + 25, galinha_y + 40), 10)
    # Mostrando a imagem da galinha na tela
    janela.blit(galinhaTamanho, (galinha_x, galinha_y))

    # Desenha o círculo nos pés da outra galinha
    sombraOutraGalinha = pygame.draw.circle(janela, (50, 50, 50), (outraGalinha_x + 25, outraGalinha_y + 40), 10)
    # Mostrando a imagem da outra galinha na tela
    janela.blit(outraGalinha, (outraGalinha_x, outraGalinha_y))

    # Verifica a colisão entre o círculo de colisão e os retângulos dos carros
    if retanguloCarro1.colliderect(sombraGalinha):
        # Posicionando a galinha no começo
        galinha_x, galinha_y = 300, 450
        # Aplicando o efeito sonoro
        efeitoSonoroColisao.play()

    # Verifica a colisão entre o círculo de colisão e os retângulos dos carros
    if retanguloCarro2.colliderect(sombraGalinha):
        # Posicionando a galinha no começo
        galinha_x, galinha_y = 300, 450
        # Aplicando o efeito sonoro
        efeitoSonoroColisao.play()

    # Verifica a colisão entre o círculo de colisão e os retângulos dos carros
    if retanguloCarro3.colliderect(sombraGalinha):
        # Posicionando a galinha no começo
        galinha_x, galinha_y = 300, 450
        efeitoSonoroColisao.play()

    # Verifica a colisão entre o círculo de colisão e os retângulos dos carros
    if retanguloCarro4.colliderect(sombraGalinha):
        # Posicionando a galinha no começo
        galinha_x, galinha_y = 300, 450
        # Aplicando o efeito sonoro
        efeitoSonoroColisao.play()

    # Verifica a colisão entre o círculo de colisão e os retângulos dos carros
    if retanguloCarro5.colliderect(sombraGalinha):
        # Posicionando a galinha no começo
        galinha_x, galinha_y = 300, 450
        # Aplicando o efeito sonoro
        efeitoSonoroColisao.play()

    # Verifica a colisão entre o círculo de colisão e os retângulos dos carros
    if retanguloCarro6.colliderect(sombraGalinha):
        # Posicionando a galinha no começo
        galinha_x, galinha_y = 300, 450
        # Aplicando o efeito sonoro
        efeitoSonoroColisao.play()

    # Outra Galinha
    # Verifica a colisão entre o círculo de colisão e os retângulos dos carros
    if retanguloCarro1.colliderect(sombraOutraGalinha):
        # Posicionando a galinha 2 no começo
        outraGalinha_x, outraGalinha_y = 940, 450
        # Aplicando o efeito sonoro
        efeitoSonoroColisao.play()

    # Verifica a colisão entre o círculo de colisão e os retângulos dos carros
    if retanguloCarro2.colliderect(sombraOutraGalinha):
        # Posicionando a galinha 2 no começo
        outraGalinha_x, outraGalinha_y = 940, 450
        # Aplicando o efeito sonoro
        efeitoSonoroColisao.play()

    # Verifica a colisão entre o círculo de colisão e os retângulos dos carros
    if retanguloCarro3.colliderect(sombraOutraGalinha):
        # Posicionando a galinha 2 no começo
        outraGalinha_x, outraGalinha_y = 940, 450
        # Aplicando o efeito sonoro
        efeitoSonoroColisao.play()

    # Verifica a colisão entre o c
    # írculo de colisão e os retângulos dos carros
    if retanguloCarro4.colliderect(sombraOutraGalinha):
        # Posicionando a galinha 2 no começo
        outraGalinha_x, outraGalinha_y = 940, 450
        # Aplicando o efeito sonoro
        efeitoSonoroColisao.play()

    # Verifica a colisão entre o círculo de colisão e os retângulos dos carros
    if retanguloCarro5.colliderect(sombraOutraGalinha):
        # Posicionando a galinha 2 no começo
        outraGalinha_x, outraGalinha_y = 940, 450
        # Aplicando o efeito sonoro
        efeitoSonoroColisao.play()

    # Verifica a colisão entre o círculo de colisão e os retângulos dos carros
    if retanguloCarro6.colliderect(sombraOutraGalinha):
        # Posicionando a galinha 2 no começo
        outraGalinha_x, outraGalinha_y = 940, 450
        # Aplicando o efeito sonoro
        efeitoSonoroColisao.play()

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
