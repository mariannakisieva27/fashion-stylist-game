class Garment:
    def __init__(self, garment_type, style, color, price):
        self.type = garment_type
        self.style = style
        self.color = color
        self.price = price

    def check_compatibility(self, other_garment):
        if self.style == other_garment.style:
            return 10  # Бонус за совпадение
        elif self.style in ["универсальный", other_garment.style]:
            return 5
        else:
            return -5  # Штраф за несовпадение

class Dress(Garment):
    def __init__(self, style, color, price, length):
        super().__init__("платье", style, color, price)
        self.length = length  # Дополнительное свойство для платья

class Model:
    def __init__(self, name):
        self.name = name
        self.outfit = []

    def wear_item(self, item):
        self.outfit.append(item)
        print(f"{self.name} надел(а) {item.type}")

    def walk_runway(self):
        print(f"{self.name} идет по подиуму в наряде: {', '.join([item.type for item in self.outfit])}")

class Jury:
    def __init__(self, preferences):
        self.preferences = preferences

    def rate_outfit(self, outfit):
        score = 0
        for item in outfit:
            for pref in self.preferences:
                if item.style == pref['style'] and item.color == pref['color']:
                    score += 10
        return score

class Shop:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_items(self):
        for item in self.items:
            print(f"{item.type} ({item.style}, {item.color}) - {item.price} монет")

class GameManager:
    def __init__(self):
        self.model = Model("Анна")
        self.jury = Jury([{'style': 'классика', 'color': 'черный'}])
        self.shop = Shop()

    def start_game(self):
        print("Добро пожаловать в Fashion Stylist: Runway Challenge!")
        self.shop.add_item(Dress("классика", "черный", 100, "длинное"))
        self.shop.add_item(Dress("бохо", "зеленый", 80, "короткое"))
        self.shop.display_items()

        # Пример покупки и надевания платья
        dress = self.shop.items[0]
        self.model.wear_item(dress)

        # Показ на подиуме
        self.model.walk_runway()

        # Оценка жюри
        score = self.jury.rate_outfit(self.model.outfit)
        print(f"Жюри оценило наряд на {score} баллов!")

if name == "__main__":
    game = GameManager()
    game.start_game()
