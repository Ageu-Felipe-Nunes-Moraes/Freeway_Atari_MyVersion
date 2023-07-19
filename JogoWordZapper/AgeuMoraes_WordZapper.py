# Módulo para jogo
import os

import pygame
# Módulo para aleatoriedade
import random

# Inicia o pygame
pygame.init()

# Caminho atual dos arquivos
caminhoAtual = os.path.abspath(os.path.dirname(__file__))

# VARIÁVEIS PARA A TELA INICIAL
telaInicial = pygame.display.set_mode((1260, 700))
caminhoRelativoImagemInicial = os.path.join(caminhoAtual, "imagemFundoZapperDesfocada.png")
imagemInicial = pygame.image.load(caminhoRelativoImagemInicial)
imagemInicialJogo = pygame.transform.scale(imagemInicial, (1260, 700))
janelaInicialAberta = True

# VARIÁVEIS PARA O JOGO
# Todos os caminhos relativos dos arquivos do jogo
caminhoRelativoSomFundo = os.path.join(caminhoAtual, 'SomFudoParaJogo.mp3')
caminhoRelativoEfeitoTiro = os.path.join(caminhoAtual, 'efeitoSonoroTiroLazer.mp3')
caminhoRelativoColisao = os.path.join(caminhoAtual, 'colisãoSom.mp3')
caminhoRelativoImagemFundo = os.path.join(caminhoAtual, "imagemFundoZapper.png")
caminhoRelativoJogador = os.path.join(caminhoAtual, "jogadorZapper.png")
caminhoRelativoInimigo = os.path.join(caminhoAtual, "inimigoAsteristico.png")

pygame.mixer.music.load(caminhoRelativoSomFundo)
pygame.mixer.music.play(loops=-1)

efeitoSonoroTiro = pygame.mixer.Sound(caminhoRelativoEfeitoTiro)
efeitoSonoroColisaoInimiga = pygame.mixer.Sound(caminhoRelativoColisao)

# Dimensões de tela de jogo
larguraTela = 1260
alturaTela = 700

# AJusta o modo do tamanho da janela
janela = pygame.display.set_mode((larguraTela, alturaTela))

# Traz a imagem de fundo do jogo para dentro do python
imagemFundo = pygame.image.load(caminhoRelativoImagemFundo)
# Coloca a imagem como tela de fundo do jogo
imagemFundoJogo = pygame.transform.scale(imagemFundo, (larguraTela, alturaTela))

# Traz a imagem da nave do jogador para dentro do jogo
imagemJogador = pygame.image.load(caminhoRelativoJogador)

# Chamando a imagem inimiga em formato de asterisco, para a tela
inimigoAsteristico = pygame.image.load(caminhoRelativoInimigo)

# Variáveis que definem a posição da nave
jogadorPosicao_x = 380
jogadorPosicao_y = 460
# Variável para a velocidade
jogadorVelocidade = 25

# Nascimento inimigo à direita
posicaoInimigaDireita_x1 = 2500
posicaoInimigaDireita_x2 = 2500
posicaoInimigaDireita_x3 = 2500
posicaoInimigaDireita_x4 = 2500
posicaoInimigaDireita_x5 = 2500
posicaoInimigaDireita_x6 = 2500

# Nascimento inimigo à esquerda
posicaoInimigaEsquerda_x1 = -100
posicaoInimigaEsquerda_x2 = -100
posicaoInimigaEsquerda_x3 = -100
posicaoInimigaEsquerda_x4 = -100
posicaoInimigaEsquerda_x5 = -100
posicaoInimigaEsquerda_x6 = -100

inimigoPosicao_y = 450

# Velocidades disponíveis ao inimigo
velocidadesInimiga = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Escolha da velocidade de maneira aleatória
velocidadesInimigaEscolha1 = random.choice(velocidadesInimiga)
velocidadesInimigaEscolha2 = random.choice(velocidadesInimiga)
velocidadesInimigaEscolha3 = random.choice(velocidadesInimiga)
velocidadesInimigaEscolha4 = random.choice(velocidadesInimiga)
velocidadesInimigaEscolha5 = random.choice(velocidadesInimiga)
velocidadesInimigaEscolha6 = random.choice(velocidadesInimiga)
velocidadesInimigaEscolha7 = random.choice(velocidadesInimiga)
velocidadesInimigaEscolha8 = random.choice(velocidadesInimiga)
velocidadesInimigaEscolha9 = random.choice(velocidadesInimiga)
velocidadesInimigaEscolha10 = random.choice(velocidadesInimiga)
velocidadesInimigaEscolha11 = random.choice(velocidadesInimiga)
velocidadesInimigaEscolha12 = random.choice(velocidadesInimiga)

# Coloca o título do jogo
pygame.display.set_caption("Word Zapper")

# Variável de controle boleana verdadeira
janelaAberta = True

# Comprimento do lazer do jogador
lazerJogador_x = 28
lazerJogador_y = 465

# Posições x das letras
posicaoLetrasA_x, posicaoLetrasB_x, posicaoLetrasC_x, posicaoLetrasD_x = 1260, 1350, 1435, 1520
posicaoLetrasE_x, posicaoLetrasF_x, posicaoLetrasG_x, posicaoLetrasH_x = 1605, 1690, 1770, 1860
posicaoLetrasI_x, posicaoLetrasJ_x, posicaoLetrasK_x, posicaoLetrasL_x = 1944, 2005, 2085, 2175
posicaoLetrasM_x, posicaoLetrasN_x, posicaoLetrasO_x, posicaoLetrasP_x = 2255, 2357, 2447, 2535
posicaoLetrasQ_x, posicaoLetrasR_x, posicaoLetrasS_x, posicaoLetrasT_x = 2619, 2705, 2790, 2875
posicaoLetrasU_x, posicaoLetrasV_x, posicaoLetrasW_x, posicaoLetrasX_x = 2960, 3040, 3120, 3212
posicaoLetrasY_x, posicaoLetrasZ_x, posicaoCaractere_X = 3293, 3377, 3462

# Posição y das letras
posicaoLetrasA_y, posicaoLetrasB_y, posicaoLetrasC_y, posicaoLetrasD_y = 114, 114, 114, 114
posicaoLetrasE_y, posicaoLetrasF_y, posicaoLetrasG_y, posicaoLetrasH_y = 114, 114, 114, 114
posicaoLetrasI_y, posicaoLetrasJ_y, posicaoLetrasK_y, posicaoLetrasL_y = 114, 114, 114, 114
posicaoLetrasM_y, posicaoLetrasN_y, posicaoLetrasO_y, posicaoLetrasP_y = 114, 114, 114, 114
posicaoLetrasQ_y, posicaoLetrasR_y, posicaoLetrasS_y, posicaoLetrasT_y = 114, 114, 114, 114
posicaoLetrasU_y, posicaoLetrasV_y, posicaoLetrasW_y, posicaoLetrasX_y = 114, 114, 114, 114
posicaoLetrasY_y, posicaoLetrasZ_y, posicaoCaractere_y = 114, 114, 114

# Velocidades em que as letras se movimentão
velocidadeLetras = 10

# Coordenada onde as letras chegam antes de voltar para a coordenada inicial
coordenadaFinal = -1000
# VariáveL que irá resetar
resetar_x = 1260

# Determina a posição das interrogações
pos_interrogacao_X = 432
pos_interrogacao_y = 570
distanciaInterrogacoes = 70

# Tamanho padrão dos retângulos para os inimigos
rectInimigo_alt = 30
rectInimigo_larg = 32

# Posição e tamanho médio dos retângulos para cada letra
reduzPosX = 10
rectLargLetra = 49
rectAltLetra = 68.5

# Tempo total antes de começar e após começar o jogo
tempoTotal = 104
# Será usado como unidade de medida de conversão para minutos
contadorTempo = 0

# Esse "subTempo" é apenas um contador simbólico que irá ser usado dentro de uma condicional
subTempo = 0

# Contador de soma, variável de controle booleana e duração do tempo. Serão usados para a exibição de uma mensagem
tempoPerda = 0
exibirPerda = False
duracaoPerda = 1000

exibirGanho = False
contadorTempoGanho = 0

reiniciar = False

