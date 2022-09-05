#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

temp = float(input("Insira a temperatura a ser convertida: "));
celsiusToF = temp * 1.8 + 32

print('A temperatura de {:.1f} em °C equivale a {:.1f}°F'.format(temp,celsiusToF))