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
        self.length = length  

class Model:
    def __init__(self, name):
        self.name = name
        self.outfit = []

    def wear_item(self, item):
        self.outfit.append(item)
        print(f"{self.name} надел(а) {item.type} ({item.style}, {item.color})")

    def walk_runway(self):
        if not self.outfit:
            print(f"{self.name} не в чем идти на подиум!")
            return
        print(f"{self.name} идет по подиуму в наряде: {', '.join([item.type for item in self.outfit])}")

    def remove_item(self, item):
        if item in self.outfit:
            self.outfit.remove(item)
            print(f"{self.name} снял(а) {item.type} ({item.style}, {item.color})")
        else:
            print(f"На {self.name} нет {item.type}")

class Jury:
    def __init__(self, preferences):
        self.preferences = preferences

    def rate_outfit(self, outfit):
        score = 0
        for item in outfit:
            for pref in self.preferences:
                style_bonus = 10 if item.style == pref['style'] else 0
                color_bonus = 5 if item.color == pref['color'] else 0 
                score += style_bonus + color_bonus  
        return score

class Shop:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_items(self):
        print("Доступные предметы:")
        for i, item in enumerate(self.items):
            print(f"{i+1}. {item.type} ({item.style}, {item.color}) - {item.price} монет")

    def buy_item(self, item_index):
        try:
            item = self.items[item_index - 1]
            print(f"Вы купили {item.type} ({item.style}, {item.color})")
            return item
        except IndexError:
            print("Неверный номер предмета.")
            return None
        except TypeError:
            print("Введите номер предмета, а не текст")
            return None

class GameManager:
    def __init__(self, model_name="Анна"):
        self.model = Model(model_name)
        self.jury = Jury([{'style': 'классика', 'color': 'черный'},
                          {'style': 'бохо', 'color': 'коричневый'}]) 
        self.shop = Shop()

    def start_game(self):
        print("Добро пожаловать в Fashion Stylist: Runway Challenge!")
        self.shop.add_item(Dress("классика", "черный", 100, "длинное"))
        self.shop.add_item(Dress("бохо", "зеленый", 80, "короткое"))
        self.shop.add_item(Garment("блузка", "классика", "белый", 60))
        self.shop.add_item(Garment("брюки", "классика", "черный", 90))
        self.shop.add_item(Garment("шляпа", "бохо", "коричневый", 40)) #Больше предметов

        while True:
            self.shop.display_items()

            choice = input(f"Что вы хотите сделать? (купить [номер], надеть [номер], снять [номер], подиум, выход): ")
            parts = choice.split()

            if not parts:
                continue

            action = parts[0].lower()

            if action == "купить":
                try:
                    item_index = int(parts[1])
                    item = self.shop.buy_item(item_index)
                    if item:
                        wear_choice = input(f"Надеть {item.type} сейчас? (да/нет): ").lower()
                        if wear_choice == "да":
                            self.model.wear_item(item)
                except (IndexError, ValueError):
                    print("Пожалуйста, введите номер предмета после 'купить'.")
            elif action == "надеть":
                try:
                    item_index = int(parts[1])
                    if 1 <= item_index <= len(self.shop.items):
                        item = self.shop.items[item_index-1]
                        self.model.wear_item(item)
                    else:
                        print("Неверный номер предмета.")


                except (IndexError, ValueError):
                    print("Пожалуйста, введите номер предмета после 'надеть'.")

            elif action == "снять":
                try:
                    item_index = int(parts[1])
                    if 1 <= item_index <= len(self.shop.items):
                        item = self.shop.items[item_index-1]
                        self.model.remove_item(item)
                    else:
                        print("Неверный номер предмета.")

                except (IndexError, ValueError):
                    print("Пожалуйста, введите номер предмета после 'снять'.")
            elif action == "подиум":
                self.model.walk_runway()
                score = self.jury.rate_outfit(self.model.outfit)
                print(f"Жюри оценило наряд на {score} баллов!")
            elif action == "выход":
                print("Спасибо за игру!")
                break
            else:
                print("Неверная команда. Попробуйте 'купить', 'надеть', 'снять', 'подиум' или 'выход'.")


if __name__ == "__main__":
    game = GameManager("Ирина") #Можно выбрать имя модели
    game.start_game()

