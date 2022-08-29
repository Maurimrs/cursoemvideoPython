# crie um programa que leia quanto dinheiro uma pessoa tem na carteira,
# e mostre quantos dolares ela poderia comprar.
# considere a cotação de  US$ 1,00 = R$ 3.27


carteira = float(input('Quantos Reais voce tem na carteira? '));
cotacao = 3.27

print('Voce teria em dolares o valor de {}'.format(carteira / cotacao));
