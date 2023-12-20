class Livro:
    livros = []
    def __init__(self, titulo, autor, ano_publicacao):
        self.disponivel = True
        self.title = titulo
        self.writer = autor
        self.year_publication = int(ano_publicacao)
        Livro.livros.append(self)

    def __str__(self):
        for l in Livro.livros:
            return f'{self.title} | {self.writer} | {self.year_publication} | {self.disponibilidade}'

    def emprestar(self):
        self.disponivel = False

    @property
    def disponibilidade(self):
        return 'Disponível' if self.disponivel else 'Indisponível'

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = []
        for l in Livro.livros:
            if l.year_publication == ano and l.disponivel:
                livros_disponiveis.append(l)
        return livros_disponiveis
