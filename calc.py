import math
import os

def bask():
    startEnd = ""

    while startEnd != "menu":

        print("ax² + bx + c = 0")

        while True:
            try:
                a = float(input("a = "))
                break
            except ValueError:
                print("Por favor, digite um número válido.")

        while True:
            try:
                b = float(input("b = "))
                break
            except ValueError:
                print("Por favor, digite um número válido.")

        while True:
            try:
                c = float(input("c = "))
                break
            except ValueError:
                print("Por favor, digite um número válido.")

        Δ = (b ** 2) - 4 * a * c

        print("Δ = (b ^ 2) - 4 * a * c")
        print("Δ = (", b, "^ 2 ) - 4 * ", a, " * ", c)
        b2 = b ** 2
        print("Δ = (", b2, ") - 4 *", a, "*", c)
        ac = 4 * a * c
        print("Δ = (", b2, ")", "-", ac)
        print("Δ =", Δ)

        if Δ < 0:
            print("\nNão há raízes reais.")

        else:
            sqrtΔ = math.sqrt(Δ)
            doisA = 2 * a
            if doisA != 0:
                x1 = (-b + sqrtΔ) / doisA
                x2 = (-b - sqrtΔ) / doisA
                print("\nx' = -b + √Δ/2a = {:.2f}".format(x1))
                print('x" = -b - √Δ/2a = {:.2f}'.format(x2))
            else:
                print("Sem resultado possível. (a = 0 e é impossível dividir por 0.)")

        print("\nPressione enter para reiniciar, ou digite 'menu' e presione enter para finalizar.\n")
        startEnd = input()
        if startEnd == "menu":
            print("")
        os.system('clear')
