from random import randint
import time
import matplotlib.pyplot as plt

def gerar_graficos(tempos, acertos):
    #tempo / k
    fig1, ax1 = plt.subplots()
    ax1.set_title('Tempo - K')
    ax1.set_ylabel('Tempo (segundos)')
    ax1.set_xlabel('K')
    ax1.scatter(list(range(9, 17)), tempos)
    fig1.savefig(f"graficos/tempo_k.png")

    #Acertos / K 
    fig3, ax3 = plt.subplots()
    ax3.set_title('Acertos por K')
    ax3.set_ylabel('Acertos')
    ax3.set_xlabel('K')
    ax3.scatter(list(range(9, 17)), acertos)
    fig3.savefig(f"graficos/acertos_k.png")


def ler_arquivos():          #lê os arquivos separando os arquivos de teste em imagens_testes 
    imagens_dicionario = []  #e as imagens para o dicionário em imagens_dicionario
    imagens_testes = []
    for i in range(1,41): 
        position = randint(1,10)
        imagem = []
        for j in range(1,11):
            arquivo = open(f"orl_faces/s{i}/{j}.pgm", "rb").read()[14:] #ignorar cabeçalho
            arquivo = arquivo.decode('ISO-8859-1')
            if j == position:
                imagens_testes.append(arquivo)
            else:
                imagem.append(arquivo)
        imagens_dicionario.append(imagem)
    return imagens_dicionario, imagens_testes

def criar_dicionarios(array_mensagens, k): 
    dicionario = {}       
    for i in range(256):   #iniciando o dicionário com o alfabeto
        dicionario[i.to_bytes(1, 'big')]=i

    #variáveis que serão usadas no LZD
    tamanho_dicionario = 256  #tamanho do dicionáro + 1 (indica o próximo local livre a ser inserido)
    char_atual =''
    char_anterior =''
    for mensagem in array_mensagens:
        for char in mensagem: #percorre toda a mensagem
            char_atual=char_anterior+char

            if char_atual.encode('ISO-8859-1') not in dicionario: #verifica se já existe o símbolo no dicionário
                if len(dicionario)<2**k:
                    dicionario[char_atual.encode('ISO-8859-1')]=tamanho_dicionario
                    tamanho_dicionario+=1
                char_anterior=char
            else:
                char_anterior=char_atual 
    return dicionario

def comprimir_testes(imagem_teste, dicionario):
    comprimida = []
    char_atual = ''
    char_anterior = ''
    indices_usados =  {}

    for pixels in imagem_teste:
        char_atual = char_anterior + pixels
        if char_atual.encode('ISO-8859-1') not in dicionario: 
            numCod = dicionario[char_anterior.encode('ISO-8859-1')]
            comprimida.append(numCod)
            char_anterior = pixels
            indices_usados[numCod] = True
        else:
            char_anterior = char_atual

    numCod = dicionario[char_anterior.encode('ISO-8859-1')]
    indices_usados[numCod] = True
    comprimida.append(numCod)
    
    return len(comprimida), len(indices_usados)




imagens_dicionario, imagens_testes = ler_arquivos()
dicionarios = []
tempos = []
total_acertos = []
for k in range(9,17):  #k variando de 9 até 16
    #gerar os 40 dicionários
    tempo_inicial = time.time() 
    dicionarios = []
    for rostos in imagens_dicionario: #rostos nesse caso representa todas as imagens de uma pasta removendo apenas a de teste, 
        dicionarios.append(criar_dicionarios(rostos, k)) #portanto tem 9 imagens e vai gerar um dicionário

    num_imagem = 0 #representa o indice da imagem para usar na validação, de forma que o esperado é que a num_imagem = 0 
    acertos = 0    #seja melhor compactada com o dicionario[0]
    for imagem in imagens_testes:
        tamanhos = []#vai registrar quantos indices foram usados para comprimir a imagem em todos os dicionários
        for dicionario in dicionarios:
            tam_img, indices = comprimir_testes(imagem, dicionario)
            tamanhos.append(indices)
        if num_imagem == tamanhos.index(max(tamanhos)): #pega o indice do maior número de indices usados para compactar 
            acertos = acertos + 1                       #o que significa maior compactibilidade, se for igual ao indice da imagem
        num_imagem = num_imagem + 1                     #representa um acerto
    tempo_final = time.time()
    tempos.append(tempo_final-tempo_inicial)
    print(f"K-{k}: Acertos={acertos}")
    total_acertos.append(acertos)
gerar_graficos(tempos, total_acertos)




    














