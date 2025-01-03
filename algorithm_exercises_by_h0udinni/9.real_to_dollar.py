# Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$)
# e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45 (O dólar da época era esse :(  ).

usd = 6.18
print('Dollar exchange rate from 01/03/2025')
n1=float(input('Enter the current money from your wallet (in BRL): '))
print(f'Your current money in dollar is: {n1/usd}. ')