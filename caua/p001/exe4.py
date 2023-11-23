#Parte1
nome = "Cauã Clemente Lima";

#Parte2
primeiro_nome = nome.split(' ')[0]
print(primeiro_nome)

sobrenome = nome.split(' ')[1] + " " + nome.split(' ')[2]
print(sobrenome)

#Parte3
lista_nomes = [primeiro_nome, sobrenome];
lista_nomes.sort();
print("\nOrdem alfabetica: 1 - {}, 2 - {}".format(lista_nomes[0], lista_nomes[1]));

#Parte4
print("\nTamanho do nome: {}".format(len(primeiro_nome)));
print("Tamanho do sobrenome: {}".format(len(sobrenome)));

#Parte5
if(primeiro_nome.lower() == primeiro_nome[::-1].lower()):
    print("\nO primeiro nome e um palindromo")
else:
    print("\nO primeiro nome nao e um palindromo")    