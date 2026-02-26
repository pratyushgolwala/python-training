ships = [
    {
        "containers": [
            {
                "items": [
                    {"name": "Glass", "fragile": True, "dest": "LON", "weight": 12},
                    {"name": "Steel", "fragile": False, "dest": "NYC", "weight": 30}
                ]
            }
        ]
    }
]

result = [
    item 
    for ship in ships
    for container in ship["containers"]
    for item in container["items"]
    if item["fragile"] and item["weight"] > 10 and item["dest"] == "LON"]


print(result)