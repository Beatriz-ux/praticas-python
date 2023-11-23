L = ["Macaco", "Galo", "Cão", "Porco", "Rato", "Boi", "Tigre", 
     "Coelho", "Dragão", "Serpente", "Cavalo", "Carneiro"]

ano_nascimento = int(input("Digite o ano de nascimento: "))

ano_chines = L[ano_nascimento % 12]
print(f"Você nasceu no ano chines do {ano_chines}.")