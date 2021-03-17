pergunta_1 = input("Telefonou para a vitima: ")
pergunta_2 = input("Esteve no local do crime: ")
pergunta_3 = input("Mora perto da vitima: ")
pergunta_4 = input("devia para a vitima: ")
pergunta_5 = input("Ja trabalhou com a vitima: ")

if pergunta_1 == "sim":
    pergunta_1 = 1
elif pergunta_1 == "nao":
    pergunta_1 = 0
else:
    print("So pode responder com sim ou nao, na pergunta 1.")
if pergunta_2 == "sim":
    pergunta_2 = 1
elif pergunta_2 == "nao":
    pergunta_2 = 0
else:
    print("So pode responder com sim ou nao, na pergunta 2.")
if pergunta_3 == "sim":
    pergunta_3 = 1
elif pergunta_3 == "nao":
    pergunta_3 = 0
else:
    print("So pode responder com sim ou nao, na pergunta 3.")
if pergunta_4 == "sim":
    pergunta_4 = 1
elif pergunta_4 == "nao":
    pergunta_4 = 0
else:
    print("So pode responder com sim ou nao, na pergunta 4.")
if pergunta_5 == "sim":
    pergunta_5 = 1
elif pergunta_5 == "nao":
    pergunta_5 = 0
else:
    print("So pode responder com sim ou nao, na pergunta 5.")

if (pergunta_1 + pergunta_2 + pergunta_3 + pergunta_4 + pergunta_5) == 2:
    print("--------------------------------------------------------------")
    print("                       Suspeita                              ")
    print("--------------------------------------------------------------")
elif pergunta_1 + pergunta_2 + pergunta_3 + pergunta_4 + pergunta_5 == 3:
    print("--------------------------------------------------------------")
    print("                       Cumplice                                ")
    print("--------------------------------------------------------------")
elif pergunta_1 + pergunta_2 + pergunta_3 + pergunta_4 + pergunta_5 == 4:
    print("--------------------------------------------------------------")
    print("                       Cumplice                               ")
    print("--------------------------------------------------------------")
else:
    if pergunta_1 + pergunta_2 + pergunta_3 + pergunta_4 + pergunta_5 == 5:
        print("--------------------------------------------------------------")
        print("                        Assassino                             ")
        print("--------------------------------------------------------------")



