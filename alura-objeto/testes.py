# nome
# categoria
# ativo
# atributos e caracteristicas do objeto
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False


restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praca'
restaurante_praca.categoria = 'Gourmet'


restaurante_pizza = Restaurante()

restaurantes = [restaurante_pizza, restaurante_praca]

# dir exibe os atributos e métodos da classe
print(dir(restaurante_praca))

# mostra os valores
print(vars(restaurante_praca))

class Musica:
    musicas = []
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = int(duracao)
        Musica.musicas.append(self)

    def mostrar_musica():
        for m in Musica.musicas:
            print(f'{m.nome} | {m.artista} | {m.duracao} s')

musica1 = Musica('To much Heaven', 'Be Gees', 235)
musica2 = Musica('Bohemian Rhapsody', 'Freddy Mercory', 355)
Musica.mostrar_musica()


# nome
# categoria
# ativo
# atributos e caracteristicas do objeto
# self é para dizer que toda classe restaurante vai ter seu próprio nome, categoria, etc.
# ou seja é a referencia da instância
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    # retorna o texto da instancia para o parametro nome e categoria
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_pizza = Restaurante('Pizza', 'Italiano')

restaurantes = [restaurante_pizza, restaurante_praca]

print(restaurantes[0])
print(restaurantes[1])

# no c# e java em vez de self usa-se this

class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade

livro = Livro('A culpa é das estrelas', 'Fulano', 325)
livro.aumentar_paginas(5)