mercado=[]
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
        lista=input("añada un producto:")
        mercado.append(lista)

    elif(option==2):
            print(mercado)

    elif(option==3):
        print(mercado)
        cambiar_nombre=input("nombre del producto a cambiar:")
        carrito=False
        for i in range(0,len(mercado)):
            if(cambiar_nombre==mercado[i]):
                nuevo_nombre=input("Digite el nombre del nuevo producto:")
                mercado[i]=nuevo_nombre
                print(mercado) 
                carrito=True

    elif(option==4):
        print (mercado)
        eliminar_producto=input("Digite el producto a sacar del carro de compras:")
        for i in range(0,len(mercado)):
            if(eliminar_producto==mercado[i]):
                mercado.pop(i)  
        print(mercado)
    elif(option==5):
        print("compra finalizada!")
        break
    else:
        print("Error")

