#Desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média.

n1 = float(input('Insira a nota 1: '));
n2 = float(input('Insira a nota 2: '));

media = (n1+n2)/2;

print('A média entre {} e {} é {}'.format(n1,n2,media));