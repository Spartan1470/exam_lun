products=[]
while(True):
    print("supermercado")
    print("***************")
    print("1->para registrar el nombre de un producto.")
    print("2->para mostrar todos los productos registrados.")
    print("3->para permitir buscar un producto y cambiar el nombre de este.")
    print("4->para permitir buscar por nombre un producto y eliminar el producto.")
    print("5->para finalizar compra.")
    print("***************")
    option=int(input("ingrese una option:"))
    
    if(option==1):
        lista=input("registre un producto:")
        products.append(lista)

    elif(option==2):
            print(products)

    elif(option==3):
        print(products)
        cambiar_nombre=input("nombre del producto a cambiar:")
        mercado=False
        for i in range(0,len(products)):
            if(cambiar_nombre==products[i]):
                nuevo_nombre=input("Digite el nombre del nuevo producto:")
                products[i]=nuevo_nombre
                print(products) 
                mercado=True

    elif(option==4):
        print (products)
        eliminar_producto=input("Digite el producto a sacar del carro de compras:")
        for i in range(0,len(products)):
            if(eliminar_producto==products[i]):
                products.pop(i)  
        print(products)
    elif(option==5):
        print("compra finalizada!")
        break
    else:
        print("Error")

