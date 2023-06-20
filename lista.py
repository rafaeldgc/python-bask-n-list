import os
import math


def listaNum():
    startEnd = ""
    while startEnd != "menu":
        lista = []
        quadrados = []
        sqrt = []
        num = 0
        soma = 0
        somaNumQuadrado = 0
        somaSqrt = 0
        contador = 0

        while num != "=":
            contador = contador + 1
            print("Digite o", contador, "º número:")
            print('Digite "=" quando terminar.')
            num = input()
            if num == "=":
                os.system('clear')
                print("Quantidade de números digitados:", contador - 1)
                print("\nNumeros digitados:", lista)
                print("Soma dos números digitados:", soma)
                print("\nQuadrados dos números digitados:", quadrados)
                print("Soma dos quadrados dos números digitados:", somaNumQuadrado)
                print("\nRaizes quadradas dos números digitados:", sqrt)
                print("Soma das raízes quadradas dos números digitados:", somaSqrt)
                print("")
            else:
                while True:
                    try:
                        num = float(num)
                        break
                    except ValueError:
                        os.system('clear')
                        print(lista)
                        print("Erro: Por favor, digite um número válido.")
                        print("Digite o", contador, "º número:")
                        num = input()
                lista.append(num)
                quadrados.append(num ** 2)
                if num > 0:
                    sqrt.append(math.sqrt(num))
                    soma = soma + num
                    somaNumQuadrado = somaNumQuadrado + (num ** 2)
                    somaSqrt = somaSqrt + (math.sqrt(num))
                else:
                    sqrt.append("N/A")
                    soma = soma + num
                    somaNumQuadrado = somaNumQuadrado + (num ** 2)
                os.system('clear')
                print(lista)
        print("Pressione enter para reiniciar, ou digite 'menu' e presione enter para voltar ao menu principal.")
        startEnd = input()
        if startEnd == "menu":
            print("")
        os.system('clear')