digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print("número | ASCII | OCTA | HEXA")
# printando numeros e seus respectivos valores em ASCII
for i in digitos:
    ascci = ord(i)
    print(f" '{i}'  -   {ascci}  -  {oct(ascci)} - {hex(ascci)}")

# caracteres especiais
char_especial = ['ç', 'ã']
print("Caracteres Especiais: Usam codigo Unicode")
print("número | UNICODE | OCTA | HEXA")
for i in char_especial:
    ascci = ord(i)
    print(f" '{i}'  -   {ascci}  -  {oct(ascci)} - {hex(ascci)}")
    
