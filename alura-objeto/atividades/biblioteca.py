from atividades import livro

Livro1 = livro.Livro('Um pedido as estrelas', 'Priscille Sibley', 2013)
Livro2 = livro.Livro('o orfanato da srta peregrine', 'Ransom Riggs', 2015)
Livro3 = livro.Livro('Sabororso Cadáver', 'Agustina Bazter', 2013)


ano_especifico = 2013
livros_disponiveis_nesse_ano = livro.Livro.verificar_disponibilidade(ano_especifico)

print(Livro1)
print(Livro2)
print(f'Temos {livros_disponiveis_nesse_ano} disponíveis publicados no ano {ano_especifico}')




