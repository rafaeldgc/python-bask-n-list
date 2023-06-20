import calc
import lista
import os

print("Selecione: ")
selecionar = ''
while selecionar != "3":
    selecionar = input(
        "1 - Calculadora De Equações do 2º grau\n2 - Lista de Números\n3 - Finalizar o programa\nDigite uma opção: ")
    if selecionar == "1":
        os.system('clear')
        calc.bask()
    elif selecionar == "2":
        os.system('clear')
        lista.listaNum()
    elif selecionar == "3":
        os.system('clear')
        pass
    else:
        os.system('clear')
        selecionar = print("Por favor selecione uma opção válida.")
else:
    print("Programa finalizado.")

input('Pressione "Enter" para sair')