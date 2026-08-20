class InventoryManagement:

    def __init__(self):
        self.warehouses = {
            "A": {},
            "B": {},
            "C": {}
        }

        self.suppliers = {}
        self.reorder_threshold = 10

    def add_product(self, warehouse, product, quantity):
        if warehouse not in self.warehouses:
            print("Invalid warehouse")
            return

        if quantity < 0:
            print("Negative inventory not allowed")
            return

        self.warehouses[warehouse][product] = \
            self.warehouses[warehouse].get(product, 0) + quantity

        print("Product added successfully")

    def remove_product(self, warehouse, product, quantity):
        if warehouse not in self.warehouses:
            print("Invalid warehouse")
            return

        if product not in self.warehouses[warehouse]:
            print("Invalid product")
            return

        if quantity < 0:
            print("Negative quantity not allowed")
            return

        if self.warehouses[warehouse][product] < quantity:
            print("Insufficient inventory")
            return

        self.warehouses[warehouse][product] -= quantity
        print("Product removed successfully")

    def transfer_stock(self, source, destination, product, quantity):
        if source not in self.warehouses or destination not in self.warehouses:
            print("Invalid warehouse")
            return

        if product not in self.warehouses[source]:
            print("Invalid product")
            return

        if quantity <= 0:
            print("Invalid quantity")
            return

        if self.warehouses[source][product] < quantity:
            print("Insufficient inventory")
            return

        self.warehouses[source][product] -= quantity
        self.warehouses[destination][product] = \
            self.warehouses[destination].get(product, 0) + quantity

        print("Stock transferred successfully")

    def reorder(self, warehouse, product, quantity):
        if warehouse not in self.warehouses:
            print("Invalid warehouse")
            return

        if product not in self.warehouses[warehouse]:
            print("Invalid product")
            return

        if self.warehouses[warehouse][product] <= self.reorder_threshold:
            self.warehouses[warehouse][product] += quantity
            print("Reorder completed")
        else:
            print("Reorder not required")

    def add_supplier(self, supplier_id, supplier_name):
        self.suppliers[supplier_id] = supplier_name
        print("Supplier added successfully")

    def low_stock(self, warehouse):
        if warehouse not in self.warehouses:
            print("Invalid warehouse")
            return

        result = {}

        for product, quantity in self.warehouses[warehouse].items():
            if quantity <= self.reorder_threshold:
                result[product] = quantity

        return result

    def select_warehouse(self, product, quantity):
        for warehouse in ["A", "B", "C"]:
            available = self.warehouses[warehouse].get(product, 0)

            if available >= quantity:
                print("Order fulfilled from Warehouse", warehouse)
                return warehouse

        print("No warehouse has sufficient stock")
        return None


inventory = InventoryManagement()

inventory.add_product("A", "Laptop", 50)
inventory.add_product("B", "Laptop", 20)
inventory.add_product("C", "Laptop", 5)

inventory.add_product("A", "Keyboard", 15)

inventory.add_supplier("S01", "ABC Suppliers")

inventory.remove_product("A", "Keyboard", 5)

inventory.transfer_stock("A", "B", "Laptop", 10)

inventory.reorder("C", "Laptop", 20)

print("Low stock:", inventory.low_stock("C"))

inventory.select_warehouse("Laptop", 15)
