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



