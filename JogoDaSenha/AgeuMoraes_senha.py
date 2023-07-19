import tkinter as tk # Importa a biblioteca gráfica Tkinter
import random # Importa a biblioteca random
import os # Módulo que reinicia o programa do zero
import sys # Módulo que reincia o programa do zero


# Cria a tela
tela = tk.Tk()

tela.geometry("1300x700")

# Traz o atributo da tela acima de outras telas como verdade
tela.attributes("-topmost", True)

# Configura a tela para branca
tela.configure(bg="white")

def mostrarTriunfo():
    parabens = tk.Label(tela, text="PARABÉNS VOCÊ VENCEEU!!!", bg="white", fg="green", font=("Times_New_Roman", 16))
    parabens.place(x = 920, y = 150)


def mostrarDerrota():
    derrota = tk.Label(tela, text="VOCÊ PERDEU!!", bg="white", fg="red", font=("Times_New_Roman", 16))
    derrota.place(x = 984, y = 150)


# Função para fechar tela
def fecharTela(event):
    # Comando que desliga a tela
    tela.destroy()


# Função para reiniciar o jogo utilizando módulos
def reiniciar(event=None):

    python = sys.executable
    os.execl(python, python, *sys.argv)


# Função para criar o botão de reiniciar
def criarBotaoReiniciar():
    
    # Cria botão de Reiniciar
    botaoReiniciar = tk.Button(tela, text="Reiniciar", command=lambda:[reiniciar()], bg = "blue", fg = "white")

    # Aplica as coordenadas do botão
    botaoReiniciar.place(x = 1030, y = 330)


