stores = {
    "1":
        {
            "name": "Store 1",
            "address": "Delhi",
            "store_id": 1
        },
    "2":
        {
            "name": "Store 2",
            "address": "Mumbai",
            "store_id": 2
        }
}


items = {
    "1":
        {
            "name": "Laptop",
            "price": 1999,
            "store_id": 1,
            "item_id": 1
        },
    "2":
        {
            "name": "Charger",
            "price": 199,
            "store_id": 2
        }
}


result = stores.values()
print(result)