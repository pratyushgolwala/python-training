products = {
    "p1": {"price": 70, "category":"electronics"},
    "p2": {"price": 90, "category":"fashion"},
    "p3": {"price": 40, "category":"electronics"}
}

updated = {
    k: {
        **v,
        "price":v["price"] * 0.85 if v["category"] == "electronics" and v["price"] > 50
        else v["price"] * 0.9 if v["category"] == "fashion" and v["price"] > 50
        else v["price"]
        
    }
    for k,v in products.items()
}

print(updated)