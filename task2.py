class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

# Создание объектов класса Store
store1 = Store("Магазин Любимый", "ул. Цветочная, 12")
store2 = Store("Гастроном №1", "пр-т Роз, 34")
store3 = Store("Экомаркет", "ул. Зеленая, 56")

# Добавление товаров в магазин Любимый
store1.add_item("яблоки", 120.5)
store1.add_item("бананы", 200.75)
store1.add_item("помидоры", 350.2)

# Добавление товаров в Гастроном №1
store2.add_item("молоко", 90.0)
store2.add_item("сок", 100.5)

# Добавление товаров в Экомаркет
store3.add_item("хлеб", 100.1)
store3.add_item("творог", 200.35)

# Проверка методов
print(f"{store1.name} - адрес: {store1.address}, ассортимент: {store1.items}")
print(f"Цена яблок: {store1.get_price('яблоки')}")

store2.remove_item("сок")
print(f"{store2.name} после удаления сока: {store2.items}")

store3.update_price("хлеб", 1.2)
print(f"{store3.name} после обновления цены на хлеб: {store3.items}")