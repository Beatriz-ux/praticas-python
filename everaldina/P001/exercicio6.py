L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L[::-1])
print(L[-1::])
print(L[:-1:])
print(L[::-2])
print(L[-2::])
print(L[:-2:])

L = ["Macaco", "Galo", "Cão", "Porco", "Rato", "Boi", "Tigre", 
     "Coelho", "Dragão", "Serpente", "Cavalo", "Carneiro"]

ano_nascimento = int(input("\nDigite o ano de nascimento: "))

ano_chines = L[ano_nascimento % 12]
print(f"Você nasceu no ano chines do {ano_chines}.")