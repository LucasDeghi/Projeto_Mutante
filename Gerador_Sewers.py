from random import randint, sample

setor = int(input('Qual o número do setor da dungeon: '))

if setor <=15:
    dado = randint(1, 10)
    print(dado)
    if dado in range(1, 3):
        print('Mercador Baratão')
        resultado = 'Mercador'
        for itens in range(1,4):
            print(randint(1,20))
    elif dado == 3:
        resultado = 'Tesouro'
        print(f'Você encontrou um item no valor de {randint(1, 10)*500}')
    elif dado in range(4, 6):
        resultado = 'Nada'
        print(resultado)
    elif dado in range (6, 10):
        resultado = 'Encontro'
        print(resultado)
        dado_encontro = randint(1, 10)
        if dado_encontro in range(1, 6):
            Batalhas_Faceis = [['RB - B'], ['B - M'], ['RB - M']]
            print(sample(Batalhas_Faceis, 1))
        elif dado_encontro in range(6, 9):
            Batalhas_Medias = [['J'], ['RB - CT'], ['RB - B - CT']]
            print(sample(Batalhas_Medias, 1))
        else:
            Batalhas_Dificeis = [['RT - J - CT'], ['RB - M - J'], ['CT - J - M']]
            print(sample(Batalhas_Dificeis, 1))
    else:
        lista = ['Criança', 'Impedimento']
        extras = lista[randint(0,1)]
        print(extras)
        if extras == lista[0]:
            Desaparecidos = ['Aline', 'Bruna', 'Carlos', 'Daniel', 'Eduarda', 'Fabricio',
                             'Gustavo', 'Heli', 'Izilda', 'Julia', 'Larissa', 'Marcelo']
            Encontrado = sample(Desaparecidos, 1)
            print(Encontrado)
        else:
            dado_impedimento = randint(1, 10)
            if dado_impedimento in range(1, 4):
                print('Gás Tóxico - Provavel que nada esteja perto')
            elif dado_impedimento in range(4, 7):
                print('Ninho de bio horror - Existem monstro perto')
            else:
                print('Lixo industrial - Mercador está próximo')

