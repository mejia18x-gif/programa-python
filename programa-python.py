# =============================================
# PROGRAMA DE AUDITORÍA DE INVENTARIO
# =============================================

# En esta matriz se almacena la información del inventario.
# Cada fila representa un producto y contiene:
# [código, nombre del producto, stock actual, stock mínimo]
inventario = [
    [101, "Teclado", 5, 10],
    [102, "Mouse", 12, 8],
    [103, "Monitor", 3, 6],
    [104, "Impresora", 7, 7],
    [105, "USB", 2, 5]
]


# Función encargada de calcular cuántas unidades
# se deben pedir para completar el stock mínimo.
def calcular_pedido(stock_actual, stock_minimo):

    # Se verifica si la cantidad disponible
    # es menor que la cantidad mínima requerida.
    if stock_actual < stock_minimo:

        # Si falta inventario, se calcula la diferencia.
        return stock_minimo - stock_actual

    # Si el stock ya es suficiente,
    # no es necesario realizar pedidos.
    else:
        return 0


# Función que muestra en pantalla
# el reporte completo de pedidos.
def mostrar_pedidos(matriz):

    # Encabezado del reporte
    print("======================================")
    print("   LISTA DE PEDIDOS DE INVENTARIO")
    print("======================================")

    # Recorrer cada producto almacenado en la matriz
    for articulo in matriz:

        # Se extraen los datos de cada artículo
        # usando la posición correspondiente de la lista.
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        # Llamado a la función para calcular
        # la cantidad que se debe pedir.
        pedido = calcular_pedido(stock_actual, stock_minimo)

        # Mostrar la información organizada
        # de cada producto en consola.
        print("Código:", codigo)
        print("Artículo:", nombre)
        print("Stock Actual:", stock_actual)
        print("Stock Mínimo:", stock_minimo)
        print("Cantidad a Pedir:", pedido)

        # Línea separadora para mejorar la lectura
        # del reporte en pantalla.
        print("--------------------------------------")


# =============================================
# PROGRAMA PRINCIPAL
# =============================================

# Se ejecuta la función principal enviando
# la matriz del inventario como parámetro.
mostrar_pedidos(inventario)