'''
L = [1, 2, 3, 4, 5, 6, 7, 8, 9];
print("L[::-1] = {}".format(L[::-1]));
print("L[-1::] = {}".format(L[-1::]));
print("L[:-1:] = {}".format(L[:-1:]));
print("L[::-2] = {}".format(L[::-2]));
print("L[-2::] = {}".format(L[-2::]));
print("L[:-2:] = {}".format(L[:-2:]));
'''

idade = int(input("Digite o ano de seu nascimento: "));
print("Seu simbolo do zodiaco chines e: ");
match idade%12:
    case 0: 
        print("Macaco");
    case 1: 
        print("Galo");
    case 2: 
        print("Cão");
    case 3: 
        print("Porco");
    case 4: 
        print("Rato");
    case 5: 
        print("Boi");
    case 6: 
        print("Tigre");
    case 7: 
        print("Coelho");
    case 8: 
        print("Dragão");
    case 9: 
        print("Serpente");
    case 10: 
        print("Cavalo");
    case 11: 
        print("Caneiro");
