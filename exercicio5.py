tipo_Combustivel = input("digite o nome do combustivel: ")
descont_Alcool = 0
descont_Gas = 0
preço_Litro = 0
preço_Final = 0
preço_Total_da_quant_digitado = 0

# COMBUSTIVEL ALCOOL
if tipo_Combustivel == "alcool":
    preço_Litro = 1.90
    quant_Litros = float(input("digite a quantidade de litros de alcool:  "))
    if quant_Litros <= 20:
        preço_Total_da_quant_digitado = quant_Litros * preço_Litro
        descont_Alcool = preço_Total_da_quant_digitado * 3 / 100
        preço_Final = preço_Total_da_quant_digitado - descont_Alcool

        print(f"Voce escolheu Alcool, para {quant_Litros} litros(L) o desconto vai ser {descont_Alcool}R$, vai pagar {preço_Total_da_quant_digitado - descont_Alcool}R$")
    elif quant_Litros > 20:
        descont_Alcool = preço_Total_da_quant_digitado * 5 / 100
        preço_Final = preço_Total_da_quant_digitado - descont_Alcool
        print(f"Voce escolheu Alcool, para {quant_Litros} litros(L) o desconto vai ser {descont_Alcool}R$,  vai pagar {preço_Total_da_quant_digitado - descont_Alcool}R$")
    else:
        print("Opçao invalida. Tente novamente! So pode digitar alcool ou gasolina.")

# COMBUSTIVEL GASOLINA
if tipo_Combustivel == "gasolina":
    preço_Litro = 2.50
    quant_Litros = float(input("digite a quantidade de litros, de gasolina:  "))
    if quant_Litros <= 20:
        preço_Total_da_quant_digitado = quant_Litros * preço_Litro
        descont_Gas = preço_Total_da_quant_digitado * 4 / 100
        preço_Final = preço_Total_da_quant_digitado - descont_Gas

        print(f"Voce escolheu Gasolina, para {quant_Litros} litros(L) o desconto vai ser {descont_Gas}R$,  vai pagar {preço_Total_da_quant_digitado - descont_Gas}R$")
    elif quant_Litros > 20:
        descont_Gas = preço_Total_da_quant_digitado * 6 / 100
        preço_Final = preço_Total_da_quant_digitado - descont_Gas
        print(f"Voce escolheu Gasolina, para {quant_Litros} litros(L) o desconto vai ser {descont_Gas}R$, vai pagar {preço_Total_da_quant_digitado - descont_Gas}R$")
else:
    print("Opçao invalida. Tente novamente!, So pode digitar alcool ou gasolina.")




