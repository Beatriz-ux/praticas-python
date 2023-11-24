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
print(a)

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


# Limite dos inteiros
print("\n\nLimite dos inteiros")
fat = 1
for i in range(1, 31):
    fat *= i
print(f'30! = {fat}')
# Resultado em Python 30! = 265252859812191058636308480000000
# Limite em c/c++ (long long int) = 9223372036854775807
# Limite em c/c++ (unsigned long long int) = 18446744073709551615
# Com os tipos nativos inteiros de C/C++ não é possível representar o valor de 30!

# Variaveis imutaveis
print("\n\nVariaveis imutaveis")
a = 5
b = a
print(f"\na = {a}, b = {b}")

a = 10

print(f"a = 10 ==> a = {a}, b = {b}")

# Metodos int
print("\n\nMetodos int")
print("int.bit_length(): Retorna o número de bits necessários para representar o inteiro em binário")
print(f"\tint.bit_length({a}) = {a.bit_length()}")
print("\nint.bit_count(): Retorna o número de bits 1 necessários para representar o inteiro em binário")
print(f"\tint.bit_count({a}) = {a.bit_count()}")
print("\nint.to_bytes(): Retorna um array de bytes representando o inteiro")
print(f"\tint.to_bytes({a}, byteorder='big') = {a.to_bytes(a.bit_length(), byteorder='big')}")
print(f"\tint.to_bytes({a}, byteorder='little') = {a.to_bytes(a.bit_length(), byteorder='little')}")
print("\nint.from_bytes(): Retorna um inteiro a partir de um array de bytes")
print(f"\tint.from_bytes({a.to_bytes(a.bit_length(), byteorder='big')}, byteorder='big') = {int.from_bytes(a.to_bytes(a.bit_length(), byteorder='big'), byteorder='big')}")
print(f"\tint.from_bytes({a.to_bytes(a.bit_length(), byteorder='little')}, byteorder='little') = {int.from_bytes(a.to_bytes(a.bit_length(), byteorder='little'), byteorder='little')}")
print("\nint.as_integer_ratio: Retorna um par de inteiros cuja divisao é igual ao número inteiro.")
print(f"\tint.as_integer_ratio({a}) = {a.as_integer_ratio()}")
print("\n\nOutros metodos e atributos do tipo int podem ser visualizados chamando a funcao dir(int).")
print(f'\t{dir(int)}')





