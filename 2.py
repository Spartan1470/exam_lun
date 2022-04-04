name=[]
year=0
age=0
older_than_22=0
for i in range(2):
    
    year=int(input("ingresar el año de nacimiento del estudiante:"))
    name=(input("ingresar el nombre del estudiante:")) 
    age=2022-year
    print(f'la edad del estudiante {name} es:{age} años')
    if(age>22):
        older_than_22=older_than_22+1
print(f'los estudiantes mayores de 22 años son:{older_than_22}') 
