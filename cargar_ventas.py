import sqlite3
import csv

conn = sqlite3.connect('inventario.db')
cursor = conn.cursor()

try:
    cursor.execute("BEGIN TRANSACTION")

    with open('nuevas_ventas.csv', 'r') as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            producto_id = int(fila['producto_id'])
            cliente_id = int(fila['cliente_id'])
            cantidad = int(fila['cantidad'])
            fecha = fila['fecha']

            # 1. Buscar el precio del producto
            cursor.execute("SELECT precio,Stock FROM Productos WHERE id = ?", (producto_id,))
            resultado = cursor.fetchone()
            if resultado == None:
                print("no se encontro dicho producto")
            else:
                precio = resultado[0]
                stock = resultado[1]
                # 2. Calcular total
                precio_total = cantidad * precio
                # 3. Insertar venta
                cursor.execute("INSERT INTO Ventas (Producto_id,Cliente_id,Cantidad,Fecha,Total) VALUES (?,?,?,?,?)",(producto_id,cliente_id,cantidad,fecha,precio_total,))
                # 4. Actualizar stock
                cursor.execute("UPDATE Productos SET Stock = Stock - ? WHERE ID = ?",(cantidad,producto_id))

    cursor.execute("COMMIT")
    print("Ventas cargadas exitosamente")

except Exception as e:
    cursor.execute("ROLLBACK")
    print(f"✗ Error: {e}")

finally:
    conn.close()