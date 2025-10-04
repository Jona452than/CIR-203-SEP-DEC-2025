inventory = {"Laptop":12,"Mouse":25,"Keyboard":8,"Monitor":5,"Camcorder":30}
inventory["Headphones"] = 15
inventory["Keyboard"] = inventory.get("Keyboard",0) + 10
def low_stock_products(inv):
    return [k for k,v in inv.items() if v < 10]
low = low_stock_products(inventory)
inventory.pop("Camcorder", None)
for prod, qty in inventory.items():
    print(prod, qty)
