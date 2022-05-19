from tkinter import YES
from jogador import Jogador
from random import choice


class JogoDaForca():
    '''Classe dedicada a gerir as regras e a mecânica do Jogo da Forca'''
    def __init__(self):
        '''O dicionário 'palavras' receberá as palavras do arquivo txt bem como as dicas sobre as palavras que também 
        estão no arquivo txt'''
        self.palavras = {}


    def start(self):
        '''Método contém a mecânica do jogo onde os usuários, através de inputs, irão interagir com o jogo '''
        jogador = input('Jogador digite seu nome: ')
        if jogador not in Jogador().ranking:
            Jogador().ranking[jogador] = [['vitórias', 0], ['derrotas', 0]]

        with open('Lista-de-Palavras.txt', 'r', encoding='utf-8') as arquivo_txt:
            '''Arquivo txt que contém as palvras utilizadas no jogo e também suas respectivas dicas. Apenas há 2 dicas por palavras'''
            lista_palavras = [x for x in arquivo_txt.read().split()]
            for i in lista_palavras:
                if i.islower:
                    self.palavras[i] = [lista_palavras[lista_palavras.index(i)+1], lista_palavras[lista_palavras.index(i)+2]]
            arquivo_txt.close()
        palavra = choice([x for x in self.palavras])
        frase="_"*len(palavra)
        print(f'A palavra tem {len(palavra)} letras\n')
        palavra_lista=list(palavra)
        erro = 0
        dica = 0
        while erro < 5 and frase != palavra:
            '''O usuário poderá errar por 5 vezes, seguidas ou não. O jogo continuará até a palavra ser acertada 
            pelo usuário ou caso ocorram 5 erros, o que ocorrer primeiro'''
            palpite = input("Digite uma letra. Para receber uma dica, digite 'dica': ")
            if len(palpite) > 1 and palpite != 'dica':
                print('Informe apenas uma letra por tentativa\n')
            elif palpite == 'dica':
                dica +=1
                if dica == 1:
                    print(f'A palavra é um(a) {self.palavras[palavra][0]}\n')
                elif dica == 2:
                    print(f'A segunda dica é: {self.palavras[palavra][1]}\n')
                else:
                    print(f'Não há mais dicas. Agora é com você, jovem Padawan! Que a Força esteja com você\n')
            else:
                for i in range(len(palavra)):
                    if palavra_lista[i] == palpite:
                        letra = list(frase)
                        letra[i] = palpite
                        frase="".join(letra)
                print(frase)
                if palpite not in palavra:
                    erro += 1
                    if erro == 1:
                        print('---------')
                        print('|      MMM')
                        print('|     do.ob')
                        print('|     ( - )')
                        print('|')
                        print('|')
                        print('|')
                    elif erro == 2:
                        print('---------')
                        print('|      MMM')
                        print('|     do.ob')
                        print('|     ( - )')
                        print('|    o=|')
                        print('|')
                        print('|')
                    elif erro == 3:
                        print('---------')
                        print('|      MMM')
                        print('|     do.ob')
                        print('|     ( - )')
                        print('|    o=| |=o')
                        print('|')
                        print('|')
                    elif erro == 4:
                        print('---------')
                        print('|      MMM')
                        print('|     do.ob')
                        print('|     ( O ) <(Não pode mais errar!)')
                        print('|    o=| |=o')
                        print('|      U')
                        print('|')
                    elif erro == 5:
                        print('---------')
                        print('|      MMM')
                        print('|     dx.xb')
                        print('|     ( 0 )')
                        print('|    o=| |=o')
                        print('|      U U')
                        print('|')
        '''Mensagens após a partida, que também revela qual era a palavra a ser descoberta '''
        if erro == 5:
            Jogador().ranking[jogador][1][1] += 1
            print('GAME OVER. Você perdeu!')
            print(f'A palavra era: {palavra.upper()}\n')
        elif frase == palavra:
            Jogador().ranking[jogador][0][1] += 1
            print(f'{palavra.upper()}. Você ganhou! Parabéns!\n')
        
    def ranking(self):
        '''Método que exibe a classificação dos jogadores, levando em consideração o número de vitórias e derrotas'''
        if len(Jogador().ranking) > 0:
            classificacao = dict(sorted(Jogador().ranking.items(), key=lambda x: x[1][1] and x[1][0], reverse=True))
            for jogador, desempenho in classificacao.items():
                print(f"{jogador} - {desempenho[0][1]} vitória(s) e {desempenho[1][1]} derrota(s)")
        else:
            print('O ranking de jogadores está vazio\n')


