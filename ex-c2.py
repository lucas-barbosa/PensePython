# -*- coding: utf-8 -*-
import datetime

# Ex 2.2.1 - O volume de uma esfera com raio r é 4/3 * PI * r³. Qual é o volume de uma esfera com raio 5?
raio = 5
volume = (4 * 3.14 * raio ** 3) / 3
print(volume)

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

# Ex 2.2.3 - Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?
t0 = 6 * 60 * 60 + 52 * 60
t1 = 8 * 60 + 15
t2 = 3 * (7 * 60 + 12)
t3 = t1
t_final = t0 + t1 + t2 + t3

print(datetime.timedelta(seconds=t_final))