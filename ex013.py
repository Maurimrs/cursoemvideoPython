#Faça um algoritmo que leia o salario de um funcionario
#e mostre seu novo salario com aumento de 15%

salario = float(input('Insira seu salario: '));
aumento = 0.15

salNovo = salario + salario * aumento;

print('O salario com aumento de 15% será de {}'.format(salNovo));

