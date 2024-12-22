import requests

BASE_URL = "http://127.0.0.1:8000"  # Cambiar la URL si tu servidor está en otro lugar

def create_producto(nombre, descripcion, precio):
    url = f"{BASE_URL}/productos"
    data = {
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Producto creado exitosamente:", response.json())
    else:
        print("Error al crear producto:", response.status_code, response.text)
    return response.json()

def get_productos():
    url = f"{BASE_URL}/productos"
    response = requests.get(url)
    if response.status_code == 200:
        productos = response.json()
        print("Lista de productos:")
        for producto in productos:
            print(producto)
    else:
        print("Error al obtener productos:", response.status_code, response.text)
    return response.json()

def get_producto_by_id(producto_id):
    url = f"{BASE_URL}/productos/{producto_id}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Producto encontrado:", response.json())
    else:
        print("Error al obtener producto:", response.status_code, response.text)
    return response.json()

def update_producto(producto_id, nombre=None, descripcion=None, precio=None):
    url = f"{BASE_URL}/productos/{producto_id}"
    data = {
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
    }
    response = requests.put(url, json=data)
    if response.status_code == 200:
        print("Producto actualizado exitosamente:", response.json())
    else:
        print("Error al actualizar producto:", response.status_code, response.text)
    return response.json()

def delete_producto(producto_id):
    url = f"{BASE_URL}/productos/{producto_id}"
    response = requests.delete(url)
    if response.status_code == 200:
        print("Producto eliminado exitosamente:", response.json())
    else:
        print("Error al eliminar producto:", response.status_code, response.text)
    return response.json()


"""Uso del las funciones"""

# Crear un producto
create_producto("Producto nuevo", "Descripción del Producto1", 10.0)

# Listar todos los productos
get_productos()

# Obtener un producto por ID
get_producto_by_id(1)

# Actualizar un producto
update_producto(1, nombre="Producto Actualizado", descripcion="Nueva descripción", precio=12.5)

# Eliminar un producto
delete_producto(1)
