import sqlite3

conectar  = sqlite3.connect("inventario.db")
cursor = conectar.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

try:
    cursor.execute("""CREATE TABLE IF NOT EXISTS Productos (ID INTEGER PRIMARY KEY AUTOINCREMENT,Nombre TEXT ,
    Categoria TEXT,Precio REAL CHECK(Precio>=0),Stock INTEGER)""")

    productos = [
        ( "Laptop Pro 14", "Tecnología", 1200, 15),
        ( "Zapatillas Runner X", "Calzado", 85, 50),
        ( "Café Premium 1kg", "Alimentos", 12, 120),
        ( "Silla Ergonómica", "Muebles", 210, 25),
        ( "Auriculares Inalámbricos", "Electrónica", 65, 40)
    ]

    cursor.executemany('INSERT INTO Productos (Nombre,Categoria,Precio,Stock) VALUES (?,?,?,?)', productos)

    cursor.execute("""CREATE TABLE IF NOT EXISTS Clientes (ID INTEGER PRIMARY KEY AUTOINCREMENT, Nombre TEXT, Email TEXT,Ciudad TEXT)""")

    clientes = [
        ("María González", "maria.gonzalez@example.com", "Buenos Aires"),
        ("Juan Pérez", "juan.perez@example.com", "Córdoba"),
        ("Lucía Fernández", "lucia.fernandez@example.com", "Rosario"),
        ("Carlos López", "carlos.lopez@example.com", "Mendoza"),
        ("Ana Martínez", "ana.martinez@example.com", "La Plata")
    ]

    cursor.executemany("""INSERT INTO Clientes (Nombre,Email,Ciudad) VALUES (?,?,?)""",clientes)

    cursor.execute("""CREATE TABLE IF NOT EXISTS Ventas (ID INTEGER PRIMARY KEY AUTOINCREMENT, Producto_id INTEGER,Cliente_id INTEGER,
    Cantidad INTEGER,Fecha TEXT,Total INTEGER,FOREIGN KEY (Producto_id) REFERENCES Productos(ID),FOREIGN KEY (Cliente_id) REFERENCES Clientes(ID))""")

    ventas = [
        (1, 2, 1, "2026-01-05", 1200),
        (3, 1, 3, "2026-01-06", 36),
        (5, 4, 2, "2026-01-07", 130),
        (2, 3, 1, "2026-01-08", 85),
        (4, 5, 1, "2026-01-09", 210),
        (1, 1, 2, "2026-01-10", 2400),
        (3, 2, 5, "2026-01-11", 60),
        (5, 3, 1, "2026-01-12", 65),
        (2, 4, 2, "2026-01-13", 170),
        (4, 1, 1, "2026-01-14", 210),
        (1, 5, 1, "2026-01-15", 1200),
        (3, 4, 2, "2026-01-16", 24),
        (5, 2, 3, "2026-01-17", 195),
        (2, 5, 1, "2026-01-18", 85),
        (4, 3, 2, "2026-01-19", 420)
    ]

    cursor.executemany("""INSERT INTO Ventas (Producto_id,Cliente_id,Cantidad,Fecha,Total) VALUES (?,?,?,?,?)""",ventas)
    conectar.commit()
    print("¡Cambios guardados en el disco!")
except sqlite3.Error as e:
    print(f"hay un error {e} en la base de datos inventario.db")
else:
    print("se creo la base de datos correctamente")
finally:
    conectar.close()