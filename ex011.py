#Faça um programa que leia a largura e a altura de uma parede em metros.
#Calcule a sua area e a quantidade de tinta necessaria para pinta-la.
#cada litro de tinta pinta uma area de 2 m².

lm = int(input('Insira a largura em metros: '));
am = int(input('Insira a altura em metros: '));

area = lm * am;

rend2 = 2;

print('Sua area é de {}m², é necessario {} litros de tinta'.format(area,area/rend2));
