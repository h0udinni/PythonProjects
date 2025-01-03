# Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma mensagem.
# Ex:
# Nome do Funcionário: Maria do Carmo
# Salário: 1850,45
# O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho.
employee=(input("What's your name? "))
wage=float(input("What is your salary? "))
print(f"Employee name: {employee}")
print(f"Salary: {wage}")
print(f"O funcionário {employee} tem um salário de R${wage} em Janeiro.")