from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Importa la clase CRUD_PRODUCTOS del archivo donde está definido
from product import CRUD_PRODUCTOS

app = FastAPI()
crud = CRUD_PRODUCTOS()

# Modelo Pydantic para la creación y actualización de productos
class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float

class ProductoResponse(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str] = None
    precio: float

class ProductoDeleteResponse(BaseModel):
    status: str
    message: str

# Endpoints

@app.post("/productos", response_model=ProductoResponse)
def create_producto(producto: ProductoBase):
    resultado = crud.create_producto(producto.nombre, producto.descripcion, producto.precio)
    return resultado["Object"]

@app.get("/productos", response_model=List[ProductoResponse])
def read_productos():
    productos = crud.read_productos()
    return [
        {"id": p.ID, "nombre": p.NOMBRE, "descripcion": p.DESCRIPCION, "precio": p.PRECIO}
        for p in productos
    ]

@app.get("/productos/{producto_id}", response_model=ProductoResponse)
def read_producto_id(producto_id: int):
    producto = crud.read_productos_id(producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail=f"Producto con ID {producto_id} no encontrado.")
    return {
        "id": producto.ID,
        "nombre": producto.NOMBRE,
        "descripcion": producto.DESCRIPCION,
        "precio": producto.PRECIO,
    }

@app.put("/productos/{producto_id}", response_model=ProductoResponse)
def update_producto(producto_id: int, producto: ProductoBase):
    actualizado = crud.update_producto(
        producto_id, nombre=producto.nombre, descripcion=producto.descripcion, precio=producto.precio
    )
    if not actualizado:
        raise HTTPException(status_code=404, detail=f"Producto con ID {producto_id} no encontrado.")
    return {
        "id": actualizado.ID,
        "nombre": actualizado.NOMBRE,
        "descripcion": actualizado.DESCRIPCION,
        "precio": actualizado.PRECIO,
    }

@app.delete("/productos/{producto_id}", response_model=ProductoDeleteResponse)
def delete_producto(producto_id: int):
    resultado = crud.delete_producto(producto_id)
    if resultado["Status"] != "True":
        raise HTTPException(status_code=404, detail=f"Producto con ID {producto_id} no encontrado.")
    return {
        "status": "True",
        "message": resultado["Message"],
    }
