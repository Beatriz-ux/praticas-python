#Parte1-2
for i in range(10):
    x = str(i);
    print("'{}' - {} - {} - {}".format(x, ord(x), oct(ord(x)), hex(ord(x))));

#Parte3
x = input("\nDigite um caractere qualquer: ");
print("'{}' - {} - {} - {}".format(x, ord(x), oct(ord(x)), hex(ord(x))));

#Parte4
print("\nImprimindo caracteres especiais: ç, ã, á, ô");
x = input("Insira um caractere especial: ");
print(x);
#python tem mais liberdade quanto a caracteres