from IM import InventoryManagement


inventory = InventoryManagement()

# Stock availability
inventory.add_product("A", "Laptop", 50)
print("Stock availability:", inventory.warehouses["A"]["Laptop"])

# Insufficient inventory
inventory.remove_product("A", "Laptop", 100)

# Warehouse transfer
inventory.transfer_stock("A", "B", "Laptop", 10)

# Concurrent orders simulation
inventory.remove_product("A", "Laptop", 5)
inventory.remove_product("A", "Laptop", 5)

# Reorder threshold
inventory.add_product("C", "Mouse", 5)
inventory.reorder("C", "Mouse", 20)

# Invalid product
inventory.remove_product("A", "Mobile", 2)

# Negative inventory
inventory.add_product("A", "Keyboard", -5)

# Multiple warehouses
inventory.add_product("B", "Keyboard", 30)
inventory.add_product("C", "Keyboard", 20)

inventory.select_warehouse("Keyboard", 15)

print("Inventory QA completed")
