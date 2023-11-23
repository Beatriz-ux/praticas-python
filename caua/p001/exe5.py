#Parte1
x = 4.0;
x += 2;
x -= 2;
x *= 2;
x /= 4;
print(x);

y = 3;
x = x + y;
print(x);
x = x ** (y - 1);
print(x);
x = x * 4;
x = x / 50;
print(x);

#Parte2
print(10.0**308);
print(10.0**(-323));

#Parte3
x = 2.0;
y = x;
print("\nx = {} - y = {} ".format(x, y));

x = x * 2;
print("\nx = {} - y = {} ".format(x, y));

y = x;
print("\nx = {} - y = {} ".format(x, y));

#Parte4
print("\nAlgumas funcoes de float: ");
print("{} E inteiro? {}".format(x, x.is_integer()))

x = 4.0000000001;
print("{} E inteiro? {}".format(x, x.is_integer()))

import math;
x = 4.5;
print("{} arredondado pra cima (={}) e pra baixo (={})\n".format(x, math.ceil(x), math.floor(x)))
