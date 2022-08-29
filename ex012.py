#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
#com 5% de desconto.

preco = float(input('Insira o preço atual: '));

desconto = 0.05;

print('O preço com 5% de  desconto seria {}'.format(preco - preco * desconto ));

