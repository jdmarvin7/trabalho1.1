numero1 = float(input("digite um numero: "))
operador = input("digite um operador: ")
numero2 = float(input(("digite outro numero: ")))
resultado = 0

if operador == "+":
    resultado = numero1 + numero2
    print("O resultado é: ",resultado)
elif operador == "-":
    resultado = numero1 - numero2
    print("O resultado é: ", resultado)
elif operador == "*":
    resultado = numero1 * numero2
    print("O resultado é: ", resultado)
elif operador == "/":
    resultado = numero1 / numero2
    print("O resultado é: ", resultado)
else:
    print("opçao invalida")

if resultado%2 == 0:
    print("par")
else:
    print("impar")
if resultado == int(resultado):
    print("O tipo é inteiro")
else:
    print("é decimal")

if resultado >= 0:
    print("positivo")
else:
    print("negativo")





