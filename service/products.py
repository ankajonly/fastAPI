import json 
from pathlib import Path
from typing import Dict, List

DATA_FILE = Path(__file__).parent.parent / "data" / "products.json"

def load_products() -> List[Dict]:
    if not DATA_FILE.exists():
        return []
    
    with open(DATA_FILE, "r", encoding= "utf-8") as file:
        data = json.load(file)
        return data.get("products", [])
    

def get_all_products() -> List[Dict]:
    return load_products()

# def get_products_by_category(category: str) -> List[Dict]:
#     products = load_products()
#     return [product for product in products if product.get("category") == category]
