year=0
age=0
older_than_22=0
for i in range(10):
    year=int(input("ingresar el año de nacimiento del estudiante: "))
    age=2022-year
    print(f'su edad es {age}')
    if(age>22):
        older_than_22=older_than_22+1
print(f'los estudiantes mayores de 22 son :{older_than_22}') 