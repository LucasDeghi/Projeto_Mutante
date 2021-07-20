from random import randint

lista_resultados = {11: {'Ambiente':'Campo Vitrificado', 'Ruina':'Não', 'Ameaça': 'Sim', 'Artefatos': 'Não'},
                    12: {'Ambiente':'Cratera Enorme', 'Ruina':'Não', 'Ameaça': 'Sim', 'Artefatos': 'Não'},
                    13: {'Ambiente': 'Deserto de Cinzas',  'Ruina':'Não', 'Ameaça': 'Sim', 'Artefatos': 'Não'},
                    14: {'Ambiente':'Deserto de Cinzas',  'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'},
                    15: {'Ambiente': 'Fábricas Abaondonadas',  'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'},
                    16:{'Ambiente': 'Fábricas Abaondonadas',  'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'},
                    21:{'Ambiente': 'Fábricas Abaondonadas',  'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'},
                    22:{'Ambiente': 'Fábricas Abaondonadas',  'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'},
                    23:{'Ambiente': 'Mata Densa', 'Ruina':'Não', 'Ameaça': 'Sim', 'Artefatos': 'Não'},
                    24:{'Ambiente': 'Mata Densa', 'Ruina':'Não', 'Ameaça': 'Sim', 'Artefatos': 'Não'},
                    25:{'Ambiente': 'Mata Morta', 'Ruina':'Não', 'Ameaça': 'Sim', 'Artefatos': 'Não'},
                    26:{'Ambiente': 'Mata Morta', 'Ruina':'Não', 'Ameaça': 'Sim', 'Artefatos': 'Não'},
                    31:{'Ambiente': 'Mata Morta', 'Ruina':'Não', 'Ameaça': 'Sim', 'Artefatos': 'Não'},
                    32:{'Ambiente': 'Matagal', 'Ruina':'Não', 'Ameaça': 'Sim', 'Artefatos': 'Não'},
                    33:{'Ambiente': 'Matagal', 'Ruina':'Não', 'Ameaça': 'Sim', 'Artefatos': 'Não'},
                    34:{'Ambiente': 'Matagal', 'Ruina':'Não', 'Ameaça': 'Sim', 'Artefatos': 'Não'},
                    35:{'Ambiente': 'Pântano', 'Ruina':'Não', 'Ameaça': 'Sim', 'Artefatos': 'Não'},
                    36:{'Ambiente': 'Pântano', 'Ruina':'Não', 'Ameaça': 'Sim', 'Artefatos': 'Não'},
                    41:{'Ambiente': 'Povoado', 'Ruina':'-', 'Ameaça': '-', 'Artefatos': '-'},
                    42:{'Ambiente': 'Povoado', 'Ruina':'-', 'Ameaça': '-', 'Artefatos': '-'},
                    43:{'Ambiente': 'Ruínas Desabando', 'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'},
                    44:{'Ambiente': 'Ruínas Desabando', 'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'},
                    45:{'Ambiente': 'Ruínas Desabando', 'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'},
                    46:{'Ambiente': 'Ruínas Deterioradas', 'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'},
                    51:{'Ambiente': 'Ruínas Deterioradas', 'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'},
                    52:{'Ambiente': 'Ruínas Deterioradas', 'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'},
                    53:{'Ambiente': 'Ruínas Deterioradas', 'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'},
                    54:{'Ambiente': 'Ruínas Deterioradas', 'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'},
                    55:{'Ambiente': 'Ruínas Encobertas', 'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'},
                    56:{'Ambiente': 'Ruínas Encobertas', 'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'},
                    61:{'Ambiente': 'Ruínas Encobertas', 'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'},
                    62:{'Ambiente': 'Ruínas Intactas', 'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'},
                    63:{'Ambiente': 'Ruínas Intactas', 'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'},
                    64:{'Ambiente': 'Ruínas Intactas', 'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'},
                    65:{'Ambiente': 'Ruínas Intactas', 'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'} ,
                    66:{'Ambiente': 'Ruínas Intactas', 'Ruina':'Sim', 'Ameaça': 'Sim', 'Artefatos': 'Sim'}}


