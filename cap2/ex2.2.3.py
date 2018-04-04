# Ex 2.2.3 - Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?
import datetime

t0 = 6 * 60 * 60 + 52 * 60
t1 = 8 * 60 + 15
t2 = 3 * (7 * 60 + 12)
t3 = t1
t_final = t0 + t1 + t2 + t3

print(datetime.timedelta(seconds=t_final))