#faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informaçoes possiveis sobre ele.

algo = input('Digite algo ');
print('O tipo primitivo é: ' ,type(algo));
print('Só tem espaços?', algo.isspace());
print ('É alfabetico?', algo.isalpha());
print( 'É alfanumerico', algo.isalnum());
print ('Esta em maiusculo?' , algo.isupper());
print ('Está em minusculo',algo.islower());
print ('É decimal? ',algo.isdecimal());
print ('É capitalizado?' , algo.istitle());
