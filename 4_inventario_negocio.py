class Inventory:
                       def __init__(self):
                           self.groups = {
                               'dairy': [],
                               'cleaning': [],
                               'grain': []
                           }
                           self.stock = {
                               'dairy': [],
                               'cleaning': [],
                               'grain': []
                           }
                       def add_product(self, name, quantity, group):
                              if group not in self.groups:
                                    print("El grupo '{group}' no es válido.")
                                    return
                              if name in self.groups[group]:
                                    index = self.groups[group].index(name)
                                    self.stock[group][index] += quantity
                              else:
                                    self.groups[group].append(name)
                                    self.stock[group].append(quantity)
                       def display_inventory(self):
                              print("Inventario:")
                              for group, products in self.groups.items():
                                    print("Grupo: {group}")
                                    for product, quantity in zip(products, self.stock[group]):
                                            print(" - Producto: {product}, Existencia: {quantity}")
                       def main():
                              inventory = Inventory()
                              dairy_products = ["Fairlife Milk", "Alta Dena Milk", "Queensland Butter"]
                              dairy_stock = [28, 36, 50]
                              for product, stock in zip(dairy_products, dairy_stock):
                                    inventory.add_product(product, stock, 'dairy')
                              while True:
                                    print("\nMenú:")
                                    print("1. Registrar nuevo producto")
                                    print("2. Visualizar inventario")
                                    print("3. Salir")
                                    choice = int(input("Ingrese la opción deseada (1/2/3): "))
                                    if choice == 1:
                                             product_name = input("Nombre del producto: ")
                                             quantity = int(input("Cantidad: "))
                                             group = input("Grupo (dairy, cleaning, grain): ")
                                             inventory.add_product(product_name, quantity, group)
                                    elif choice == 2:
                                             inventory.display_inventory()
                                    elif choice == 3:
                                             break
                                    else:
                                             print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
                       if __name__ == "__main__":
                              main()
