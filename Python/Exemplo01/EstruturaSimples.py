A = input("Insira o nome do A: ")
B = input("Insira o nome do B: ")

if(A>B):
    aux = A;
    A=B;
    B=aux;

print("O VAlor da Variavel A agora é:", A);
print("O valor de B agora é:", B);
