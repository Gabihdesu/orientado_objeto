from modelos import restaurante

restaurante_praca = restaurante.Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Guilherme', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Gabi', 5)

'''restaurante_mexicano = restaurante.Restaurante('Mexican Food', 'Mexicana')
restaurante_japa = restaurante.Restaurante('Akira', 'Asiatica')
restaurante_mexicano.alternar_estado()'''


def main():
    restaurante.Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
