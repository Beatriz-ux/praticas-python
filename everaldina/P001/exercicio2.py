a = 10
b = -3
c = 0

# operadores aritmeticos
print("Soma")
print(f"({a}) + ({b}) = {a + b}")
print(f"({a}) + ({c}) = {a + c}")
print(f"({b}) + ({c}) = {b + c}")

print("\nSubtração")
print(f"({a}) - ({b}) = {a - b}")
print(f"({a}) - ({c}) = {a - c}")
print(f"({b}) - ({c}) = {b - c}")
print(f"({b}) - ({a}) = {b - a}")
print(f"({c}) - ({b}) = {c - b}")
print(f"({c}) - ({a}) = {c - a}")

print("\nMultiplicação")
print(f"({a}) * ({b}) = {a * b}")
print(f"({a}) * ({c}) = {a * c}")
print(f"({b}) * ({c}) = {b * c}")

# Na divisão em python, entre dois inteiros resulta em um float
# Isso em C/C++ não acontece, o resultado é um inteiro, a nao ser
# que se pelo menos um dos operandos seja float
print("\nDivisão")
print(f"({a}) / ({b}) = {a / b}")
print(f"({b}) / ({a}) = {b / a}")
print(f"({c}) / ({b}) = {c / b}")
print(f"({c}) / ({a}) = {c / a}")

# O operador // é uma novidade do python em relação a C/C++
# Ele retorna a parte inteira da divisão, funciona de forma
# semelhante ao operador / em C/C++ entre dois inteiros
print("\nDivisão Inteira")
print(f"({a}) // ({b}) = {a // b}")
print(f"({b}) // ({a}) = {b // a}")
print(f"({c}) // ({b}) = {c // b}")
print(f"({c}) // ({a}) = {c // a}")

print("\nResto da Divisão")
print(f"({a}) % ({b}) = {a % b}")
print(f"({b}) % ({a}) = {b % a}")
print(f"({c}) % ({b}) = {c % b}")
print(f"({c}) % ({a}) = {c % a}")

# Não existe operador de potencia em C/C++
# Em python, o operador ** é o operador de potencia
print("\nPotencia")
print(f"({a}) ** ({b}) = {a ** b}")
print(f"({b}) ** ({a}) = {b ** a}")
print(f"({c}) ** ({a}) = {c ** a}")
print(f"({a}) ** ({c}) = {a ** c}")
print(f"({b}) ** ({c}) = {b ** c}")


# Operadores compostos
print("\nSoma e Atribuição")
print(f"({a}) += ({b}) = ", end="")
a += b
print(a)
print(f"({a}) += ({c}) = ", end="")
a += c
print(a)

print("\nSubtração e Atribuição")
print(f"({a}) -= ({b}) = ", end="")
a -= b
print(a)
print(f"({a}) -= ({c}) = ", end="")
a -= c

print("\nMultiplicação e Atribuição")
print(f"({a}) *= ({b}) = ", end="")
a *= b
print(a)

print("\nDivisão e Atribuição")
print(f"({a}) /= ({b}) = ", end="")
a /= b
print(a)

# Como o operador // não existe em C/C++, não existe o operador //= também
print("\nDivisão Inteira e Atribuição")
print(f"({a}) //= ({b}) = ", end="")
a //= b
print(a)

print("\nResto da Divisão e Atribuição")
print(f"({a}) %= ({b}) = ", end="")
a %= b
print(a)

# Como o operador ** não existe em C/C++, não existe o operador **= também
print("\nPotencia e Atribuição")
print(f"({a}) **= ({b}) =", end="")
a **= b
print(a)

# Os operadores de incremento e decremento não existem em python






