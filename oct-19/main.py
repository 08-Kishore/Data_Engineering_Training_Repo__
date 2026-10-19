from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float

products = []

@app.get("/")
def home():
    return {"Message": "API is running"}

@app.get("/products")
def get_products():
    return products

@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return {
        "message": "Product created",
        "products": products
    }

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

# Update a product by ID
@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            deleted = products.pop(index)
            return {"Message": "Product deleted", "Product": deleted}
    raise HTTPException(status_code=404, detail="Product not found")