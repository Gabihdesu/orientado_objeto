# atributos e caracteristicas do objeto
# self é para dizer que toda classe restaurante vai ter seu próprio nome, categoria, etc.
# ou seja é a referencia da instância

from modelos.avaliacao import Avaliacao
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        # _ é usado para definir que o atributo não deve ser alterado pelo usuario
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    # retorna o texto da instancia para o parametro nome e categoria
    def __str__(self):
        return f'{self._nome} | {self.categoria}'

    # criar proprio metodos
    # metodo referenciando a classe
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for r in Restaurante.restaurantes:
            print(f'{r._nome.ljust(25)} | {r.categoria.ljust(25)} | {str(r.media_avaliacoes).ljust(25)} '
                  f'| {r.ativo}')

    # modificar como um atributo é lido
    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'

    # metodo para os objetos
    def alternar_estado(self):
        # se tiver false fica true se tiver true fica false
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if nota <= 5:
            self.avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(self.avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Sem avaliação'
        soma_notas = sum(self.avaliacao._nota for a in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas / quantidade_notas, 1)
        return media
