produto = input("maça ou morango")
morango = 0
maça = 0
kg_morango = 0
kg_maça = 0
preço_total = 0
peso = float(input("digite o peso (kg) do morango"))


if produto == "morango":
    kg_morango = 2.50
    peso = print("digite o peso (kg) do morango")
    if morango <= 5:
        kg_morango = 2.50
        peso = print("digite o peso (kg) do morango")
        preço_total = (peso) * kg_morango
        print(preço_total)
    elif morango > 5:
        kg_morango = 2.20
        preço_total = peso * kg_morango
# nao terminado






