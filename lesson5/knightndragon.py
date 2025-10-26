import random

weapons = {
    "club": {"damage": 50, "critical_chance": 30, "critical_percentage": 1.5},
    "mace": {"damage": 150, "critical_chance": 20, "critical_percentage": 2},
    "axe": {"damage": 100, "critical_chance": 20, "critical_percentage": 2.25},
    "sword": {"damage": 100, "critical_chance": 50, "critical_percentage": 2.5},
    "spear": {"damage": 125, "critical_chance": 35, "critical_percentage": 2.5},
}
list_of_mobs = ["goblin", "orc", "troll", "satyr"]


class Weapon:
    def __init__(self, name):
        stats = weapons[name]
        self.name = name
        self.damage = stats["damage"]
        self.critical_chance = stats["critical_chance"]
        self.critical_percentage = stats["critical_percentage"]

    def deal_damage(self, base_damage):
        damage = random.randint(base_damage - 5, base_damage + 5) + self.damage
        critical = False
        if random.randint(1, 100) <= self.critical_chance:
            damage = damage*self.critical_percentage
            critical = True
        return damage, critical


class Character:
    def __init__(self, name, health, damage, armor):
        self._name = name
        self._health = health
        self._damage = damage
        self._armor = armor

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value > 500:
            self._health = 500
        else:
            self._health = value

    @property
    def damage(self):
        return self._damage

    @property
    def armor(self):
        return self._armor

    @armor.setter
    def armor(self, value):
        if value >= 1:
            raise ValueError("Armor cannot be greater than or equal to 1")
        if value < 0:
            raise ValueError("Armor cannot be less than 0")
        self._armor = value

    def take_damage(self, damage):
        self._health = self._health - (damage - damage*self._armor)

    def attack(self, target):
        damage = random.randint(self._damage - 5, self._damage + 5)
        target.take_damage(damage)
        print(f"{self._name} аттакует {target.name}, нанося {damage} урона")
        return damage


class Knight(Character):
    def __init__(self, name="Bard", health=500, damage=80, armor=0, weapon=Weapon("club")):
        super().__init__(name, health, damage, armor)
        self.weapon = weapon

    def attack(self, target):
        damage, critical = self.weapon.deal_damage(self._damage)
        if critical:
            print(f"Критический удар! {self._name} наносит {target.name} {damage} урона")
        else:
            print(f"{self._name} наносит {target.name} {damage} урона")
        target.take_damage(damage)
        return damage


class Dragon(Character):
    def __init__(self, name="Smaug", health=700, damage=150, armor=0):
        super().__init__(name, health, damage, armor)

    def attack(self, target):
        if random.randint(1, 100) < 30:
            damage = random.randint(self._damage - 5, self._damage + 5) + 50
            print(f"{self._name} аттакует огнём {target.name}, нанося {damage} урона")
        else:
            damage = random.randint(self._damage - 5, self._damage + 5)
            print(f"{self._name} наносит {target.name} {damage} урона")

        target.take_damage(damage)
        return damage


class Mob(Character):
    def __init__(self, name):
        if name == "goblin":
            super().__init__("goblin", 200, 50, 0)
        elif name == "orc":
            super().__init__("orc", 300, 70, 0.2)
        elif name == "troll":
            super().__init__("troll", 300, 90, 0.2)
        elif name == "satyr":
            super().__init__("satyr", 250, 100, 0)
        else:
            raise ValueError("Invalid mob name")


class Game:
    def __init__(self):
        self.knight = Knight()
        self.dragon = Dragon()

    def fight(self, enemy):
        while self.knight.health > 0 and enemy.health > 0:
            print(f"\n{self.knight.name} HP: {self.knight.health:.1f} | {enemy.name} HP: {enemy.health:.1f}")
            action = input("Выберите действие: [A] Атаковать [H] Полечиться\n> ").lower()
            if action == "a":
                self.knight.attack(enemy)
            elif action == "h":
                self.knight.health += 80
            else:
                print("Неверная команда. Ход пропущен.")
                continue
            if enemy.health > 0:
                enemy.attack(self.knight)
            if not self.knight.health > 0 and not isinstance(enemy, Dragon):
                print("Вы погибли! Конец игры.")
                exit()
        if self.knight.health > 0:
            print(f"{enemy.name} побежден!\n")

    def forest(self):
        print(f"Вы — рыцарь, ваше начальное оружие: {self.knight.weapon.name} (палка)")
        mob = Mob(random.choice(["goblin", "orc", "troll"]))
        self.fight(mob)
        print("Вы нашли артефакт, топор и щит (+0.2 броня).")
        self.knight.weapon = Weapon("axe")
        self.knight.armor = 0.2

    def castle(self):
        print("\nВы заходите в замок. На вас идут враги.")
        for _ in range(2):
            mob = Mob(random.choice(list_of_mobs))
            self.fight(mob)

        weapons_options = [Weapon("sword"), Weapon("mace"), Weapon("spear")]
        print("Вы находите три оружия на выбор:")
        for i, w in enumerate(weapons_options):
            print(f"{i+1}) {w.name} - урон {w.damage}, крит {w.critical_chance}%, множитель {w.critical_percentage}")
        choice = input("Выберите оружие (1-3)\nНажмите любую другую кнопку, чтобы оставить текущее: ")
        try:
            self.knight.weapon = (weapons_options[int(choice)-1])
        except:
            print("Оставлено текущее оружие.")

        print("Вы находите новый щит (+0.5 броня)")
        self.knight.armor = 0.5

        for _ in range(2):
            mob = Mob(random.choice(list_of_mobs))
            self.fight(mob)

    def dragon_room(self):
        print("\nВы вошли в зал дракона!")
        print("Вы видите дракона. Доступны варианты:")
        print("1) Расколдовать дракона")
        print("2) Убить дракона")
        while True:
            choice = input("Выберите действие (1-2): ")
            if choice in ("1", "2"):
                break
        if choice == "1":
            print("Вы использовали артефакт! Дракон превращается в человека и благодарит вас.")
            print("Концовка: Мирная")
        elif choice == "2":
            print("Вы сражаетесь с драконом!")
            self.fight(self.dragon)
            if self.knight.health > 0:
                print("Вы победили дракона! Вы стали легендой!")
                print("Концовка: Героическая")
            else:
                print("Вы промедлили и дракон вас убил. Концовка: Трагическая")

    def play(self):
        self.forest()
        self.castle()
        self.dragon_room()


if __name__ == "__main__":
    game = Game()
    game.play()