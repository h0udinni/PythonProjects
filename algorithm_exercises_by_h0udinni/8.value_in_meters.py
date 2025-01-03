# Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.
# Ex:
# Digite uma distância em metros: 185.72
# A distância de 85.7m corresponde a:
# 0.18572Km
# 1.8572Hm
# 18.572Dam
# 1857.2dm
# 18572.0cm
# 185720.0mm

n1=float(input('Enter a distance in meters: '))
print(f'The distance in M (meter) is: {n1} m.')
print(f'The distance in Km (kilometer) is: {n1/1000} Km.') #divida o valor de comprimento por 1000
print(f'The distance in Hm (hectometer) is: {n1/100} Hm.') #divida o valor de comprimento por 100
print(f'The distance in Dam (decameter) is: {n1/10} Dam.') #divida o valor de comprimento por 10
print(f'The distance in Dm (decimeter) is: {n1*10} Dam.') #Multiplique o valor de comprimento por 10
print(f'The distance in cm (centimeter) is: {n1*100} Dam.') #Multiplique o valor de comprimento por 100
print(f'The distance in mm (milimeter) is: {n1*1000} Dam.') #Multiplique o valor de comprimento por 1000