# Quantidade de tempo antes que a palavra que eu tenho que encontrar suma da tela e que o jogo seja resetado
tempoPausa = 3

# Lista vazia onde será armazenada o tempo do jogo quando uma certa condicional for executada
listaTempoParaPausa = []

# Lista vazia onde será armazenada o tempo do jogo quando uma certa condicional for executada
listaTempoParaErro = []

arquivoTxtRelativo = os.path.join(caminhoAtual, 'WordZapper.txt')

# 'Puxa' o arquivo txt com as palavras para o jogo
with open(arquivoTxtRelativo) as arquivo:
    todasPalavras = arquivo.readlines()

# Retira a quebra de linha das palavras
listaPalavras = [linha.rstrip() for linha in todasPalavras]

# Determinando o significado de cada variável
interrogacaoLetra1, interrogacaoLetra2, interrogacaoLetra3, interrogacaoLetra4 = '?', '?', '?', '?'
interrogacaoLetra5, interrogacaoLetra6 = '?', '?'

# Dicionário com todas as posições Y das letras
posicaoLetras_y = {
    'A': posicaoLetrasA_y,
    'B': posicaoLetrasB_y,
    'C': posicaoLetrasC_y,
    'D': posicaoLetrasD_y,
    'E': posicaoLetrasE_y,
    'F': posicaoLetrasF_y,
    'G': posicaoLetrasG_y,
    'H': posicaoLetrasH_y,
    'I': posicaoLetrasI_y,
    'J': posicaoLetrasJ_y,
    'K': posicaoLetrasK_y,
    'L': posicaoLetrasL_y,
    'M': posicaoLetrasM_y,
    'N': posicaoLetrasN_y,
    'O': posicaoLetrasO_y,
    'P': posicaoLetrasP_y,
    'Q': posicaoLetrasQ_y,
    'R': posicaoLetrasR_y,
    'S': posicaoLetrasS_y,
    'T': posicaoLetrasT_y,
    'U': posicaoLetrasU_y,
    'V': posicaoLetrasV_y,
    'W': posicaoLetrasW_y,
    'X': posicaoLetrasX_y,
    'Y': posicaoLetrasY_y,
    'Z': posicaoLetrasZ_y,
    '*': posicaoCaractere_y
}

# Pontuação do jogador
pontuacaoJogador = 0


# Some com as letras da tela, até completar o ciclo
def sumirLetras(letraDicionario, novaPosicao):

    global posicaoLetras_y
    posicaoLetras_y[letraDicionario] = novaPosicao


# Verifica as letras atingidas pelo lazer do jogador e coloca na tela se forem corretas
def verificacaoLetra(rectLetra, letra):
    # Traz uma variável de fora, para dentro da função através de uma "global"
    global interrogacaoLetra1, interrogacaoLetra2, interrogacaoLetra3, interrogacaoLetra4, interrogacaoLetra5, \
        interrogacaoLetra6, palavraSorteada, listaPalavraSorteada, pontuacaoJogador, formatacaoPerda, exibirPerda, \
        tempoPerda, perda, tempoTotal

    # Transforma a palavra sorteada em uma lista
    listaPalavraSorteada = list(palavraSorteada)

    # Condicionais que determinam a mudança das interrogações na tela para as letras da palavra sorteada
    if len(palavraSorteada) >= 1:

        # identifica colisão com o retângulo
        if rectLetra.colide_retangulo(disparoLazerJogador) and letra == palavraSorteada[0]:

            interrogacaoLetra1 = letra
            sumirLetras(letra, -1500)
            listaFormada1 = [interrogacaoLetra1]
            if tempoTotal < 95:
                tempoTotal += 5
            elif tempoTotal >= 95:
                tempoTotal = 99

    if len(palavraSorteada) >= 2:

        if rectLetra.colide_retangulo(disparoLazerJogador) and letra == palavraSorteada[1] and\
                interrogacaoLetra1 != "?":

            interrogacaoLetra2 = letra
            sumirLetras(letra, -1500)
            listaFormada2 = [interrogacaoLetra1, interrogacaoLetra2]
            if tempoTotal < 95:
                tempoTotal += 5
            elif tempoTotal >= 95:
                tempoTotal = 99

    if len(palavraSorteada) >= 3:

        if rectLetra.colide_retangulo(disparoLazerJogador) and letra == palavraSorteada[2] and\
                interrogacaoLetra2 != "?":

            interrogacaoLetra3 = letra
            sumirLetras(letra, -1500)
            listaFormada3 = [interrogacaoLetra1, interrogacaoLetra2, interrogacaoLetra3]
            if tempoTotal < 95:
                tempoTotal += 5
            elif tempoTotal >= 95:
                tempoTotal = 99

    if len(palavraSorteada) >= 4:

        if rectLetra.colide_retangulo(disparoLazerJogador) and letra == palavraSorteada[3] and\
                interrogacaoLetra3 != "?":

            interrogacaoLetra4 = letra
            sumirLetras(letra, -1500)
            listaFormada4 = [interrogacaoLetra1, interrogacaoLetra2, interrogacaoLetra3, interrogacaoLetra4]
            if tempoTotal < 95:
                tempoTotal += 5
            elif tempoTotal >= 95:
                tempoTotal = 99

    if len(palavraSorteada) >= 5:

        if rectLetra.colide_retangulo(disparoLazerJogador) and letra == palavraSorteada[4] and\
                interrogacaoLetra4 != "?":

            interrogacaoLetra5 = letra
            sumirLetras(letra, -1500)
            listaFormada5 = [interrogacaoLetra1, interrogacaoLetra2, interrogacaoLetra3, interrogacaoLetra4,
                             interrogacaoLetra5]

            if tempoTotal < 95:
                tempoTotal += 5
            elif tempoTotal >= 95:
                tempoTotal = 99

    if len(palavraSorteada) == 6:

        if rectLetra.colide_retangulo(disparoLazerJogador) and letra == palavraSorteada[5] and\
                interrogacaoLetra5 != "?":

            interrogacaoLetra6 = letra
            sumirLetras(letra, -1500)
            listaFormada6 = [interrogacaoLetra1, interrogacaoLetra2, interrogacaoLetra3, interrogacaoLetra4,
                             interrogacaoLetra5, interrogacaoLetra6]

            if tempoTotal < 95:
                tempoTotal += 5
            elif tempoTotal >= 95:
                tempoTotal = 99

    if rectLetra.colide_retangulo(disparoLazerJogador):
        sumirLetras(letra, -1500)
        if letra not in palavraSorteada:
            # Mostra a mensagem de perda de pontuação na tela
            perda = 15
            stringPerda = str(f" - {15} PONTOS")
            pontuacaoJogador -= perda
            fontePerdaPontos = pygame.font.Font(None, 70)
            formatacaoPerda = fontePerdaPontos.render(stringPerda, True, (255, 0, 0), (48, 15, 158, 255))
            exibirPerda = True
            if pontuacaoJogador < 0:
                pontuacaoJogador = 0
            # Obtém o tempo atual em milissegundos
            tempoPerda = pygame.time.get_ticks()


# Classe para criar inimigos
class Inimigo:
    def __init__(self, x, y):
        janela.blit(inimigoAsteristico, (x, y))


# Classe para criar retângulos
class Retangulo:
    def __init__(self, x, y, largura, altura):
        pygame.draw.rect(janela, (0, 0, 0), (x, y, largura, altura))


# Classe para criar retângulos que serão sobrepostos por personagens do jogo para capitar as colisões
class RetanguloColisao:
    def __init__(self, r, g, b, a, x, y, largura, altura):
        pygame.draw.rect(janela, (r, g, b, a), (x, y, largura, altura))
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

    # Função para verificar colisão entre retângulos
    def colide_retangulo(self, outro_retangulo):
        # Verifica a colisão entre as duas coordenadas horizontais e entre as duas coordenadas verticais
        if self.x < outro_retangulo.x + outro_retangulo.largura and \
                self.x + self.largura > outro_retangulo.x and \
                self.y < outro_retangulo.y + outro_retangulo.altura and \
                self.y + self.altura > outro_retangulo.y:
            efeitoSonoroColisaoInimiga.play()
            return True
        return False


