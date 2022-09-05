#Exercício Python 15: Escreva um programa que pergunte 
# a quantidade de Km percorridos por um carro alugado e 
# a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Insira a quantidade de KMs percorridos: '));
day = int(input('Insira a quantidade de dias utilizados: '));
custoDia = float(60.0);
custoKm = float(0.15);

totalPagar = km * custoKm + day * custoDia ;

print('Você rodou no total {:.2f} KMs por {:.2f} Dias, o valor diario é R${:.2f} e o custo por km R${:.2f}, \n no total voce vai pagar R${:.2f}'.format(km,day,custoDia,custoKm,totalPagar));
