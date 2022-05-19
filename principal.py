from forca import JogoDaForca
from time import sleep

def menu():
    '''Menu para o usuário inicar uma partida e ver o ranking dos jogadores'''
    print('''      -------------------------------
      Jogo da Forca
      Escolha uma opção abaixo:
      [1] Iniciar uma partida
      [2] Mostrar ranking de jogadores
      [3] Sair
      -------------------------------''')
    opcao = str(input('Digite sua opção: '))
    if opcao == '1':
        JogoDaForca().start()
        return menu()
    elif opcao == '2':
        JogoDaForca().ranking()
        return menu()
    elif opcao == '3':
        print('Fechando..')
        sleep(1)
        print('Até uma próxima partida')
    else:
        return menu()

menu()