# Classe para criar letras
class Letras:
    def __init__(self, letra):
        fonte = pygame.font.Font(None, 100)
        self.formatacao = fonte.render(letra, True, (235, 235, 234, 255), (48, 15, 158, 255,))

    # Função para posicionar letras criadas pela classe
    def posicaoLetra(self, x, y):
        janela.blit(self.formatacao, (x, y))


# Classe para criar interrogações com a mesma formatação e editar a posição delas
class Interrogacao:
    def __init__(self, letra):
        fonte = pygame.font.Font(None, 100)
        self.formatacao = fonte.render(letra, True, (182, 201, 96, 255), (0, 0, 0, 25))
        self.letra = letra

    def posicaoInterrogacao(self, x, y):
        janela.blit(self.formatacao, (x, y))


# Classe para criar letras
class Regras:
    def __init__(self, letra):
        fonte = pygame.font.Font(None, 30)
        self.formatacao = fonte.render(letra, True, (235, 235, 234, 255), (48, 15, 158, 255,))

    # Função para posicionar letras criadas pela classe
    def posicaoRegras(self, x, y):
        janela.blit(self.formatacao, (x, y))


# Estrutura de repetição controlada pela variável boleana
while janelaInicialAberta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            janelaInicialAberta = False
            janelaAberta = False

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_RETURN] or comandos[pygame.K_KP_ENTER]:
            janelaInicialAberta = False

    telaInicial.blit(imagemInicialJogo, (0, 0))
    # Cria a letra
    fonteTempo = pygame.font.Font(None, 100)
    formatacaoNomeJogo = fonteTempo.render('Como Jogar:', True, (118, 225, 115, 255), (48, 15, 158, 255))
    janela.blit(formatacaoNomeJogo, (420, 30))

    regra1 = Regras(" - Você precisa montar todas as palavras que aparecerem na tela")
    regra2 = Regras(" - As palavras devem ser montadas na ordem correta")
    regra3 = Regras(" - Elas surgem apenas por um curto período de tempo")
    regra4 = Regras(" - Desvie de todos os inimigos que emergem das laterais da tela")
    regra5 = Regras(" - Se houver um choque inimigo, você perderá alguns segundos")
    regra6 = Regras(" - Para toda letra acertada você ganha +5 segundos de tempo")
    regra7 = Regras(" - As teclas 'espaço'(atira) e 'setas'(Movimentam o jogador)")
    regra8 = Regras(" - Quando você montar a palavra envie ela atirando no '*'")
    regra9 = Regras(" - Monte o maior número de palavras, antes que o jogo acabe")
    regra10 = Regras(" - O jogo só acaba quando o temporizador chegar a zero")

    Regras.posicaoRegras(regra1, 300, 200)
    Regras.posicaoRegras(regra2, 300, 230)
    Regras.posicaoRegras(regra3, 300, 260)
    Regras.posicaoRegras(regra4, 300, 290)
    Regras.posicaoRegras(regra5, 300, 320)
    Regras.posicaoRegras(regra6, 300, 350)
    Regras.posicaoRegras(regra7, 300, 380)
    Regras.posicaoRegras(regra8, 300, 410)
    Regras.posicaoRegras(regra9, 300, 440)
    Regras.posicaoRegras(regra10, 300, 470)

    fonteInterrogacao = pygame.font.Font(None, 70)
    mensagemInstrucao = "Pressione a tecla 'Enter' para iniciar o jogo!"
    formatacaoInstrucao = fonteInterrogacao.render(mensagemInstrucao, True, (182, 201, 96, 255), (0, 0, 0, 25))
    telaInicial.blit(formatacaoInstrucao, (115, 600))

    pygame.display.update()


