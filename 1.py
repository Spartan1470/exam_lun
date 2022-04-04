negatives=0
multiple2=0
multiple3=0
Number=0
n=0
i=0
n=int(input("cantidad de de numeros?"))
for i in range (n):
    Number=int(input("ingrese numero: "))
    if(Number % 2==0):
        multiple2=multiple2+1
    if(Number % 3==0):
        multiple3=multiple3+1
    if(Number<0):
        negatives=negatives+1
    if(Number% 2==0 and Number% 3==0):
        multiple2=multiple2+1
        multiple3=multiple3+1
print(f'multiplos de 2:{multiple2}')
print(f'multiplos de 3:{multiple3}')
print(f'negativos: {negatives}')