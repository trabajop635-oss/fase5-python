# Matriz con informacion de cinco articulos

Inventario =  [
    [ 111, "Computador", 1, 50],
    [ 112, "Cable HDMI", 30, 100],
    [ 113, "Disco duro", 100, 300],
    [ 114, "Teclado", 5, 50],
    [ 115, "Mouse", 2, 100]

]

# funcion (modulo)
resultados=[]
def calcular (Stock_actual, Stock_minimo):

    if Stock_actual < Stock_minimo:
        return Stock_minimo - Stock_actual
    else:
        return 0

# procedimiento para mostrar la lista de pedidos 

def mostrar_pedidos (lista):
    print("="* 50)
    print("lista de pedidos_reabastecimiento")
    print("="* 50)

    for pedido in lista:
        print (f"{pedido [0]}-cantidad a pedir:{pedido [1]}")

print("="* 50)    
                  

# recorrer la matriz

for fila in Inventario:

    nombre = fila [1] 
    Stock_actual = fila [2]
    Stock_minimo = fila [3]

    cantidad = calcular (Stock_actual, Stock_minimo)

    resultados . append ([ nombre, cantidad ])

# imprimir lista de pedidos

mostrar_pedidos (resultados)