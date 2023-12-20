class Carros:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = int(ano)

class Restaurante:
    def __init__(self, nome, categoria, estrelas_michelan, localizacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.estrelas_michelan = int(estrelas_michelan)
        self.localizacao = localizacao

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

class Cliente:
    def __init__(self, nome, telefone, ativo, frequencia):
        self.nome = nome
        self.ativo = False
        self.frequencia = frequencia
        self.tel = telefone


carro1 = Carros('Wolksvagen', 'Vermelho', 2022)
restaurante_helena = Restaurante('Mani', 'Comida Brasileira', 5, 'av. Paulista, 187')
cliente1 = Cliente('Juliana', '(11)910598078', True, 'Mensal')

print(restaurante_helena)

class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}!'

    def aniversario(self):
        self.idade += 1


Pessoa = Pessoa('Gabriela', 24)
Pessoa.aniversario()

