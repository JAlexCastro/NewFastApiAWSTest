"""
Punto de entrada para la aplicación FastAPI, incluye las rutas desde route_product.

"""

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de SQLAlchemy
Base = declarative_base()
DATABASE_URL = "sqlite:///mi_db.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Modelo de la tabla Productos
class Producto(Base):
    __tablename__ = "productos"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    NOMBRE = Column(String, nullable=False)
    DESCRIPCION = Column(String)
    PRECIO = Column(Float, nullable=False)

# Funciones CRUD para la tabla Productos
class CRUD_PRODUCTOS:
    def __init__(self):
        pass

    def create_producto(self, nombre, descripcion, precio):
        nuevo_producto = Producto(NOMBRE=nombre, DESCRIPCION=descripcion, PRECIO=precio)
        session.add(nuevo_producto)
        session.commit()
        session.refresh(nuevo_producto)  # Actualiza el objeto con los valores de la base de datos
        print(f"Producto '{nombre}' creado exitosamente.")

        return {
            "Status": True,
            "Message": "Producto creado",
            "Object": {
                "id": nuevo_producto.ID,
                "nombre": nuevo_producto.NOMBRE,
                "descripcion": nuevo_producto.DESCRIPCION,
                "precio": nuevo_producto.PRECIO,
            },
        }

    def read_productos_id(self, n_id):
        # Usar filter en lugar de filter_by y aplicar la expresión correcta
        producto = session.query(Producto).filter(Producto.ID == n_id).first()
        
        if producto:
            print(f"ID: {producto.ID}, Nombre: {producto.NOMBRE}, Descripción: {producto.DESCRIPCION}, Precio: {producto.PRECIO}")
            return producto
        else:
            print(f"Producto con ID {n_id} no encontrado.")
            return None
    
    def read_productos(self):
        productos = session.query(Producto).all()
        for producto in productos:
            print(f"ID: {producto.ID}, Nombre: {producto.NOMBRE}, Descripción: {producto.DESCRIPCION}, Precio: {producto.PRECIO}")
        return productos

    def update_producto(self, producto_id, nombre=None, descripcion=None, precio=None):
        producto = session.query(Producto).filter(Producto.ID == producto_id).first()
        if producto:
            if nombre:
                producto.NOMBRE = nombre
            if descripcion:
                producto.DESCRIPCION = descripcion
            if precio:
                producto.PRECIO = precio
            session.commit()
            print(f"Producto ID {producto_id} actualizado exitosamente.")
        else:
            print(f"Producto ID {producto_id} no encontrado.")
        return producto

    def delete_producto(self, producto_id):
        producto = session.query(Producto).filter(Producto.ID == producto_id).first()
        if producto:
            session.delete(producto)
            session.commit()
            print(f"Producto ID {producto_id} eliminado exitosamente.")
        else:
            print(f"Producto ID {producto_id} no encontrado.")
        
        return {"Status":"True", "Message":"Producto eliminado exitosamente"}


obj = CRUD_PRODUCTOS()
obj.read_productos()