Ruinas_normais_tabela = {11:'Abrigo', 12:'Arranha-céus', 13:'Avião Caído',
                         14:'Bairro Residencial', 15:'Campo de Batalha', 16:'Centro Esportivo',
                         21:'Cinema', 22:'Cratera', 23:'Delegacia de Polícia',
                         24:'Edifício de Escritórios', 25:'Escola', 26:'Estação de Metro',
                         31:'Estação de Rádio', 32:'Estação de Trem', 33:'Estacionamento',
                         34:'Hospital', 35:'Igreja', 36:'Lanchonete Fast-Food',
                         41:'Loja de Caça', 42:'Mansão Arruinada', 43:'Marina',
                         44:'Museu', 45:'Parque de Diversões', 46:'Parque Encoberto',
                         51:'Piscina Pública', 52:'Playground', 53:'Ponte Arruinada',
                         54:'Posto de Gasolina', 55:'Rodovia', 56:'Rodoviária',
                         61:'Shopping', 62:'Subúrbio', 63:'Supermercado',
                         64:'Tanque', 65:'Teatro', 66:'Túnel'}


Ruinas_industriais_tabela = {11: 'Base Militar', 12: 'Base Militar', 13: 'Base Militar',
                             14: 'Clube de Tiro', 15: 'Clube de Tiro', 16: 'Clube de Tiro',
                             21: 'Estação Depuradora', 22: 'Estação Depuradora', 23: 'Estação Depuradora',
                             24: 'Fábrica', 25: 'Fábrica', 26: 'Fábrica',
                             31: 'Linha Elétrica', 32: 'Linha Elétrica', 33: 'Linha Elétrica',
                             34: 'Lixão', 35: 'Lixão', 36: 'Lixão',
                             41: 'Moinho de Vento', 42: 'Moinho de Vento', 43: 'Moinho de Vento',
                             44: 'Navio Encalhado', 45: 'Navio Encalhado', 46: 'Navio Encalhado',
                             51: 'Refinaria', 52: 'Refinaria', 53: 'Refinaria',
                             54:'Tanque de Petróleo', 55:'Tanque de Petróleo', 56:'Tanque de Petróleo',
                             61:'Torre de Rádio', 62:'Torre de Rádio', 63:'Torre de Rádio',
                             64:'Tubulação', 65:'Tubulação', 66:'Tubulação'}



def d66():
    dado_d = randint(1, 6)
    dado_u = randint(1, 6)
    resultado = str(dado_d) + str(dado_u)
    return int(resultado)


class Gerador_Setor:

    def ambiente_setor(self):
        self.Ambiente = lista_resultados[dado]['Ambiente']
        return self.Ambiente

    def ruina_setor(self):
        self.Ruina =  lista_resultados[dado]['Ruina']
        return self.Ruina

    def ameaça_setor(self):
        self.Ameaça = lista_resultados[dado]['Ameaça']
        return self.Ameaça

    def artefato_setor(self):
        self.Artefato = lista_resultados[dado]['Artefatos']
        return self.Artefato

dado = d66()



class Desafio_setor:
    def Tipo_Ruina(self):
        Gerador_Setor().ruina_setor()
        if  Gerador_Setor().ruina_setor() == 'Sim':
            escolha = randint(1, 2)
            if escolha == 1:
                return print('A ruina deste setor é um(a): ', Ruinas_normais_tabela[d66()])
            else:
                return print('A ruina deste setor é um(a): ', Ruinas_industriais_tabela[d66()])


    def nivel_podridao(self):
        dado = d66()
        if dado in range(11, 13):
            self.podridao = 'Temos um Oásis de Podridão (nível 0)'
        elif dado in range(13, 56):
            self.podridao = 'Temos podridão Fraca aqui (nível 1)'
        else:
            self.podridao = 'Área de Podridão Forte (nível 2)'
        return print(self.podridao)



    def nivel_ameaça(self):
        evento = []
        nivel = randint(1,6) + randint(1, 6)
        for i in range(1, nivel + 1):
           decisao = randint(1 , 6)
           if decisao == 1:
              tipo = randint(1, 6)
              if tipo in range(1, 3):
                evento.append('Ameaça Humanoide')
              elif tipo in range(3, 6):
                evento.append('Ameaça Monstruosa')
              else:
               evento.append('Ameaça de Fenômeno')
           elif decisao == 6:
              evento.append('Artefato')
        return print(evento)





