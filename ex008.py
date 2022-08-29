#Escreva um programa que leia um valor em metros e o exiba convertido
#em centimetros e milimetros.

from calendar import c


m = float(input('Digite um valor em metros. '));

c = m * 100;
mm = m * 1000;

print('{} em Centimetros é {} e em milimetros é {} '.format(m,c,mm));
