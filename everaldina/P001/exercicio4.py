nome_completo = "Everaldina Guimarães Barbosa"

nome, sobrenome = nome_completo.split(" ", 1)
print("Nome Completo: ", nome_completo)
print("Nome:", nome, " | Sobrenome:", sobrenome)
print("Tamanho do Nome:", len(nome), " | Tamanho do Sobrenome:", len(sobrenome))

if(nome < sobrenome):
    print("Alfabeticamente o 'Nome' vem antes do 'Sobrenome'")
else:
    print("Alfabeticamente o 'Sobrenome' vem antes do 'Nome'")
    
nome_reverso = nome[::-1]
if(nome.lower() == nome_reverso.lower()):
    print("O 'Nome' é um palíndromo")
else:
    print("O 'Nome' não é um palíndromo")

print('a' > 'A')