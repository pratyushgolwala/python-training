transactions = [
    {"amt": 120, "curr": "USD", "status": "Success"},
    {"amt": 250, "curr": "USD", "status": "Failed"},
    {"amt": 75,  "curr": "EUR", "status": "Success"},
    {"amt": 300, "curr": "USD", "status": "Success"},
    {"amt": 50,  "curr": "USD", "status": "Failed"},
    {"amt": 180, "curr": "EUR", "status": "Success"},
    {"amt": 40,  "curr": "USD", "status": "Failed"},
    {"amt": 500, "curr": "USD", "status": "Success"},
    {"amt": 90,  "curr": "EUR", "status": "Failed"},
    {"amt": 60,  "curr": "USD", "status": "Success"},
    {"amt": 220, "curr": "USD", "status": "Success"},
    {"amt": 130, "curr": "EUR", "status": "Failed"},
]

total_usd_success = 0
total_usd_failed = 0
for transaction in transactions:
    usd_amount = transaction["amt"]
    if transaction["curr"] == "EUR":
        usd_amount *= 1.1
    if transaction["status"] == "Success":
        total_usd_success += usd_amount
    else:
        total_usd_failed += usd_amount
total_dict = {
    "Success" : total_usd_success,
    "Failed" : total_usd_failed
}

print(total_dict)