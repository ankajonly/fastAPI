from fastapi import FastAPI, HTTPException
from service.products import get_all_products


app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Hello, World!",
        "status": "success"
    }

# with open("data/products.json", "r", encoding="utf-8") as f:
#     data = json.load(f)
#     products = {product["id"]: product for product in data["products"]}


@app.get("/products")
def get_products():
    return get_all_products()




# @app.get("/products/category/{category}")
# def get_products_category(category: str):
#     products = get_products_by_category(category)
#     if not products:
#         raise HTTPException(status_code=404, detail="No products found in this category")
#     return products


# @app.get("/products/{product_id}")
# def get_product(product_id: int):
    
#     product = products.get(product_id)
#     if product:
#         return {
#             "product_id": product_id,
#             "details": product,
#             "status": "success",
#             "message": "Product found"
#         }
#     else:
#         raise HTTPException(status_code=404, detail="Product not found")

# @app.get("/products/allCategories")
# def get_all_categories():
#     categories = set(product["category"] for product in products.values())
#     return {
#         "categories": list(categories),
#         "status": "success",
#         "message": f"Found {len(categories)} unique categories"
#     }

# @app.get("/products/fashion")
# def get_fashion_products():
#     fashion_products = [product for product in products.values() if product["category"] == "Fashion"]
#     return {
#         "products": fashion_products,
#         "status": "success",
#         "message": f"Found {len(fashion_products)} fashion products"
#     }

# @app.get("/products/electronics")
# def get_electronics_products():
#     electronics_products = [product for product in products.values() if product["category"] == "Electronics"]
#     return {
#         "products": electronics_products,
#         "status": "success",
#         "message": f"Found {len(electronics_products)} electronics products"
#     }

# @app.get("/products/home")
# def get_home_products():
#     home_products = [product for product in products.values() if product["category"] == "Home"]
#     return {
#         "products": home_products,
#         "status": "success",
#         "message": f"Found {len(home_products)} home products"
#     }

# @app.get("/products/grocery")
# def get_grocery_products():
#     grocery_products = [product for product in products.values() if product["category"] == "Grocery"]
#     return {
#         "products": grocery_products,
#         "status": "success",
#         "message": f"Found {len(grocery_products)} grocery products"
#     }