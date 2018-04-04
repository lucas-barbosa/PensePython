# Ex 2.2.2 - Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?
preco = 24.95
desconto = 0.40 * preco
preco_atacado = preco - desconto
quantidade_livros = 60
transporte_primeira_unidade = 3
transporte_adicional = 0.75
transporte = (quantidade_livros - 1) * transporte_adicional + transporte_primeira_unidade

valor_total = preco_atacado * quantidade_livros + transporte
print(valor_total)