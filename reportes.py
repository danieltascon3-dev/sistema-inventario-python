import sqlite3

conn = sqlite3.connect('inventario.db')
cursor = conn.cursor()

# Reporte 1
cursor.execute("SELECT productos.nombre,productos.categoria,SUM(ventas.cantidad),SUM(ventas.total) FROM productos "
               "INNER JOIN ventas ON productos.id = ventas.producto_id "
               "GROUP BY productos.id,productos.nombre,productos.categoria "
               "ORDER BY SUM(ventas.cantidad) DESC LIMIT 5")
for fila in cursor.fetchall():
    print(fila)  # ← Solo MUESTRA en pantalla

# Reporte 2
print("reporte 2")
cursor.execute("SELECT clientes.nombre, clientes.ciudad, SUM(ventas.total),COUNT(Ventas.id) FROM clientes "
               "INNER JOIN ventas ON clientes.id = ventas.cliente_id GROUP BY clientes.nombre, clientes.ciudad "
               "HAVING SUM(ventas.total) > 5000 ORDER BY SUM(ventas.total) DESC")
for fila in cursor.fetchall():
    print(fila)

#reporte 3
print("reporte 3")
cursor.execute("SELECT Productos.nombre,Productos.stock,SUM(Ventas.cantidad),"
               "CASE "
               "WHEN Productos.stock < 10 THEN 'Urgente'"
               "WHEN Productos.stock < 20 THEN 'Bajo'"
               "ELSE 'OK'"
               "END AS estado_stock "
               "FROM Productos INNER JOIN ventas ON Productos.id = Ventas.producto_id "
               "WHERE productos.stock < 20 "
               "GROUP BY Productos.id,Productos.nombre,Productos.stock "
               "ORDER BY Productos.stock ASC")
for i in cursor.fetchall():
    print(i)
print("reporte 4")
cursor.execute("""SELECT Clientes.ciudad,COUNT(Clientes.ID),SUM(Ventas.total),SUM(Ventas.total) / COUNT(DISTINCT Clientes.id)
FROM Clientes INNER JOIN Ventas ON Clientes.ID = Ventas.cliente_id
GROUP BY Clientes.ciudad
ORDER BY SUM(Ventas.total) DESC""")
for i in cursor.fetchall():
    print(i)
conn.close()