# Estrutura de repetição controlada pela variável boleana
while janelaAberta:
    # Executa delay de 30 mílisegundo
    delay = pygame.time.delay(30)

    # Para cada evento que ocorre no pygame ele cria uma iteração de verificação
    for evento in pygame.event.get():
        # Condicional que verifica se o tipo do evento é igual a sair do jogo
        if evento.type == pygame.QUIT:
            # Variável de controle boleana falsa que resulta no fim da iteração
            janelaAberta = False

    # Lê as teclas pressionadas pelo usuario
    comandos = pygame.key.get_pressed()

    if tempoTotal <= 102:
        # Condicionais que determinam o movimento da nave através do teclado
        if comandos[pygame.K_UP] and jogadorPosicao_y > 200:
            jogadorPosicao_y -= jogadorVelocidade
        if comandos[pygame.K_DOWN] and jogadorPosicao_y < 460:
            jogadorPosicao_y += jogadorVelocidade
        if comandos[pygame.K_LEFT] and jogadorPosicao_x > 220:
            jogadorPosicao_x -= jogadorVelocidade
        if comandos[pygame.K_RIGHT] and jogadorPosicao_x < 940:
            jogadorPosicao_x += jogadorVelocidade

    # Se tempo for igual a 104 ele vai escolher uma palavra
    if tempoTotal == 104:
        # Escolhe uma palavra aleatóriamente
        palavraEscolhida = random.choice(listaPalavras)
        palavraSorteada = palavraEscolhida.upper()
        pontuacaoJogador = 0
        perda = 0

    # Traz a imagem de fundo para a tela e posiciona ela nas coordenadas do canto superior esquerdo da tela
    janela.blit(imagemFundoJogo, (0, 0))

    # Condicional que verifica constantemente o tipo booleano da variável para ser executada
    if exibirPerda:  # Quando não tem nenhuma igualdade, a variável só é verificada se ela for verdadeira
        # Obtém o tempo atual em milissegundos
        tempoAtual = pygame.time.get_ticks()
        # Se a conta do tempo registrado anteriormente com o tempo atual for maior que o tempo de duração, executará
        if tempoAtual - tempoPerda >= duracaoPerda:
            exibirPerda = False  # Desativa a exibição da mensagem

        # Desenha a mensagem na tela
        janela.blit(formatacaoPerda, (450, 300))

    # Criando retângulo de colisão do jogador
    rectJogador = RetanguloColisao(48, 15, 158, 255, jogadorPosicao_x, jogadorPosicao_y, 96, 38)

    # Criando retângulo de colisão inimgo
    rectInimigoDireita1 = RetanguloColisao(
        48, 15, 158, 255, posicaoInimigaDireita_x1, inimigoPosicao_y, rectInimigo_alt, rectInimigo_larg)
    rectInimigoDireita2 = RetanguloColisao(
        48, 15, 158, 255, posicaoInimigaDireita_x2, inimigoPosicao_y - 50, rectInimigo_alt, rectInimigo_larg)
    rectInimigoDireita3 = RetanguloColisao(
        48, 15, 158, 255, posicaoInimigaDireita_x3, inimigoPosicao_y - 100, rectInimigo_alt, rectInimigo_larg)
    rectInimigoDireita4 = RetanguloColisao(
        48, 15, 158, 255, posicaoInimigaDireita_x4, inimigoPosicao_y - 150, rectInimigo_alt, rectInimigo_larg)
    rectInimigoDireita5 = RetanguloColisao(
        48, 15, 158, 255, posicaoInimigaDireita_x5, inimigoPosicao_y - 200, rectInimigo_alt, rectInimigo_larg)
    rectInimigoDireita6 = RetanguloColisao(
        48, 15, 158, 255, posicaoInimigaDireita_x6, inimigoPosicao_y - 250, rectInimigo_alt, rectInimigo_larg)

    rectInimigoEsquerda1 = RetanguloColisao(
        48, 15, 158, 255, posicaoInimigaEsquerda_x1, inimigoPosicao_y, rectInimigo_alt, rectInimigo_larg)
    rectInimigoEsquerda2 = RetanguloColisao(
        48, 15, 158, 255, posicaoInimigaEsquerda_x2, inimigoPosicao_y - 50, rectInimigo_alt, rectInimigo_larg)
    rectInimigoEsquerda3 = RetanguloColisao(
        48, 15, 158, 255, posicaoInimigaEsquerda_x3, inimigoPosicao_y - 100, rectInimigo_alt, rectInimigo_larg)
    rectInimigoEsquerda4 = RetanguloColisao(
        48, 15, 158, 255, posicaoInimigaEsquerda_x4, inimigoPosicao_y - 150, rectInimigo_alt, rectInimigo_larg)
    rectInimigoEsquerda5 = RetanguloColisao(
        48, 15, 158, 255, posicaoInimigaEsquerda_x5, inimigoPosicao_y - 200, rectInimigo_alt, rectInimigo_larg)
    rectInimigoEsquerda6 = RetanguloColisao(
        48, 15, 158, 255, posicaoInimigaEsquerda_x6, inimigoPosicao_y - 250, rectInimigo_alt, rectInimigo_larg)

    # Criando retângulo de colisão das letras
    rectLetraA = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasA_x - reduzPosX, posicaoLetras_y['A'], rectLargLetra, rectAltLetra)
    rectLetraB = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasB_x - reduzPosX, posicaoLetras_y['B'], rectLargLetra, rectAltLetra)
    rectLetraC = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasC_x - reduzPosX, posicaoLetras_y['C'], rectLargLetra, rectAltLetra)
    rectLetraD = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasD_x - reduzPosX, posicaoLetras_y['D'], rectLargLetra, rectAltLetra)
    rectLetraE = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasE_x - reduzPosX, posicaoLetras_y['E'], rectLargLetra - 4, rectAltLetra)
    rectLetraF = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasF_x - reduzPosX, posicaoLetras_y['F'], rectLargLetra - 7, rectAltLetra)
    rectLetraG = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasG_x - reduzPosX, posicaoLetras_y['G'], rectLargLetra + 4, rectAltLetra)
    rectLetraH = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasH_x - reduzPosX, posicaoLetras_y['H'], rectLargLetra, rectAltLetra)
    rectLetraI = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasI_x - reduzPosX, posicaoLetras_y['I'], rectLargLetra - 30, rectAltLetra)
    rectLetraJ = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasJ_x - reduzPosX, posicaoLetras_y['J'], rectLargLetra - 11, rectAltLetra)
    rectLetraK = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasK_x - reduzPosX, posicaoLetras_y['K'], rectLargLetra, rectAltLetra)
    rectLetraL = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasL_x - reduzPosX, posicaoLetras_y['L'], rectLargLetra - 7, rectAltLetra)
    rectLetraM = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasM_x - reduzPosX, posicaoLetras_y['M'], rectLargLetra + 8, rectAltLetra)
    rectLetraN = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasN_x - reduzPosX, posicaoLetras_y['N'], rectLargLetra, rectAltLetra)
    rectLetraO = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasO_x - reduzPosX, posicaoLetras_y['O'], rectLargLetra + 4, rectAltLetra)
    rectLetraP = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasP_x - reduzPosX, posicaoLetras_y['P'], rectLargLetra - 4, rectAltLetra)
    rectLetraQ = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasQ_x - reduzPosX, posicaoLetras_y['Q'], rectLargLetra + 4, rectAltLetra)
    rectLetraR = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasR_x - reduzPosX, posicaoLetras_y['R'], rectLargLetra, rectAltLetra)
    rectLetraS = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasS_x - reduzPosX, posicaoLetras_y['S'], rectLargLetra - 4, rectAltLetra)
    rectLetraT = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasT_x - reduzPosX, posicaoLetras_y['T'], rectLargLetra - 7, rectAltLetra)
    rectLetraU = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasU_x - reduzPosX, posicaoLetras_y['U'], rectLargLetra, rectAltLetra)
    rectLetraV = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasV_x - reduzPosX, posicaoLetras_y['V'], rectLargLetra - 4, rectAltLetra)
    rectLetraW = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasW_x - reduzPosX, posicaoLetras_y['W'], rectLargLetra + 15, rectAltLetra)
    rectLetraX = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasX_x - reduzPosX, posicaoLetras_y['X'], rectLargLetra - 4, rectAltLetra)
    rectLetraY = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasY_x - reduzPosX, posicaoLetras_y['Y'], rectLargLetra - 4, rectAltLetra)
    rectLetraZ = RetanguloColisao(
        48, 15, 158, 255, posicaoLetrasZ_x - reduzPosX, posicaoLetras_y['Z'], rectLargLetra - 7, rectAltLetra)
    rectCaractere = RetanguloColisao(
        48, 15, 158, 255, posicaoCaractere_X - reduzPosX, posicaoLetras_y['*'] + 2, rectLargLetra - 23, rectAltLetra)

    # Se o tempo for menor que 100 segundo ele executará o comando abaixo
    if tempoTotal < 100:
        # Se o jogador colidir com qualquer retângulo ele perderá 2 segundo do seu tempo; isso crescerá exponencialmente
        if rectJogador.colide_retangulo(rectInimigoDireita1) or rectJogador.colide_retangulo(rectInimigoDireita2) or \
                rectJogador.colide_retangulo(rectInimigoDireita3) or rectJogador.colide_retangulo(
              rectInimigoDireita4) or \
                rectJogador.colide_retangulo(rectInimigoDireita5) or rectJogador.colide_retangulo(
              rectInimigoDireita6) or \
                rectJogador.colide_retangulo(rectInimigoEsquerda1) or rectJogador.colide_retangulo(
              rectInimigoEsquerda2) or \
                rectJogador.colide_retangulo(rectInimigoEsquerda3) or rectJogador.colide_retangulo(
              rectInimigoEsquerda4) or \
                rectJogador.colide_retangulo(rectInimigoEsquerda5) or rectJogador.colide_retangulo(
              rectInimigoEsquerda6):
            tempoTotal -= 2

    # Unidade de medida para contar o tempo em segundos
    contadorTempo += 52.635
    # Condicional que simular um temporizador, subtraindo 1 segundo a cada 1000 de 'contadorTempo'
    if contadorTempo >= 1000:
        contadorTempo = 0
        tempoTotal -= 1

    # Transforma o 'tempoTotal' de inteiro para string
    tempoTotalString = str(tempoTotal)

    # Cria a letra
    fonteTempo = pygame.font.Font(None, 100)
    # Formata e escreve a mensagem
    formatacaoTempo = fonteTempo.render(tempoTotalString, True, (118, 225, 115, 255), (48, 15, 158, 255,))
    # Condicional que irá mostrar o tempo na tela apenas quando ele começar a contar valendo no jogo
    if tempoTotal <= 99:
        janela.blit(formatacaoTempo, (590, 30))

    # Condicional que irá mostrar por pouco tempo o nome do jogo na tela
    if tempoTotal > 102:
        formatacaoNomeJogo = fonteTempo.render('W  O  R  D', True, (118, 225, 115, 255), (48, 15, 158, 255))
        janela.blit(formatacaoNomeJogo, (470, 30))

        nomeJogo = Letras('Z  A  P  P  E  R')
        Letras.posicaoLetra(nomeJogo, 400, 114)

    # Condicional que irá resetar o jogador e todas as posições das letras do jogo
    if tempoTotal <= 0:
        tempoTotal = 108

        exibirGanho = False

        jogadorPosicao_x = 380
        jogadorPosicao_y = 460

        # Posições x das letras
        posicaoLetrasA_x, posicaoLetrasB_x, posicaoLetrasC_x, posicaoLetrasD_x = 1260, 1350, 1435, 1520
        posicaoLetrasE_x, posicaoLetrasF_x, posicaoLetrasG_x, posicaoLetrasH_x = 1605, 1690, 1770, 1860
        posicaoLetrasI_x, posicaoLetrasJ_x, posicaoLetrasK_x, posicaoLetrasL_x = 1944, 2005, 2085, 2175
        posicaoLetrasM_x, posicaoLetrasN_x, posicaoLetrasO_x, posicaoLetrasP_x = 2255, 2357, 2447, 2535
        posicaoLetrasQ_x, posicaoLetrasR_x, posicaoLetrasS_x, posicaoLetrasT_x = 2619, 2705, 2790, 2875
        posicaoLetrasU_x, posicaoLetrasV_x, posicaoLetrasW_x, posicaoLetrasX_x = 2960, 3040, 3120, 3212
        posicaoLetrasY_x, posicaoLetrasZ_x, posicaoCaractere_X = 3293, 3377, 3462

        posicaoLetras_y['A'] = 114
        posicaoLetras_y['B'] = 114
        posicaoLetras_y['C'] = 114
        posicaoLetras_y['D'] = 114
        posicaoLetras_y['E'] = 114
        posicaoLetras_y['F'] = 114
        posicaoLetras_y['G'] = 114
        posicaoLetras_y['H'] = 114
        posicaoLetras_y['I'] = 114
        posicaoLetras_y['J'] = 114
        posicaoLetras_y['K'] = 114
        posicaoLetras_y['L'] = 114
        posicaoLetras_y['M'] = 114
        posicaoLetras_y['N'] = 114
        posicaoLetras_y['O'] = 114
        posicaoLetras_y['P'] = 114
        posicaoLetras_y['Q'] = 114
        posicaoLetras_y['R'] = 114
        posicaoLetras_y['S'] = 114
        posicaoLetras_y['T'] = 114
        posicaoLetras_y['U'] = 114
        posicaoLetras_y['V'] = 114
        posicaoLetras_y['W'] = 114
        posicaoLetras_y['X'] = 114
        posicaoLetras_y['Y'] = 114
        posicaoLetras_y['Z'] = 114
        posicaoLetras_y['*'] = 114

    # Condicionais que fazem a letra voltar para o começo após utrapassar a coordenada demarcada
    if posicaoLetrasA_x < coordenadaFinal:
        posicaoLetrasA_x = resetar_x
        posicaoLetras_y['A'] = 114

    if posicaoLetrasB_x < coordenadaFinal:
        posicaoLetrasB_x = resetar_x
        posicaoLetras_y['B'] = 114

    if posicaoLetrasC_x < coordenadaFinal:
        posicaoLetrasC_x = resetar_x
        posicaoLetras_y['C'] = 114

    if posicaoLetrasD_x < coordenadaFinal:
        posicaoLetrasD_x = resetar_x
        posicaoLetras_y['D'] = 114

    if posicaoLetrasE_x < coordenadaFinal:
        posicaoLetrasE_x = resetar_x
        posicaoLetras_y['E'] = 114

    if posicaoLetrasF_x < coordenadaFinal:
        posicaoLetrasF_x = resetar_x
        posicaoLetras_y['F'] = 114

    if posicaoLetrasG_x < coordenadaFinal:
        posicaoLetrasG_x = resetar_x
        posicaoLetras_y['G'] = 114

    if posicaoLetrasH_x < coordenadaFinal:
        posicaoLetrasH_x = resetar_x
        posicaoLetras_y['H'] = 114

    if posicaoLetrasI_x < coordenadaFinal:
        posicaoLetrasI_x = resetar_x
        posicaoLetras_y['I'] = 114

    if posicaoLetrasJ_x < coordenadaFinal:
        posicaoLetrasJ_x = resetar_x
        posicaoLetras_y['J'] = 114

    if posicaoLetrasK_x < coordenadaFinal:
        posicaoLetrasK_x = resetar_x
        posicaoLetras_y['K'] = 114

    if posicaoLetrasL_x < coordenadaFinal:
        posicaoLetrasL_x = resetar_x
        posicaoLetras_y['L'] = 114

    if posicaoLetrasM_x < coordenadaFinal:
        posicaoLetrasM_x = resetar_x
        posicaoLetras_y['M'] = 114

    if posicaoLetrasN_x < coordenadaFinal:
        posicaoLetrasN_x = resetar_x
        posicaoLetras_y['N'] = 114

    if posicaoLetrasO_x < coordenadaFinal:
        posicaoLetrasO_x = resetar_x
        posicaoLetras_y['O'] = 114

    if posicaoLetrasP_x < coordenadaFinal:
        posicaoLetrasP_x = resetar_x
        posicaoLetras_y['P'] = 114

    if posicaoLetrasQ_x < coordenadaFinal:
        posicaoLetrasQ_x = resetar_x
        posicaoLetras_y['Q'] = 114

    if posicaoLetrasR_x < coordenadaFinal:
        posicaoLetrasR_x = resetar_x
        posicaoLetras_y['R'] = 114

    if posicaoLetrasS_x < coordenadaFinal:
        posicaoLetrasS_x = resetar_x
        posicaoLetras_y['S'] = 114

    if posicaoLetrasT_x < coordenadaFinal:
        posicaoLetrasT_x = resetar_x
        posicaoLetras_y['T'] = 114

    if posicaoLetrasU_x < coordenadaFinal:
        posicaoLetrasU_x = resetar_x
        posicaoLetras_y['U'] = 114

    if posicaoLetrasV_x < coordenadaFinal:
        posicaoLetrasV_x = resetar_x
        posicaoLetras_y['V'] = 114

    if posicaoLetrasW_x < coordenadaFinal:
        posicaoLetrasW_x = resetar_x
        posicaoLetras_y['W'] = 114

    if posicaoLetrasX_x < coordenadaFinal:
        posicaoLetrasX_x = resetar_x
        posicaoLetras_y['X'] = 114

    if posicaoLetrasY_x < coordenadaFinal:
        posicaoLetrasY_x = resetar_x
        posicaoLetras_y['Y'] = 114

    if posicaoLetrasZ_x < coordenadaFinal:
        posicaoLetrasZ_x = resetar_x
        posicaoLetras_y['Z'] = 114

    if posicaoCaractere_X < coordenadaFinal:
        posicaoCaractere_X = resetar_x
        posicaoLetras_y['*'] = 114

    # Aplicando a classe de Letra para criar as letras do alfabeto
    letraA, letraB, letraC, letraD = Letras('A'), Letras('B'), Letras('C'), Letras('D')
    letraE, letraF, letraG, letraH = Letras('E'), Letras('F'), Letras('G'), Letras('H')
    letraI, letraJ, letraK, letraL = Letras('I'), Letras('J'), Letras('K'), Letras('L')
    letraM, letraN, letraO, letraP = Letras('M'), Letras('N'), Letras('O'), Letras('P')
    letraQ, letraR, letraS, letraT = Letras('Q'), Letras('R'), Letras('S'), Letras('T')
    letraU, letraV, letraW, letraX = Letras('U'), Letras('V'), Letras('W'), Letras('X')
    letraY, letraZ, caractere = Letras('Y'), Letras('Z'), Letras('*')

    if tempoTotal <= 104:
        # Atribuindo velocidade igual nas letras
        posicaoLetrasA_x -= velocidadeLetras
        posicaoLetrasB_x -= velocidadeLetras
        posicaoLetrasC_x -= velocidadeLetras
        posicaoLetrasD_x -= velocidadeLetras
        posicaoLetrasE_x -= velocidadeLetras
        posicaoLetrasF_x -= velocidadeLetras
        posicaoLetrasG_x -= velocidadeLetras
        posicaoLetrasH_x -= velocidadeLetras
        posicaoLetrasI_x -= velocidadeLetras
        posicaoLetrasJ_x -= velocidadeLetras
        posicaoLetrasK_x -= velocidadeLetras
        posicaoLetrasL_x -= velocidadeLetras
        posicaoLetrasM_x -= velocidadeLetras
        posicaoLetrasN_x -= velocidadeLetras
        posicaoLetrasO_x -= velocidadeLetras
        posicaoLetrasP_x -= velocidadeLetras
        posicaoLetrasQ_x -= velocidadeLetras
        posicaoLetrasR_x -= velocidadeLetras
        posicaoLetrasS_x -= velocidadeLetras
        posicaoLetrasT_x -= velocidadeLetras
        posicaoLetrasU_x -= velocidadeLetras
        posicaoLetrasV_x -= velocidadeLetras
        posicaoLetrasW_x -= velocidadeLetras
        posicaoLetrasX_x -= velocidadeLetras
        posicaoLetrasY_x -= velocidadeLetras
        posicaoLetrasZ_x -= velocidadeLetras
        posicaoCaractere_X -= velocidadeLetras

    # Usando uma subfunção ou metódo para, posicionar as letras na tela
    Letras.posicaoLetra(letraA, posicaoLetrasA_x, posicaoLetras_y['A'])
    Letras.posicaoLetra(letraB, posicaoLetrasB_x, posicaoLetras_y['B'])
    Letras.posicaoLetra(letraC, posicaoLetrasC_x, posicaoLetras_y['C'])
    Letras.posicaoLetra(letraD, posicaoLetrasD_x, posicaoLetras_y['D'])
    Letras.posicaoLetra(letraE, posicaoLetrasE_x, posicaoLetras_y['E'])
    Letras.posicaoLetra(letraF, posicaoLetrasF_x, posicaoLetras_y['F'])
    Letras.posicaoLetra(letraG, posicaoLetrasG_x, posicaoLetras_y['G'])
    Letras.posicaoLetra(letraH, posicaoLetrasH_x, posicaoLetras_y['H'])
    Letras.posicaoLetra(letraI, posicaoLetrasI_x, posicaoLetras_y['I'])
    Letras.posicaoLetra(letraJ, posicaoLetrasJ_x, posicaoLetras_y['J'])
    Letras.posicaoLetra(letraK, posicaoLetrasK_x, posicaoLetras_y['K'])
    Letras.posicaoLetra(letraL, posicaoLetrasL_x, posicaoLetras_y['L'])
    Letras.posicaoLetra(letraM, posicaoLetrasM_x, posicaoLetras_y['M'])
    Letras.posicaoLetra(letraN, posicaoLetrasN_x, posicaoLetras_y['N'])
    Letras.posicaoLetra(letraO, posicaoLetrasO_x, posicaoLetras_y['O'])
    Letras.posicaoLetra(letraP, posicaoLetrasP_x, posicaoLetras_y['P'])
    Letras.posicaoLetra(letraQ, posicaoLetrasQ_x, posicaoLetras_y['Q'])
    Letras.posicaoLetra(letraR, posicaoLetrasR_x, posicaoLetras_y['R'])
    Letras.posicaoLetra(letraS, posicaoLetrasS_x, posicaoLetras_y['S'])
    Letras.posicaoLetra(letraT, posicaoLetrasT_x, posicaoLetras_y['T'])
    Letras.posicaoLetra(letraU, posicaoLetrasU_x, posicaoLetras_y['U'])
    Letras.posicaoLetra(letraV, posicaoLetrasV_x, posicaoLetras_y['V'])
    Letras.posicaoLetra(letraW, posicaoLetrasW_x, posicaoLetras_y['W'])
    Letras.posicaoLetra(letraX, posicaoLetrasX_x, posicaoLetras_y['X'])
    Letras.posicaoLetra(letraY, posicaoLetrasY_x, posicaoLetras_y['Y'])
    Letras.posicaoLetra(letraZ, posicaoLetrasZ_x, posicaoLetras_y['Z'])
    Letras.posicaoLetra(caractere, posicaoCaractere_X, posicaoLetras_y['*'] + 2)

    # Usando a classe Interrogações para criar variáveis com a quantidade de interrogações necessária
    interrogacao1, interrogacao2, interrogacao3, interrogacao4, interrogacao5, \
        interrogacao6 = Interrogacao(interrogacaoLetra1), Interrogacao(interrogacaoLetra2), \
        Interrogacao(interrogacaoLetra3), Interrogacao(interrogacaoLetra4), Interrogacao(interrogacaoLetra5), \
        Interrogacao(interrogacaoLetra6)

    # Posiciona as interrogações na tela
    Interrogacao.posicaoInterrogacao(interrogacao1, pos_interrogacao_X, pos_interrogacao_y)
    Interrogacao.posicaoInterrogacao(interrogacao2, pos_interrogacao_X + distanciaInterrogacoes, pos_interrogacao_y)
    Interrogacao.posicaoInterrogacao(interrogacao3, pos_interrogacao_X + distanciaInterrogacoes * 2, pos_interrogacao_y)
    Interrogacao.posicaoInterrogacao(interrogacao4, pos_interrogacao_X + distanciaInterrogacoes * 3, pos_interrogacao_y)
    Interrogacao.posicaoInterrogacao(interrogacao5, pos_interrogacao_X + distanciaInterrogacoes * 4, pos_interrogacao_y)
    Interrogacao.posicaoInterrogacao(interrogacao6, pos_interrogacao_X + distanciaInterrogacoes * 5, pos_interrogacao_y)

    # Só permite o inimigo aparecer na tela após a contagem do tempo começar a aparecer na tela
    if tempoTotal < 102:
        # Posiciona o inimigo na tela através de variáveis
        inimigoDireita1 = Inimigo(posicaoInimigaDireita_x1, inimigoPosicao_y)
        inimigoDireita2 = Inimigo(posicaoInimigaDireita_x2, inimigoPosicao_y - 50)
        inimigoDireita3 = Inimigo(posicaoInimigaDireita_x3, inimigoPosicao_y - 100)
        inimigoDireita4 = Inimigo(posicaoInimigaDireita_x4, inimigoPosicao_y - 150)
        inimigoDireita5 = Inimigo(posicaoInimigaDireita_x5, inimigoPosicao_y - 200)
        inimigoDireita6 = Inimigo(posicaoInimigaDireita_x6, inimigoPosicao_y - 250)

        # Posiciona o inimigo na tela através de variáveis
        inimigoEsquerda1 = Inimigo(posicaoInimigaEsquerda_x1, inimigoPosicao_y)
        inimigoEsquerda2 = Inimigo(posicaoInimigaEsquerda_x2, inimigoPosicao_y - 50)
        inimigoEsquerda3 = Inimigo(posicaoInimigaEsquerda_x3, inimigoPosicao_y - 100)
        inimigoEsquerda4 = Inimigo(posicaoInimigaEsquerda_x4, inimigoPosicao_y - 150)
        inimigoEsquerda5 = Inimigo(posicaoInimigaEsquerda_x5, inimigoPosicao_y - 200)
        inimigoEsquerda6 = Inimigo(posicaoInimigaEsquerda_x6, inimigoPosicao_y - 250)

        # Atribuindo velocidades diferentes para cada inimigo, indo e voltando
        posicaoInimigaDireita_x1 -= velocidadesInimigaEscolha1
        posicaoInimigaDireita_x2 -= velocidadesInimigaEscolha2
        posicaoInimigaDireita_x3 -= velocidadesInimigaEscolha3
        posicaoInimigaDireita_x4 -= velocidadesInimigaEscolha4
        posicaoInimigaDireita_x5 -= velocidadesInimigaEscolha5
        posicaoInimigaDireita_x6 -= velocidadesInimigaEscolha6

        posicaoInimigaEsquerda_x1 += velocidadesInimigaEscolha7
        posicaoInimigaEsquerda_x2 += velocidadesInimigaEscolha8
        posicaoInimigaEsquerda_x3 += velocidadesInimigaEscolha9
        posicaoInimigaEsquerda_x4 += velocidadesInimigaEscolha10
        posicaoInimigaEsquerda_x5 += velocidadesInimigaEscolha11
        posicaoInimigaEsquerda_x6 += velocidadesInimigaEscolha12

    # O inimigo da esquerda se movimentará para a direita, até que o da direita atinja -100 e ele então possa voltar
    if posicaoInimigaEsquerda_x1 > 1300:
        posicaoInimigaDireita_x1 = 1300
        velocidadesInimigaEscolha1 = random.choice(velocidadesInimiga)

    if posicaoInimigaEsquerda_x2 > 1300:
        posicaoInimigaDireita_x2 = 1300
        velocidadesInimigaEscolha2 = random.choice(velocidadesInimiga)

    if posicaoInimigaEsquerda_x3 > 1300:
        posicaoInimigaDireita_x3 = 1300
        velocidadesInimigaEscolha3 = random.choice(velocidadesInimiga)

    if posicaoInimigaEsquerda_x4 > 1300:
        posicaoInimigaDireita_x4 = 1300
        velocidadesInimigaEscolha4 = random.choice(velocidadesInimiga)

    if posicaoInimigaEsquerda_x5 > 1300:
        posicaoInimigaDireita_x5 = 1300
        velocidadesInimigaEscolha5 = random.choice(velocidadesInimiga)

    if posicaoInimigaEsquerda_x6 > 1300:
        posicaoInimigaDireita_x6 = 1300
        velocidadesInimigaEscolha6 = random.choice(velocidadesInimiga)

    # Em quanto o inimigo da direita tiver a posição maior que -100, o inimigo da esquerda se manterá na posição -100
    if posicaoInimigaDireita_x1 > -100:
        posicaoInimigaEsquerda_x1 = -100
        velocidadesInimigaEscolha7 = random.choice(velocidadesInimiga)

    if posicaoInimigaDireita_x2 > -100:
        posicaoInimigaEsquerda_x2 = -100
        velocidadesInimigaEscolha8 = random.choice(velocidadesInimiga)

    if posicaoInimigaDireita_x3 > -100:
        posicaoInimigaEsquerda_x3 = -100
        velocidadesInimigaEscolha9 = random.choice(velocidadesInimiga)

    if posicaoInimigaDireita_x4 > -100:
        posicaoInimigaEsquerda_x4 = -100
        velocidadesInimigaEscolha10 = random.choice(velocidadesInimiga)

    if posicaoInimigaDireita_x5 > -100:
        posicaoInimigaEsquerda_x5 = -100
        velocidadesInimigaEscolha11 = random.choice(velocidadesInimiga)

    if posicaoInimigaDireita_x6 > -100:
        posicaoInimigaEsquerda_x6 = -100
        velocidadesInimigaEscolha12 = random.choice(velocidadesInimiga)

    # Garante que não tenha nenhum erro com a escolha da palavra, e quando escolhe outra palavra, coloca a sobra exata
    # de interrogações
    if tempoTotal == 103 or tempoTotal == 102:
        if len(palavraSorteada) == 6:
            interrogacaoLetra1, interrogacaoLetra2, interrogacaoLetra3, interrogacaoLetra4, interrogacaoLetra5, \
                interrogacaoLetra6 = palavraSorteada[0], palavraSorteada[1], palavraSorteada[2], palavraSorteada[3], \
                palavraSorteada[4], palavraSorteada[5]

        elif len(palavraSorteada) == 5:
            interrogacaoLetra1, interrogacaoLetra2, interrogacaoLetra3, interrogacaoLetra4, \
                interrogacaoLetra5 = palavraSorteada[0], palavraSorteada[1], palavraSorteada[2], palavraSorteada[3], \
                palavraSorteada[4]
            interrogacaoLetra6 = '?'

        elif len(palavraSorteada) == 4:
            interrogacaoLetra1, interrogacaoLetra2, interrogacaoLetra3, interrogacaoLetra4 = palavraSorteada[0], \
                palavraSorteada[1], palavraSorteada[2], palavraSorteada[3]
            interrogacaoLetra6, interrogacaoLetra5 = '?', '?'

        elif len(palavraSorteada) == 3:
            interrogacaoLetra1, interrogacaoLetra2, interrogacaoLetra3 = palavraSorteada[0], palavraSorteada[1], \
                palavraSorteada[2]
            interrogacaoLetra6, interrogacaoLetra5, interrogacaoLetra4 = '?', '?', '?'

        elif len(palavraSorteada) == 2:
            interrogacaoLetra1, interrogacaoLetra2 = palavraSorteada[0], palavraSorteada[1]
            interrogacaoLetra6, interrogacaoLetra5, interrogacaoLetra4, interrogacaoLetra3 = '?', '?', '?', '?'

    # Faz a palavra "sumir" da tela
    elif tempoTotal == 101:
        interrogacaoLetra1, interrogacaoLetra2, interrogacaoLetra3, interrogacaoLetra4, interrogacaoLetra5, \
            interrogacaoLetra6 = '?', '?', '?', '?', '?', '?'

    # Verifica se o jogador acertou a letra correta
    else:
        if tempoTotal <= 102:
            # Tecla de disparo lazer
            if comandos[pygame.K_SPACE]:
                disparoLazerJogador = RetanguloColisao(
                    249, 255, 87, 255, jogadorPosicao_x + 34, jogadorPosicao_y - 460, lazerJogador_x, lazerJogador_y)

                efeitoSonoroTiro.play()

                verificacaoLetra(rectLetraA, "A")
                verificacaoLetra(rectLetraB, "B")
                verificacaoLetra(rectLetraC, "C")
                verificacaoLetra(rectLetraD, "D")
                verificacaoLetra(rectLetraE, "E")
                verificacaoLetra(rectLetraF, "F")
                verificacaoLetra(rectLetraG, "G")
                verificacaoLetra(rectLetraH, "H")
                verificacaoLetra(rectLetraI, "I")
                verificacaoLetra(rectLetraJ, "J")
                verificacaoLetra(rectLetraK, "K")
                verificacaoLetra(rectLetraL, "L")
                verificacaoLetra(rectLetraM, "M")
                verificacaoLetra(rectLetraN, "N")
                verificacaoLetra(rectLetraO, "O")
                verificacaoLetra(rectLetraP, "P")
                verificacaoLetra(rectLetraQ, "Q")
                verificacaoLetra(rectLetraR, "R")
                verificacaoLetra(rectLetraS, "S")
                verificacaoLetra(rectLetraT, "T")
                verificacaoLetra(rectLetraU, "U")
                verificacaoLetra(rectLetraV, "V")
                verificacaoLetra(rectLetraW, "W")
                verificacaoLetra(rectLetraX, "X")
                verificacaoLetra(rectLetraY, "Y")
                verificacaoLetra(rectLetraZ, "Z")

                # Se a pessoa pensa que terminou a palavra, ela pode enviar a mesma, como concluída, pelo asterisco
                if rectCaractere.colide_retangulo(disparoLazerJogador):

                    # Lista com todas as icógnitas e não icógnitas na tela
                    listaFormada6 = [interrogacaoLetra1, interrogacaoLetra2, interrogacaoLetra3, interrogacaoLetra4,
                                     interrogacaoLetra5, interrogacaoLetra6]

                    # Filtrador de interrogações
                    listaFormadaSemInterrogacoes = list(filter(lambda x: x != '?', listaFormada6))
                    # Junta as palavras
                    palavraFormada = "".join(listaFormadaSemInterrogacoes)

                    # Transforma todas as palavras da listaPalavras, para maiúsculas
                    listaPalavrasMaiusculas = [palavra.upper() for palavra in listaPalavras]

                    if palavraFormada in listaPalavrasMaiusculas:
                        exibirGanho = True

                    if palavraFormada not in listaPalavrasMaiusculas:
                        reiniciar = True

                    posicaoLetras_y['A'] = 114
                    posicaoLetras_y['B'] = 114
                    posicaoLetras_y['C'] = 114
                    posicaoLetras_y['D'] = 114
                    posicaoLetras_y['E'] = 114
                    posicaoLetras_y['F'] = 114
                    posicaoLetras_y['G'] = 114
                    posicaoLetras_y['H'] = 114
                    posicaoLetras_y['I'] = 114
                    posicaoLetras_y['J'] = 114
                    posicaoLetras_y['K'] = 114
                    posicaoLetras_y['L'] = 114
                    posicaoLetras_y['M'] = 114
                    posicaoLetras_y['N'] = 114
                    posicaoLetras_y['O'] = 114
                    posicaoLetras_y['P'] = 114
                    posicaoLetras_y['Q'] = 114
                    posicaoLetras_y['R'] = 114
                    posicaoLetras_y['S'] = 114
                    posicaoLetras_y['T'] = 114
                    posicaoLetras_y['U'] = 114
                    posicaoLetras_y['V'] = 114
                    posicaoLetras_y['W'] = 114
                    posicaoLetras_y['X'] = 114
                    posicaoLetras_y['Y'] = 114
                    posicaoLetras_y['Z'] = 114
                    posicaoLetras_y['*'] = 114

                    # O subTempo inicia em 0, por isso que ao rodar o código de hierarquia acima, obrigatoriamente o
                    # de baixo irá rodar
                    if subTempo == 0:
                        # Somando 1 ao subtempo para controlar quantas vezes esse código pode ser executado por vez
                        subTempo += 1
                        # Acrescenta o tempo atual de jogo dentro de uma lista vazia
                        listaTempoParaPausa.append(tempoTotal)

    if exibirGanho:

        # Lista com todas as icógnitas e não icógnitas na tela
        listaFormada6 = [interrogacaoLetra1, interrogacaoLetra2, interrogacaoLetra3, interrogacaoLetra4,
                            interrogacaoLetra5, interrogacaoLetra6]

        # Filtrador de interrogações
        listaFormadaSemInterrogacoes = list(filter(lambda x: x != '?', listaFormada6))
        # Junta as palavras
        palavraFormada = "".join(listaFormadaSemInterrogacoes)

        # Transforma todas as palavras da listaPalavras, para maiúsculas
        listaPalavrasMaiusculas = [palavra.upper() for palavra in listaPalavras]
        
        # Verifica se a palavra montada pertence a minha lista
        # Se sim, a mensagem de pontuação será apresentada
        if palavraFormada in listaPalavrasMaiusculas:
            contadorTempoGanho += 1
            # Mostra a mensagem de ganho de pontuação na tela
            ganho = 75
            stringGanho = (f'+ {ganho} PONTOS')
            fonteGanhoPontos = pygame.font.Font(None, 70)
            formatacaoGanho = fonteGanhoPontos.render(stringGanho, True, (0, 255, 0), (48, 15, 158, 255))
            janela.blit(formatacaoGanho, (450, 300))
            if contadorTempoGanho == 1:
                pontuacaoJogador += ganho

            if contadorTempoGanho == 2:
                reiniciar = True

            if contadorTempoGanho == 25:
                exibirGanho = False
                contadorTempoGanho = 0

    if reiniciar:
        # posicionamento do jogador
        jogadorPosicao_x = 380
        jogadorPosicao_y = 460

        # Posições x das letras
        posicaoLetrasA_x, posicaoLetrasB_x, posicaoLetrasC_x, posicaoLetrasD_x = 1260, 1350, 1435, 1520
        posicaoLetrasE_x, posicaoLetrasF_x, posicaoLetrasG_x, posicaoLetrasH_x = 1605, 1690, 1770, 1860
        posicaoLetrasI_x, posicaoLetrasJ_x, posicaoLetrasK_x, posicaoLetrasL_x = 1944, 2005, 2085, 2175
        posicaoLetrasM_x, posicaoLetrasN_x, posicaoLetrasO_x, posicaoLetrasP_x = 2255, 2357, 2447, 2535
        posicaoLetrasQ_x, posicaoLetrasR_x, posicaoLetrasS_x, posicaoLetrasT_x = 2619, 2705, 2790, 2875
        posicaoLetrasU_x, posicaoLetrasV_x, posicaoLetrasW_x, posicaoLetrasX_x = 2960, 3040, 3120, 3212
        posicaoLetrasY_x, posicaoLetrasZ_x, posicaoCaractere_X = 3293, 3377, 3462

        # Nascimento inimigo à direita
        posicaoInimigaDireita_x1 = 2500
        posicaoInimigaDireita_x2 = 2500
        posicaoInimigaDireita_x3 = 2500
        posicaoInimigaDireita_x4 = 2500
        posicaoInimigaDireita_x5 = 2500
        posicaoInimigaDireita_x6 = 2500

        # Nascimento inimigo à esquerda
        posicaoInimigaEsquerda_x1 = -100
        posicaoInimigaEsquerda_x2 = -100
        posicaoInimigaEsquerda_x3 = -100
        posicaoInimigaEsquerda_x4 = -100
        posicaoInimigaEsquerda_x5 = -100
        posicaoInimigaEsquerda_x6 = -100

        # Escolhe uma palavra aleatóriamente
        palavraEscolhida = random.choice(listaPalavras)
        palavraSorteada = palavraEscolhida.upper()

        # Garante que não tenha nenhum erro com a escolha da palavra, e quando escolhe outra palavra,
        # coloca a sobra exata de interrogações
        if len(palavraSorteada) == 6:
            interrogacaoLetra1, interrogacaoLetra2, interrogacaoLetra3, interrogacaoLetra4, \
                interrogacaoLetra5, interrogacaoLetra6 = palavraSorteada[0], palavraSorteada[1], \
                palavraSorteada[2], palavraSorteada[3], palavraSorteada[4], palavraSorteada[5]

        elif len(palavraSorteada) == 5:
            interrogacaoLetra1, interrogacaoLetra2, interrogacaoLetra3, interrogacaoLetra4, \
                interrogacaoLetra5 = palavraSorteada[0], palavraSorteada[1], palavraSorteada[2], \
                palavraSorteada[3], palavraSorteada[4]
            interrogacaoLetra6 = '?'

        elif len(palavraSorteada) == 4:
            interrogacaoLetra1, interrogacaoLetra2, interrogacaoLetra3, interrogacaoLetra4 = \
                palavraSorteada[0], palavraSorteada[1], palavraSorteada[2], palavraSorteada[3]
            interrogacaoLetra6, interrogacaoLetra5 = '?', '?'

        elif len(palavraSorteada) == 3:
            interrogacaoLetra1, interrogacaoLetra2, interrogacaoLetra3 = palavraSorteada[0], \
                palavraSorteada[1], palavraSorteada[2]
            interrogacaoLetra6, interrogacaoLetra5, interrogacaoLetra4 = '?', '?', '?'

        elif len(palavraSorteada) == 2:
            interrogacaoLetra1, interrogacaoLetra2 = palavraSorteada[0], palavraSorteada[1]
            interrogacaoLetra6, interrogacaoLetra5, interrogacaoLetra4, interrogacaoLetra3 = '?', '?', \
                '?', '?'
        reiniciar = False

    # Condicional que será executada apenas se a lista onde foi armazenada o tempo atual do jogo estiver diferente de
    # vazia
    if len(listaTempoParaPausa) != 0:
        # Esconde o tempo de verdade no fundo do tempo parado falso
        rectPausaTempo = pygame.draw.rect(janela, (48, 15, 158, 255,), (585, 25, 90, 80))

        # Transformando o tempo pausado em um texto
        tempoParadoString = str(listaTempoParaPausa[0])
        # Formata e escreve a mensagem
        formatacaoTempoParado = fonteTempo.render(tempoParadoString, True, (118, 225, 115, 255), (48, 15, 158, 255,))
        # Irá mostrar como se o tempo estivesse parado
        janela.blit(formatacaoTempoParado, (590, 30))

        # Reseta o subTempo
        subTempo = 0

        # Faz uma conta baseada no tempo do jogo armazenado na lista vazia subtraído pela quantidade de tempo que eu
        # quero de "pausa", que nesse caso, é dois
        calculoPausaTempo = listaTempoParaPausa[0] - tempoPausa

        # Se o tempo total do jogo for o mesmo da conta feita acima, ele reinicia as posições e ajusta as interrogações
        # para a aparecerem na tela no lugar da icógnita. Se o tempo Total for menor ou igual a 1, a condicional também
        # executará
        if tempoTotal == calculoPausaTempo or tempoTotal <= 1:
            tempoTotal = listaTempoParaPausa[0]

            # Limpando as listas, para quando a ação for repetida não ocorrerem erros
            listaTempoParaPausa.clear()
            listaPalavraSorteada.clear()

            # Transformando as letras em icógnitas para com interrogações
            interrogacaoLetra1, interrogacaoLetra2, interrogacaoLetra3, interrogacaoLetra4, interrogacaoLetra5, \
                interrogacaoLetra6 = '?', '?', '?', '?', '?', '?'

    # São os retângulos laterais 'invisíveis' pintados de preto de onde partirão os inimigos
    retanguloDireito = Retangulo(1058, 185, 202, 350)
    retanguloEsquerdo = Retangulo(0, 185, 204, 350)
    retanguloEsquerdoCima = Retangulo(0, 110, 370, 74)
    retanguloDireitoCima = Retangulo(891, 110, 370, 74)

    # Condicional que apresenta a pontuação final do jogador
    if tempoTotal > 104:
        fonteVitoria = pygame.font.Font(None, 65)
        pontuacaoJogadorString = str(f"PONTUAÇÃO TOTAL: {pontuacaoJogador}")
        formatacaoPontuacao = fonteVitoria.render(pontuacaoJogadorString, True, (182, 201, 96, 255),
                                                  (48, 15, 158, 255))
        janela.blit(formatacaoPontuacao, (378, 300))

    # Posiciona o jogador nas coordenadas das variáveis
    janela.blit(imagemJogador, (jogadorPosicao_x, jogadorPosicao_y))

    # Atualiza a tela períodicamente
    pygame.display.update()

pygame.mixer.music.stop()
# Saindo do jogo e finalizando o programa
pygame.quit()
