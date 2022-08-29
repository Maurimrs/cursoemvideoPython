from operator import mod


n1 = int(input('Digite o primeiro numero: '));
n2 = int(input('Digite o segundo numero: '));

soma = n1+n2;
sub = n1 - n2;
mult = n1 * n2;
div = float( n1 / n2);
pot = float(n1 ** n2);
divint = n1 // n2;
rest = float(n1 % n2);

print('A soma entre {} e {} é {}'.format(n1,n2,soma))
print('A subtração entre {} e {} é {}'.format(n1,n2,sub))
print('A multiplicação entre {} e {} é {}'.format(n1,n2,mult))
print('A divisão entre {} e {} é {}'.format(n1,n2,div))
print('A potenciação entre {} e {} é {}'.format(n1,n2,pot))
print('A divisão inteira entre {} e {} é {}'.format(n1,n2,divint))
print('O resto entre {} e {} é {}'.format(n1,n2,rest))