import sys

# lista com numeros negativos, positivos, com e sem parte decimal
numeros = [0.0, 42.0, 3.14159, -42.0, -3.14159]

#Operadores Aritméticos
print("Soma")
for i in numeros:
    for j in range(-1, 4):
        print(f"({i}) + ({j}) = {i + j}")
print()

print("Subtração")
for i in numeros:
    for j in range(-1, 4):
        print(f"({i}) - ({j}) = {i - j}")
print()

print("Multiplicação")
for i in numeros:
    for j in range(-1, 4):
        print(f"({i}) * ({j}) = {i * j}")
print()
        
print("Divisão")
for i in numeros:
    for j in range(-1, 4):
        if j != 0:
            print(f"({i}) / ({j}) = {i / j}")
print()
  
print("Divisão Inteira")
for i in numeros:
    for j in range(-1, 4):
        if j != 0:
            print(f"({i}) // ({j}) = {i // j}")
print()

print("Potencia")
for i in numeros:
    for j in range(-1, 4):
        if i != 0:
            print(f"({i})^({j}) = {i ** j}")
print()

print("Negação")
for i in numeros:
    print(f"-({i}) = {-i}")
print()

a = 5
b = 2.0
c = 1.5
#Operadores compostos
print("\nSoma e Atribuição")
print(f"{a} += {b} = ", end="")
a += b 
print(a)
print(f"{a} += {c} = ", end="")
a += c 
print(a)


print("\nSubtração e Atribuição")
print(f"{a} -= {b} = ", end="")
a -= b 
print(a)
print(f"{a} -= {c} = ", end="")
a -= c 
print(a)

print("\nMultiplicação e Atribuição")
print(f"{a} *= {b} = ", end="")
a *= b 
print(a)
print(f"{a} *= {c} = ", end="")
a *= c 
print(a)

print("\nDivisão e Atribuição")
print(f"{a} /= {b} = ", end="")
a /= b 
print(a)
print(f"{a} /= {c} = ", end="")
a /= c 
print(a)

print("\nDivisão Inteira e Atribuição")
print(f"{a} //= {b} = ", end="")
a //= b 
print(a)
print(f"{a} //= {c} = ", end="")
a //= c 
print(a)

print("\nResto da Divisão e Atribuição")
print(f"{a} %= {b} = ", end="")
a %= b 
print(a)
print(f"{a} %= {c} = ", end="")
a %= c 
print(a)

print("\nPotencia e Atribuição")
print(f"{a} **= {b} =", end="")
a **= b 
print(a)
print(f"{a} **= {c} = ", end="")
a **= c 
print(a, end="")


# maior e menor potencia de dois em float
max_float =  sys.float_info.max
min_float = sys.float_info.min
exp_max = 0
exp_min = 0

while 2**exp_max <= max_float:
    exp_max += 1

while 2**exp_min >= min_float:
    exp_min -= 1
    
print(f"\n\nMaior potencia de 2 em float: 2^{exp_max}")
print(f"Menor potencia de 2 em float: 2^{exp_min}")


# imutabilidade numerica
a = 7
b = a

print(f"\n\na = {a}")
print(f"b = {b}")

a = 10

print(f"Atribuindo a = 10:")
print(f"a = {a}")
print(f"b = {b}")


# metodos float
print("\n\nMetodos float:")
print("float.as_integer_ratio: Retorna um par de inteiros cuja divisao é igual ao número de ponto flutuante.")
print(f"\tfloat.as_integer_ratio(3.14159) = {float.as_integer_ratio(3.14159)}")
print(f"\tfloat.as_integer_ratio(42.0) = {float.as_integer_ratio(42.0)}")
print("\nfloat.is_integer: Retorna verdadeiro se o número de ponto flutuante for um inteiro.")
print(f"\tfloat.is_integer(3.14159) = {float.is_integer(3.14159)}")
print(f"\tfloat.is_integer(42.0) = {float.is_integer(42.0)}")
print("\nfloat.hex: Retorna uma string hexadecimal representando o número de ponto flutuante.")
print(f"\tfloat.hex(3.14159) = {float.hex(3.14159)}")
print(f"\tfloat.hex(42.0) = {float.hex(42.0)}")
print("\nfloat.fromhex: Retorna o número de ponto flutuante representado por uma string hexadecimal.")
print(f"\tfloat.fromhex('0x1.921fb54442d18p+1') = {float.fromhex('0x1.921fb54442d18p+1')}")
print(f"\tfloat.fromhex('0x1.5000000000000p+5') = {float.fromhex('0x1.5000000000000p+5')}")

