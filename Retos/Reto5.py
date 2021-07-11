productos = ["tomate","cebolla","arroz","lentejas","zanahoria","manzana","mandarina","carne","pescado"]
grupoProductos = ["verduras","verduras","granos","granos","verduras","frutas","frutas","carnes","carnes"]

def grupos (lista): 
    elemento_lista = []
    for i in lista:
        if i in elemento_lista:
            continue
        else:
            elemento_lista.append(i)
    return elemento_lista
print (grupos(grupoProductos))

""" [0,1,3,6,8] -> Son los índices de cada producto en la lista de productos
[“verduras”,”verduras”,”granos”,”granos”,”verduras”,”frutas”,”frutas”,”carnes”,”carnes”] -> Lista de grupos
“verduras” -> El grupo que interesa
Retorna:
[0,1,4] -> Se necesitan los productos que están en la posición 0,1 y 4 de la lista de productos que pertenecen
 al grupo “verduras” """

def necesito_del_grupo (list_indices,list_grupos,grupo):