#Função para mover o canvasJogo para a direita
def moverDireita():


    def desabilitarBotao():
        botaoRoxo.config(state="disable")
        botaoAzul.config(state="disable")
        botaoVerde.config(state="disable")
        botaoAmarelo.config(state="disable")
        botaoVermelho.config(state="disable")
        botaoMarrom.config(state="disable")

    # Mover o retângulo de 50 em 50 pixels para a direita 
    canvasJogo.move(retangulo, 50, 0)

    # Verificar se o retângulo alcançou a coordenada (400, 50)
    if canvasJogo.coords(retangulo)[0] < 500:
        
        # Agenda a chamada da função novamente após 100ms
        canvasJogo.after(150, moverDireita)

    # É executada se a primeira condicional não for satisfeita
    else:

        # Lista de cores
        listaCores = ["blue", "purple", "brown", "green", "red", "orange"]
        # Embaralha as cores
        random.shuffle(listaCores)
        # Seleciona quatro cores da lista e cria uma nova
        sorteada = random.sample(listaCores, 4)
        # Teste que mostra a primeira cor da nova lista
        print(sorteada[1])

        # Contador
        s = 0

        # Contador
        r = 0

        # Estrutura de repetição para a criação das bolas que foram selecionadas aleatóriamente
        for resultado in range(0, 4):  

            # Cria o fundo do canvas que fica atrás da bola
            respostaCerta = tk.Canvas(tela, width=42, height=42, highlightthickness=0)
            # Cria a bola
            respostaCerta.create_oval(0, 0, 40, 40, fill=sorteada[0 + s], outline="black")
            # Configura o canvas para branco
            respostaCerta.configure(bg="white")
            # posiciona a bola na tela
            respostaCerta.place(x = 920 + r, y = 250)

            # Soma 1 ao contador
            s += 1
            
            # Soma 90 ao contador 
            r += 90


        esconder = tk.Canvas(tela, width=320, height=60, highlightthickness=0)
        esconder.configure(bg="white")
        esconder.place(x = 920, y = 245)


        # Cria o canvas por trás da faixa cinza
        canvaFaixa = tk.Canvas(tela, width=64.2, height=460)
        # Cria o retangulo cinza na tela
        canvaFaixa.create_rectangle(0, 0, 64.8, 462, fill="grey", outline="white", width=10)
        # Configura o canvas para cinza
        canvaFaixa.configure(bg="grey")
        # Posiciona o retangulo na tela
        canvaFaixa.place(x=538, y=90)

        # Contador
        n = 0

        # Estrutura de repetição para criar as linhas que dividem as fases do jogo
        for linhasSeparadas in range(0,9):
            
            # Soma 79 ao contador
            n += 47.4

            # Cria o canvas por trás da linha
            canvasLinhas = tk.Canvas(tela, width=289.2, height=6, highlightthickness=0)
            # Mostra o canvas na tela

            # Cria a linha na tela
            canvasLinhas.create_line(0, 3, 600, 3, fill="white", width=3)
            # Configura o canvas para preto
            canvasLinhas.configure(bg="black")
            # Posiciona a linha na tela
            canvasLinhas.place(x = 533, y = 555.4 - n)


        # Lista vazia das bolas que não foram preenchidas ainda
        bolasSemPreencher = []

        # Contador
        c = 0
        
        # Estrutura de repetição para a criação das bolas que o usuário irá preencher com as escolhas dele durante o jogo
        for bolaSeparada in range (0, 4):
            
            # Soma 90 ao contador
            c += 54


            # Repecitivamente, cria o canvas, mostra ele na tela, cria a bola, configura o canva para preto, posiciona a bola na tela, e manda para a lista das bolas não preenchidas  
            canvaBola1 = tk.Canvas(tela, width=25.2, height=24.3, highlightthickness=0)        
            canvaBola1.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canvaBola1.configure(bg= "black")
            canvaBola1.place(x = 560 + c, y = 520 )
            bolasSemPreencher.append(canvaBola1)


            # Repecitivamente, cria o canvas, mostra ele na tela, cria a bola, configura o canva para preto, posiciona a bola na tela, e manda para a lista das bolas não preenchidas  
            canvaBola2 = tk.Canvas(tela, width=25.2, height=24.3, highlightthickness=0)
            canvaBola2.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canvaBola2.configure(bg= "black")
            canvaBola2.place(x = 560 + c, y = 474 )
            bolasSemPreencher.append(canvaBola2)


            # Repecitivamente, cria o canvas, mostra ele na tela, cria a bola, configura o canva para preto, posiciona a bola na tela, e manda para a lista das bolas não preenchidas  
            canvaBola3 = tk.Canvas(tela, width=25.2, height=24.3, highlightthickness=0)
            canvaBola3.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canvaBola3.configure(bg= "black")
            canvaBola3.place(x = 560 + c, y = 428 )
            bolasSemPreencher.append(canvaBola3)


            # Repecitivamente, cria o canvas, mostra ele na tela, cria a bola, configura o canva para preto, posiciona a bola na tela, e manda para a lista das bolas não preenchidas  
            canvaBola4 = tk.Canvas(tela, width=25.2, height=24.3, highlightthickness=0)
            canvaBola4.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canvaBola4.configure(bg= "black")
            canvaBola4.place(x = 560 + c, y = 380 )
            bolasSemPreencher.append(canvaBola4)


            # Repecitivamente, cria o canvas, mostra ele na tela, cria a bola, configura o canva para preto, posiciona a bola na tela, e manda para a lista das bolas não preenchidas  
            canvaBola5 = tk.Canvas(tela, width=25.2, height=24.3, highlightthickness=0)
            canvaBola5.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canvaBola5.configure(bg= "black")
            canvaBola5.place(x = 560 + c, y = 334 )
            bolasSemPreencher.append(canvaBola5)


            # Repecitivamente, cria o canvas, mostra ele na tela, cria a bola, configura o canva para preto, posiciona a bola na tela, e manda para a lista das bolas não preenchidas  
            canvaBola6 = tk.Canvas(tela, width=25.2, height=24.3, highlightthickness=0)
            canvaBola6.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canvaBola6.configure(bg= "black")
            canvaBola6.place(x = 560 + c, y = 283.5 )
            bolasSemPreencher.append(canvaBola6)


            # Repecitivamente, cria o canvas, mostra ele na tela, cria a bola, configura o canva para preto, posiciona a bola na tela, e manda para a lista das bolas não preenchidas  
            canvaBola7 = tk.Canvas(tela, width=25.2, height=24.3, highlightthickness=0)
            canvaBola7.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canvaBola7.configure(bg= "black")
            canvaBola7.place(x = 560 + c, y = 236.5 )
            bolasSemPreencher.append(canvaBola7)


            # Repecitivamente, cria o canvas, mostra ele na tela, cria a bola, configura o canva para preto, posiciona a bola na tela, e manda para a lista das bolas não preenchidas  
            canvaBola8 = tk.Canvas(tela, width=25.2, height=24.3, highlightthickness=0)
            canvaBola8.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canvaBola8.configure(bg= "black")
            canvaBola8.place(x = 560 + c, y = 190 )
            bolasSemPreencher.append(canvaBola8)


            # Repecitivamente, cria o canvas, mostra ele na tela, cria a bola, configura o canva para preto, posiciona a bola na tela, e manda para a lista das bolas não preenchidas  
            canvaBola9 = tk.Canvas(tela, width=25.2, height=24.3, highlightthickness=0)
            canvaBola9.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canvaBola9.configure(bg= "black")
            canvaBola9.place(x = 560 + c, y = 142 )
            bolasSemPreencher.append(canvaBola9)


            # Repecitivamente, cria o canvas, mostra ele na tela, cria a bola, configura o canva para preto, posiciona a bola na tela, e manda para a lista das bolas não preenchidas  
            canvaBola10 = tk.Canvas(tela, width=25.2, height=24.3, highlightthickness=0)
            canvaBola10.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canvaBola10.configure(bg= "black")
            canvaBola10.place(x = 560 + c, y = 96 )
            bolasSemPreencher.append(canvaBola10)


        instruir = tk.Label(tela, text="DESCUBRA A ORDEM CORRETA DAS CORES.", bg="white", fg="black", font=("Times_New_Roman",12))
        instruir.place(x = 50, y = 180)

        instruir2 = tk.Label(tela, text="EXEMPLO:", bg="white", fg="black", font=("Times_New_Roman",12))
        instruir2.place(x = 50, y = 200)

        instruir3 = tk.Label(tela, text="BOLA BRANCA SIGNIFICA QUE A COR ESTÁ CERTA,", bg="white", fg="black", font=("Times_New_Roman",10))
        instruir3.place(x = 50, y = 260)

        instruir4 = tk.Label(tela, text=" MAS NO LUGAR ERRADO", bg="white", fg="black", font=("Times_New_Roman",10))
        instruir4.place(x = 45, y = 280)

        instruir5 = tk.Label(tela, text="BOLA PRETA SIGNIFICA QUE A COR ESTÁ CERTA", bg="white", fg="black", font=("Times_New_Roman",10))
        instruir5.place(x = 50, y = 400)

        instruir6 = tk.Label(tela, text=" E NO LUGAR CERTO", bg="white", fg="black", font=("Times_New_Roman",10))
        instruir6.place(x = 45, y = 420)


        # Contador
        v = 0

        # Estrutura de repetição para a criação das bolas que foram selecionadas aleatóriamente
        for resultado in range(0, 2):  

            # Cria o fundo do canvas que fica atrás da bola
            respostaCerta = tk.Canvas(tela, width=45, height=45, highlightthickness=0)
            # Cria a bola
            respostaCerta.create_oval(0, 0, 40, 40, fill="white", outline="black")
            # Configura o canvas para branco
            respostaCerta.configure(bg="white")
            # posiciona a bola na tela
            respostaCerta.place(x = 80 + v, y = 320)

            
            # Soma 90 ao contador 
            v += 90

        
        # Contador
        t = 0

        # Estrutura de repetição para a criação das bolas que foram selecionadas aleatóriamente
        for resultado in range(0, 2):  

            # Cria o fundo do canvas que fica atrás da bola
            respostaCerta = tk.Canvas(tela, width=45, height=45, highlightthickness=0)
            # Cria a bola
            respostaCerta.create_oval(0, 0, 40, 40, fill="black", outline="black")
            # Configura o canvas para branco
            respostaCerta.configure(bg="white")
            # posiciona a bola na tela
            respostaCerta.place(x = 80 + t, y = 455)

            
            # Soma 90 ao contador 
            t += 90


        # Lista vazia que irá receber a escolha dos botões feitas pelo usuário
        bolasResultado = []

        # Lista vazia que irá receber a escolha dos botões feitas pelo usuário
        bolasResultado2 = []

        # Lista vazia que irá receber a escolha dos botões feitas pelo usuário
        bolasResultado3 = []

        # Lista vazia que irá receber a escolha dos botões feitas pelo usuário
        bolasResultado4 = []

        # Lista vazia que irá receber a escolha dos botões feitas pelo usuário
        bolasResultado5 = []

        # Lista vazia que irá receber a escolha dos botões feitas pelo usuário
        bolasResultado6 = []

        # Lista vazia que irá receber a escolha dos botões feitas pelo usuário
        bolasResultado7 = []

        # Lista vazia que irá receber a escolha dos botões feitas pelo usuário
        bolasResultado8 = []

        # Lista vazia que irá receber a escolha dos botões feitas pelo usuário
        bolasResultado9 = []

        # Lista vazia que irá receber a escolha dos botões feitas pelo usuário
        bolasResultado10 = []



        # Função verificadora de lista
        def verificarLista():
            
            # Condicional que avalia se há quatro cores na lista
            if len(bolasResultado) == 4:

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolasResultado[0] in set(sorteada) and bolasResultado[0] != sorteada[0]:
                    listaBolas[19].itemconfig(1, fill="white")

                if bolasResultado[1] in set(sorteada) and bolasResultado[1] != sorteada[1]:
                    listaBolas[39].itemconfig(1, fill="white")

                if bolasResultado[2] in set(sorteada) and bolasResultado[2] != sorteada[2]:
                    listaBolas[38].itemconfig(1, fill="white")

                if bolasResultado[3] in set(sorteada) and bolasResultado[3] != sorteada[3]:
                    listaBolas[18].itemconfig(1, fill="white")

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada                
                if bolasResultado[0] in set(sorteada) and bolasResultado[0] == sorteada[0]:
                    listaBolas[19].itemconfig(1, fill="black")

                if bolasResultado[1] in set(sorteada) and bolasResultado[1] == sorteada[1]:
                    listaBolas[39].itemconfig(1, fill="black")

                if bolasResultado[2] in set(sorteada) and bolasResultado[2] == sorteada[2]:
                    listaBolas[38].itemconfig(1, fill="black")

                if bolasResultado[3] in set(sorteada) and bolasResultado[3] == sorteada[3]:
                    listaBolas[18].itemconfig(1, fill="black")


            # Condicional que avalia se há quatro cores na lista
            if len(bolasResultado2) == 4:

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada                
                if bolasResultado2[0] in set(sorteada) and bolasResultado2[0] != sorteada[0]:
                    listaBolas[17].itemconfig(1, fill="white")

                if bolasResultado2[1] in set(sorteada) and bolasResultado2[1] != sorteada[1]:
                    listaBolas[37].itemconfig(1, fill="white")

                if bolasResultado2[2] in set(sorteada) and bolasResultado2[2] != sorteada[2]:
                    listaBolas[36].itemconfig(1, fill="white")

                if bolasResultado2[3] in set(sorteada) and bolasResultado2[3] != sorteada[3]:
                    listaBolas[16].itemconfig(1, fill="white")

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada                
                if bolasResultado2[0] in set(sorteada) and bolasResultado2[0] == sorteada[0]:
                    listaBolas[17].itemconfig(1, fill="black")

                if bolasResultado2[1] in set(sorteada) and bolasResultado2[1] == sorteada[1]:
                    listaBolas[37].itemconfig(1, fill="black")

                if bolasResultado2[2] in set(sorteada) and bolasResultado2[2] == sorteada[2]:
                    listaBolas[36].itemconfig(1, fill="black")

                if bolasResultado2[3] in set(sorteada) and bolasResultado2[3] == sorteada[3]:
                    listaBolas[16].itemconfig(1, fill="black")


            # Condicional que avalia se há quatro cores na lista
            if len(bolasResultado3) == 4:

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada                
                if bolasResultado3[0] in set(sorteada) and bolasResultado3[0] != sorteada[0]:
                    listaBolas[15].itemconfig(1, fill="white")

                if bolasResultado3[1] in set(sorteada) and bolasResultado3[1] != sorteada[1]:
                    listaBolas[35].itemconfig(1, fill="white")

                if bolasResultado3[2] in set(sorteada) and bolasResultado3[2] != sorteada[2]:
                    listaBolas[34].itemconfig(1, fill="white")

                if bolasResultado3[3] in set(sorteada) and bolasResultado3[3] != sorteada[3]:
                    listaBolas[14].itemconfig(1, fill="white")

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada               
                if bolasResultado3[0] in set(sorteada) and bolasResultado3[0] == sorteada[0]:
                    listaBolas[15].itemconfig(1, fill="black")

                if bolasResultado3[1] in set(sorteada) and bolasResultado3[1] == sorteada[1]:
                    listaBolas[35].itemconfig(1, fill="black")

                if bolasResultado3[2] in set(sorteada) and bolasResultado3[2] == sorteada[2]:
                    listaBolas[34].itemconfig(1, fill="black")

                if bolasResultado3[3] in set(sorteada) and bolasResultado3[3] == sorteada[3]:
                    listaBolas[14].itemconfig(1, fill="black")


            # Condicional que avalia se há quatro cores na lista
            if len(bolasResultado4) == 4:

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolasResultado4[0] in set(sorteada) and bolasResultado4[0] != sorteada[0]:
                    listaBolas[13].itemconfig(1, fill="white")

                if bolasResultado4[1] in set(sorteada) and bolasResultado4[1] != sorteada[1]:
                    listaBolas[33].itemconfig(1, fill="white")

                if bolasResultado4[2] in set(sorteada) and bolasResultado4[2] != sorteada[2]:
                    listaBolas[32].itemconfig(1, fill="white")

                if bolasResultado4[3] in set(sorteada) and bolasResultado4[3] != sorteada[3]:
                    listaBolas[12].itemconfig(1, fill="white")

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada                
                if bolasResultado4[0] in set(sorteada) and bolasResultado4[0] == sorteada[0]:
                    listaBolas[13].itemconfig(1, fill="black")

                if bolasResultado4[1] in set(sorteada) and bolasResultado4[1] == sorteada[1]:
                    listaBolas[33].itemconfig(1, fill="black")

                if bolasResultado4[2] in set(sorteada) and bolasResultado4[2] == sorteada[2]:
                    listaBolas[32].itemconfig(1, fill="black")

                if bolasResultado4[3] in set(sorteada) and bolasResultado4[3] == sorteada[3]:
                    listaBolas[12].itemconfig(1, fill="black")


            # Condicional que avalia se há quatro cores na lista
            if len(bolasResultado5) == 4:

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolasResultado5[0] in set(sorteada) and bolasResultado5[0] != sorteada[0]:
                    listaBolas[11].itemconfig(1, fill="white")

                if bolasResultado5[1] in set(sorteada) and bolasResultado5[1] != sorteada[1]:
                    listaBolas[31].itemconfig(1, fill="white")

                if bolasResultado5[2] in set(sorteada) and bolasResultado5[2] != sorteada[2]:
                    listaBolas[30].itemconfig(1, fill="white")

                if bolasResultado5[3] in set(sorteada) and bolasResultado5[3] != sorteada[3]:
                    listaBolas[10].itemconfig(1, fill="white")

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada   
                if bolasResultado5[0] in set(sorteada) and bolasResultado5[0] == sorteada[0]:
                    listaBolas[11].itemconfig(1, fill="black")

                if bolasResultado5[1] in set(sorteada) and bolasResultado5[1] == sorteada[1]:
                    listaBolas[31].itemconfig(1, fill="black")

                if bolasResultado5[2] in set(sorteada) and bolasResultado5[2] == sorteada[2]:
                    listaBolas[30].itemconfig(1, fill="black")

                if bolasResultado5[3] in set(sorteada) and bolasResultado5[3] == sorteada[3]:
                    listaBolas[10].itemconfig(1, fill="black")


            # Condicional que avalia se há quatro cores na lista
            if len(bolasResultado6) == 4:

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolasResultado6[0] in set(sorteada) and bolasResultado6[0] != sorteada[0]:
                    listaBolas[9].itemconfig(1, fill="white")

                if bolasResultado6[1] in set(sorteada) and bolasResultado6[1] != sorteada[1]:
                    listaBolas[29].itemconfig(1, fill="white")

                if bolasResultado6[2] in set(sorteada) and bolasResultado6[2] != sorteada[2]:
                    listaBolas[28].itemconfig(1, fill="white")

                if bolasResultado6[3] in set(sorteada) and bolasResultado6[3] != sorteada[3]:
                    listaBolas[8].itemconfig(1, fill="white")

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolasResultado6[0] in set(sorteada) and bolasResultado6[0] == sorteada[0]:
                    listaBolas[9].itemconfig(1, fill="black")

                if bolasResultado6[1] in set(sorteada) and bolasResultado6[1] == sorteada[1]:
                    listaBolas[29].itemconfig(1, fill="black")

                if bolasResultado6[2] in set(sorteada) and bolasResultado6[2] == sorteada[2]:
                    listaBolas[28].itemconfig(1, fill="black")

                if bolasResultado6[3] in set(sorteada) and bolasResultado6[3] == sorteada[3]:
                    listaBolas[8].itemconfig(1, fill="black")


            # Condicional que avalia se há quatro cores na lista
            if len(bolasResultado7) == 4:

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolasResultado7[0] in set(sorteada) and bolasResultado7[0] != sorteada[0]:
                    listaBolas[7].itemconfig(1, fill="white")

                if bolasResultado7[1] in set(sorteada) and bolasResultado7[1] != sorteada[1]:
                    listaBolas[27].itemconfig(1, fill="white")

                if bolasResultado7[2] in set(sorteada) and bolasResultado7[2] != sorteada[2]:
                    listaBolas[26].itemconfig(1, fill="white")

                if bolasResultado7[3] in set(sorteada) and bolasResultado7[3] != sorteada[3]:
                    listaBolas[6].itemconfig(1, fill="white")

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolasResultado7[0] in set(sorteada) and bolasResultado7[0] == sorteada[0]:
                    listaBolas[7].itemconfig(1, fill="black")

                if bolasResultado7[1] in set(sorteada) and bolasResultado7[1] == sorteada[1]:
                    listaBolas[27].itemconfig(1, fill="black")

                if bolasResultado7[2] in set(sorteada) and bolasResultado7[2] == sorteada[2]:
                    listaBolas[26].itemconfig(1, fill="black")

                if bolasResultado7[3] in set(sorteada) and bolasResultado7[3] == sorteada[3]:
                    listaBolas[6].itemconfig(1, fill="black")


            # Condicional que avalia se há quatro cores na lista
            if len(bolasResultado8) == 4:
                
                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolasResultado8[0] in set(sorteada) and bolasResultado8[0] != sorteada[0]:
                    listaBolas[5].itemconfig(1, fill="white")
                
                if bolasResultado8[1] in set(sorteada) and bolasResultado8[1] != sorteada[1]:
                    listaBolas[25].itemconfig(1, fill="white")
                
                if bolasResultado8[2] in set(sorteada) and bolasResultado8[2] != sorteada[2]:
                    listaBolas[24].itemconfig(1, fill="white")
                
                if bolasResultado8[3] in set(sorteada) and bolasResultado8[3] != sorteada[3]:
                    listaBolas[4].itemconfig(1, fill="white")
                
                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolasResultado8[0] in set(sorteada) and bolasResultado8[0] == sorteada[0]:
                    listaBolas[5].itemconfig(1, fill="black")
                
                if bolasResultado8[1] in set(sorteada) and bolasResultado8[1] == sorteada[1]:
                    listaBolas[25].itemconfig(1, fill="black")
                
                if bolasResultado8[2] in set(sorteada) and bolasResultado8[2] == sorteada[2]:
                    listaBolas[24].itemconfig(1, fill="black")
                
                if bolasResultado8[3] in set(sorteada) and bolasResultado8[3] == sorteada[3]:
                    listaBolas[4].itemconfig(1, fill="black")


            # Condicional que avalia se há quatro cores na lista
            if len(bolasResultado9) == 4:
                
                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolasResultado9[0] in set(sorteada) and bolasResultado9[0] != sorteada[0]:
                    listaBolas[3].itemconfig(1, fill="white")

                if bolasResultado9[1] in set(sorteada) and bolasResultado9[1] != sorteada[1]:
                    listaBolas[23].itemconfig(1, fill="white")

                if bolasResultado9[2] in set(sorteada) and bolasResultado9[2] != sorteada[2]:
                    listaBolas[22].itemconfig(1, fill="white")

                if bolasResultado9[3] in set(sorteada) and bolasResultado9[3] != sorteada[3]:
                    listaBolas[2].itemconfig(1, fill="white")

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolasResultado9[0] in set(sorteada) and bolasResultado9[0] == sorteada[0]:
                    listaBolas[3].itemconfig(1, fill="black")

                if bolasResultado9[1] in set(sorteada) and bolasResultado9[1] == sorteada[1]:
                    listaBolas[23].itemconfig(1, fill="black")

                if bolasResultado9[2] in set(sorteada) and bolasResultado9[2] == sorteada[2]:
                    listaBolas[22].itemconfig(1, fill="black")

                if bolasResultado9[3] in set(sorteada) and bolasResultado9[3] == sorteada[3]:
                    listaBolas[2].itemconfig(1, fill="black")


            # Condicional que avalia se há quatro cores na lista   
            if len(bolasResultado10) == 4:
                
                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolasResultado10[0] in set(sorteada) and bolasResultado10[0] != sorteada[0]:
                    listaBolas[1].itemconfig(1, fill="white")
                
                if bolasResultado10[1] in set(sorteada) and bolasResultado10[1] != sorteada[1]:
                    listaBolas[21].itemconfig(1, fill="white")
                
                if bolasResultado10[2] in set(sorteada) and bolasResultado10[2] != sorteada[2]:
                    listaBolas[20].itemconfig(1, fill="white")
                
                if bolasResultado10[3] in set(sorteada) and bolasResultado10[3] != sorteada[3]:
                    listaBolas[0].itemconfig(1, fill="white")
                
                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolasResultado10[0] in set(sorteada) and bolasResultado10[0] == sorteada[0]:
                    listaBolas[1].itemconfig(1, fill="black")
                
                if bolasResultado10[1] in set(sorteada) and bolasResultado10[1] == sorteada[1]:
                    listaBolas[21].itemconfig(1, fill="black")
                
                if bolasResultado10[2] in set(sorteada) and bolasResultado10[2] == sorteada[2]:
                    listaBolas[20].itemconfig(1, fill="black")
                
                if bolasResultado10[3] in set(sorteada) and bolasResultado10[3] == sorteada[3]:
                    listaBolas[0].itemconfig(1, fill="black")


                # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições
                if bolasResultado[0] != sorteada[0] or bolasResultado[1] != sorteada[1] or bolasResultado[2] != sorteada[2] or bolasResultado[3] != sorteada[3]:
                    # Limpa lista
                    bolasResultado.clear()
                    
                # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições
                if bolasResultado2[0] != sorteada[0] or bolasResultado2[1] != sorteada[1] or bolasResultado2[2] != sorteada[2] or bolasResultado2[3] != sorteada[3]:
                    # Limpa lista
                    bolasResultado2.clear()
                    
                # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições
                if bolasResultado3[0] != sorteada[0] or bolasResultado3[1] != sorteada[1] or bolasResultado3[2] != sorteada[2] or bolasResultado3[3] != sorteada[3]:   
                    # Limpa lista
                    bolasResultado3.clear()
                    
                # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições
                if bolasResultado4[0] != sorteada[0] or bolasResultado4[1] != sorteada[1] or bolasResultado4[2] != sorteada[2] or bolasResultado4[3] != sorteada[3]:      
                    # Limpa lista
                    bolasResultado4.clear()
                    
                # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições
                if bolasResultado5[0] != sorteada[0] or bolasResultado5[1] != sorteada[1] or bolasResultado5[2] != sorteada[2] or bolasResultado5[3] != sorteada[3]:   
                    # Limpa lista
                    bolasResultado5.clear()
                    
                # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições
                if bolasResultado6[0] != sorteada[0] or bolasResultado6[1] != sorteada[1] or bolasResultado6[2] != sorteada[2] or bolasResultado6[3] != sorteada[3]:      
                    # Limpa lista
                    bolasResultado6.clear()
                    
                # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições
                if bolasResultado7[0] != sorteada[0] or bolasResultado7[1] != sorteada[1] or bolasResultado7[2] != sorteada[2] or bolasResultado7[3] != sorteada[3]:      
                    # Limpa lista
                    bolasResultado7.clear()
                    
                 # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições
                if bolasResultado8[0] != sorteada[0] or bolasResultado8[1] != sorteada[1] or bolasResultado8[2] != sorteada[2] or bolasResultado8[3] != sorteada[3]:     
                    # Limpa lista
                    bolasResultado8.clear()
                    
                # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições
                if bolasResultado9[0] != sorteada[0] or bolasResultado9[1] != sorteada[1] or bolasResultado9[2] != sorteada[2] or bolasResultado9[3] != sorteada[3]:    
                    # Limpa lista
                    bolasResultado.clear()
                    
                # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições, limpa lista, cria botão de reiniciar, desabilita botões, declara derrota e mostra o resultado certo na tela
                if bolasResultado10[0] != sorteada[0] or bolasResultado10[1] != sorteada[1] or bolasResultado10[2] != sorteada[2] or bolasResultado10[3] != sorteada[3]:
                        
                    bolasResultado10.clear()
                    criarBotaoReiniciar()
                    desabilitarBotao()
                    mostrarDerrota()  
                    esconder.place_forget()

            
            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada
            if len(bolasResultado) == 4 and bolasResultado[0] == sorteada[0] and bolasResultado[1] == sorteada[1] and bolasResultado[2] == sorteada[2] and bolasResultado[3] == sorteada[3]:
                # Parâmentro teste
                mostrarTriunfo()
                desabilitarBotao()
                criarBotaoReiniciar()
                # Verifica a lista
                bolasResultado.clear()
                esconder.place_forget()
            
            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada
            if len(bolasResultado2) == 4 and bolasResultado2[0] == sorteada[0] and bolasResultado2[1] == sorteada[1] and bolasResultado2[2] == sorteada[2] and bolasResultado2[3] == sorteada[3]:
                # Parâmetro de teste
                mostrarTriunfo()
                desabilitarBotao()
                criarBotaoReiniciar()
                # Verifica a lista
                bolasResultado2.clear()
                esconder.place_forget()

            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada
            if len(bolasResultado3) == 4 and bolasResultado3[0] == sorteada[0] and bolasResultado3[1] == sorteada[1] and bolasResultado3[2] == sorteada[2] and bolasResultado3[3] == sorteada[3]:
                # Parâmetro de teste
                mostrarTriunfo()
                desabilitarBotao()
                criarBotaoReiniciar()
                # Verifica a lista
                bolasResultado3.clear()
                esconder.place_forget()

            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada
            if len(bolasResultado4) == 4 and bolasResultado4[0] == sorteada[0] and bolasResultado4[1] == sorteada[1] and bolasResultado4[2] == sorteada[2] and bolasResultado4[3] == sorteada[3]:
                # Parâmetro de teste
                mostrarTriunfo()
                desabilitarBotao()
                criarBotaoReiniciar()
                # Verifica a lista
                bolasResultado4.clear()
                esconder.place_forget()

            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada
            if len(bolasResultado5) == 4 and bolasResultado5[0] == sorteada[0] and bolasResultado5[1] == sorteada[1] and bolasResultado5[2] == sorteada[2] and bolasResultado5[3] == sorteada[3]:
                # Parâmetro de teste
                mostrarTriunfo()
                desabilitarBotao()
                criarBotaoReiniciar()
                # Verifica a lista
                bolasResultado5.clear()
                esconder.place_forget()

            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada
            if len(bolasResultado6) == 4 and bolasResultado6[0] == sorteada[0] and bolasResultado6[1] == sorteada[1] and bolasResultado6[2] == sorteada[2] and bolasResultado6[3] == sorteada[3]:
                # Parâmetro de teste
                mostrarTriunfo()
                desabilitarBotao()
                criarBotaoReiniciar()
                # Verifica a lista
                bolasResultado6.clear()
                esconder.place_forget()

            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada           
            if len(bolasResultado7) == 4 and bolasResultado7[0] == sorteada[0] and bolasResultado7[1] == sorteada[1] and bolasResultado7[2] == sorteada[2] and bolasResultado7[3] == sorteada[3]:
                # Parâmetro teste
                mostrarTriunfo()
                desabilitarBotao()
                criarBotaoReiniciar()
                # Verifica a lista
                bolasResultado7.clear()
                esconder.place_forget()

            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada           
            if len(bolasResultado8) == 4 and bolasResultado8[0] == sorteada[0] and bolasResultado8[1] == sorteada[1] and bolasResultado8[2] == sorteada[2] and bolasResultado8[3] == sorteada[3]:
                # Parâmetro teste
                mostrarTriunfo()
                desabilitarBotao()
                criarBotaoReiniciar()
                # Verifica a lista
                bolasResultado8.clear()
                esconder.place_forget()

            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada           
            if len(bolasResultado9) == 4 and bolasResultado9[0] == sorteada[0] and bolasResultado9[1] == sorteada[1] and bolasResultado9[2] == sorteada[2] and bolasResultado9[3] == sorteada[3]:
                # Parâmetro teste
                mostrarTriunfo()
                desabilitarBotao()
                criarBotaoReiniciar()
                # Verifica a lista
                bolasResultado9.clear()
                esconder.place_forget()

            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada           
            if len(bolasResultado10) == 4 and bolasResultado10[0] == sorteada[0] and bolasResultado10[1] == sorteada[1] and bolasResultado10[2] == sorteada[2] and bolasResultado10[3] == sorteada[3]:
                # Parâmetro teste
                mostrarTriunfo()
                desabilitarBotao()
                criarBotaoReiniciar()
                # Verifica a lista
                bolasResultado10.clear()
                esconder.place_forget()   
            

            # Se a condicional acima não for satisfeita, o código abaixo é chamado
            else:
                # Agenda a execução da função novamente a cada 100 milissegundos
                tela.after(1000, verificarLista)



        # Função para mudar a cor
        def mudarCor(cor):  
            # Estrutura de repetição que vai ler e ordenar tudo que esta na lista de bolasSemPreencher
            for inteirosDivisiveis, bola in enumerate(bolasSemPreencher):
                # Condicional que só muda de cor se o número divísivel por 10 for inteiro
                if inteirosDivisiveis % 10 == 0:
                    # Obtém a cor atual de qualquer uma das bolas
                    corAtual = bola.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if corAtual == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        bola.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        bolasResultado.append(cor)
                        # Verifica a lista de escolhas                       
                        verificarLista()

                        # Retorna para o começo para esperar a próxima ação
                        return     

            for bolasEspecificas, bola in enumerate(bolasSemPreencher):
                # Condicional que só muda de cor se o número for igual aos propostos
                if bolasEspecificas == 1  or bolasEspecificas == 11 or bolasEspecificas == 21 or bolasEspecificas == 31:
                    # Obtém a cor atual de qualquer uma das bolas
                    corAtual = bola.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if corAtual == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        bola.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        bolasResultado2.append(cor)
                        # Verifica a lista de escolhas                       
                        verificarLista()
                        # Retorna para o começo para esperar a próxima ação             
                        return
                    
            for bolasEspecificas, bola in enumerate(bolasSemPreencher):
                # Condicional que só muda de cor se o número for igual aos propostos
                if bolasEspecificas == 2  or bolasEspecificas == 12 or bolasEspecificas == 22 or bolasEspecificas == 32:
                    # Obtém a cor atual de qualquer uma das bolas
                    corAtual = bola.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if corAtual == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        bola.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        bolasResultado3.append(cor)
                        # Verifica a lista de escolhas                       
                        verificarLista()
                        # Retorna para o começo para esperar a próxima ação             
                        return
                    
            for bolasEspecificas, bola in enumerate(bolasSemPreencher):
                # Condicional que só muda de cor se o número for igual aos propostos
                if bolasEspecificas == 3  or bolasEspecificas == 13 or bolasEspecificas == 23 or bolasEspecificas == 33:
                    # Obtém a cor atual de qualquer uma das bolas
                    corAtual = bola.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if corAtual == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        bola.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        bolasResultado4.append(cor)
                        # Verifica a lista de escolhas                       
                        verificarLista()
                        # Retorna para o começo para esperar a próxima ação             
                        return 

            for bolasEspecificas, bola in enumerate(bolasSemPreencher):
                # Condicional que só muda de cor se o número for igual aos propostos
                if bolasEspecificas == 4  or bolasEspecificas == 14 or bolasEspecificas == 24 or bolasEspecificas == 34:
                    # Obtém a cor atual de qualquer uma das bolas
                    corAtual = bola.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if corAtual == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        bola.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        bolasResultado5.append(cor)
                        # Verifica a lista de escolhas                       
                        verificarLista()
                        # Retorna para o começo para esperar a próxima ação             
                        return
                    
            for bolasEspecificas, bola in enumerate(bolasSemPreencher):
                # Condicional que só muda de cor se o número for igual aos propostos
                if bolasEspecificas == 5  or bolasEspecificas == 15 or bolasEspecificas == 25 or bolasEspecificas == 35:
                    # Obtém a cor atual de qualquer uma das bolas
                    corAtual = bola.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if corAtual == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        bola.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        bolasResultado6.append(cor)
                        # Verifica a lista de escolhas                       
                        verificarLista()
                        # Retorna para o começo para esperar a próxima ação             
                        return 

            for bolasEspecificas, bola in enumerate(bolasSemPreencher):
                # Condicional que só muda de cor se o número for igual aos propostos
                if bolasEspecificas == 6  or bolasEspecificas == 16 or bolasEspecificas == 26 or bolasEspecificas == 36:
                    # Obtém a cor atual de qualquer uma das bolas
                    corAtual = bola.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if corAtual == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        bola.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        bolasResultado7.append(cor)
                        # Verifica a lista de escolhas                       
                        verificarLista()
                        # Retorna para o começo para esperar a próxima ação             
                        return 
                    
            for bolasEspecificas, bola in enumerate(bolasSemPreencher):
                # Condicional que só muda de cor se o número for igual aos propostos
                if bolasEspecificas == 7  or bolasEspecificas == 17 or bolasEspecificas == 27 or bolasEspecificas == 37:
                    # Obtém a cor atual de qualquer uma das bolas
                    corAtual = bola.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if corAtual == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        bola.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        bolasResultado8.append(cor)
                        # Verifica a lista de escolhas                       
                        verificarLista()
                        # Retorna para o começo para esperar a próxima ação             
                        return 


            for bolasEspecificas, bola in enumerate(bolasSemPreencher):
                # Condicional que só muda de cor se o número for igual aos propostos
                if bolasEspecificas == 8  or bolasEspecificas == 18 or bolasEspecificas == 28 or bolasEspecificas == 38:
                    # Obtém a cor atual de qualquer uma das bolas
                    corAtual = bola.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if corAtual == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        bola.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        bolasResultado9.append(cor)
                        # Verifica a lista de escolhas                       
                        verificarLista()
                        # Retorna para o começo para esperar a próxima ação             
                        return 

            for bolasEspecificas, bola in enumerate(bolasSemPreencher):
                # Condicional que só muda de cor se o número for igual aos propostos
                if bolasEspecificas == 9  or bolasEspecificas == 19 or bolasEspecificas == 29 or bolasEspecificas == 39:
                    # Obtém a cor atual de qualquer uma das bolas
                    corAtual = bola.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if corAtual == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        bola.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        bolasResultado10.append(cor)
                        # Verifica a lista de escolhas                       
                        verificarLista()
                        # Retorna para o começo para esperar a próxima ação             
                        return
   

        # Criar botões com certas características específicas
        botaoRoxo = tk.Button(tela, command=lambda: (mudarCor("purple")), bg="purple", fg= "white")

        # Determina o lugar através de coordenadas
        botaoRoxo.place(x=462, y=600)

        # Criar botões com certas características específicas
        botaoAzul = tk.Button(tela, command=lambda: (mudarCor("blue")), bg="blue", fg= "white")
        # Determina o lugar através de coordenada
        botaoAzul.place(x=544, y=600)

        # Criar botões com certas características específicas
        botaoVerde = tk.Button(tela, command=lambda: (mudarCor("green")), bg="green", fg= "white")
        # Determina o lugar através de coordenada
        botaoVerde.place(x=626, y=600)

        # Criar botões com certas características específicas
        botaoAmarelo = tk.Button(tela, command=lambda: (mudarCor("orange")), bg="orange", fg= "white")
        # Determina o lugar através de coordenada
        botaoAmarelo.place(x=708, y=600)

        # Criar botões com certas características específicas
        botaoVermelho = tk.Button(tela, command=lambda: (mudarCor("red")), bg="red", fg= "white")
        # Determina o lugar através de coordenada
        botaoVermelho.place(x=790, y=600)

        # Criar botões com certas características específicas
        botaoMarrom = tk.Button(tela, command=lambda: (mudarCor("brown")), bg="brown", fg="white")
        # Determina o lugar através de coordenada
        botaoMarrom.place(x=872, y=600)

        # Legenda para o título do jogo
        titulo = tk.Label(tela, text="JOGO DA SENHA", bg = "white", fg = "black", font = ("Times_New_Roman", 18))
        # Posiciona o título na tela
        titulo.place(x = 580, y = 30)

        # Instrução para sair da tela
        instrucao = tk.Label(tela, text="Pressione 'ESC', para sair do jogo", bg = "white", fg = "black", font = ("Times_New_Roman", 10))
        # Posiciona a instrução na tela
        instrucao.place(x = 570)

        # contador
        a = 0
        
        # Mostra todas as cooordenadas de y
        posicoesY = [97, 112, 140, 155, 187, 202, 235, 250, 281, 296, 329, 344, 376, 391, 424, 439, 471, 486, 515, 530]

        # Lista vazia para armazenar as bolas que irão indicar se o usuário está no caminho certo
        listaBolas = []

        # Estrutura de repetição para criação de bolas
        for acertos in range(0,2):
            # Soma 40 ao contador
            a += 24
            # Estrutura de repetição que posiciona cada bola no seu devido lugar
            for y in posicoesY:
                # Cria o fundo das bolas
                canvaAcertos = tk.Canvas(tela, width=16.8, height=16.8, highlightthickness=0)
                # Cria as bolas
                canvaAcertos.create_oval(0, 0, 15, 15, fill="grey", outline="grey")
                # Configura a cor para cinza
                canvaAcertos.configure(bg="grey")
                # Define as posições variáveis
                canvaAcertos.place(x=525 + a, y=y)
                # Acrescentas as bolas em uma lista vazia para facilitar a chamada 
                listaBolas.append(canvaAcertos)


# Cria o canvas dentro da janela principal e o deixa com as bordas transparentes
canvasJogo = tk.Canvas(tela, width=1000, height=1000, highlightthickness=0)

# Desenha um quadrado ou rentângulo
retangulo = canvasJogo.create_rectangle(30, 30, 330, 510, fill="black", outline="blue", width=15)

# Configura o fundo do elemento canva para branco
canvasJogo.configure(bg="white")

# Determina o lugar através de coordenadas
canvasJogo.place(x=0, y=50)


# Chamar a função move_right() após um atraso de 10 mílisegundo
canvasJogo.after(10, moverDireita)



# Vincula o botão "ESC" a função fechar tela
tela.bind("<Escape>", fecharTela)

# Mantêm a tela aberta e operando para sempre verificar quaisquer movomentações dentro dela
tela.mainloop()

