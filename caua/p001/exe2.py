#Parte1
x = 10;
y = 4;

print("Python possui mais operadores compostos do que c++, sendo \nalguns desses 'novos' operadores '//=' e '**='  ");

print(x + y); #Soma
print(x - y); #Subtracao
print(x * y); #Multiplicacao
print(x // y); #Divisao inteira
print(x / y); #Divisao
print(x % y); #Mod / Resto
print(x ** y); #Exponenciacao

print("Utilizando Operadores compostos para alterar o valor de x: ");

y = x;
x+=2
print(y, "+= 2 =", x);

y = x;
x-=2
print(y, "-= 2 =", x);

y = x;
x*=2
print(y, "*= 2 =", x);

y = x;
x//=2
print(y, "//= 2 =", x);

y = x;
x%=2
print(y, "%= 2 =", x);

y = x;
x**=0
print(y, "**= 0 =", x);


#Parte2
x = 1;
for i in range(30):
    x*= (i+1)

print("\nFatorial de 30: ");
print(x);
print("Maior numero inteiro no c++ (ULLONG_MAX):")
print(18446744073709551615);

#Parte3
print("\nAs variaveis numericas sao imutavies pois ao incrementar um valor a uma variavel,\nnao se altera o valor que estava dentro da variavel, mas um novo ponteiro e estabelecido para\narmazenar o novo valor");

x = 50;
print(x);

y = x;
print(y);

x *=2;
print(x);
print(y);

y = x;
print(y);

#Parte4 
'''
Em python, ha diversas funcoes nao so para ints como para variaveis numericas no geral.
Sao muitas, ao ponto que nao da para listar todas. Segue um exemplo, usando .__sizeof__:
'''

print("\n(x.__sizeof__) imprime:", x.__sizeof__, "\n");