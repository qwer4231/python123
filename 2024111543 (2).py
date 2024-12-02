import random

class Character:
    def __init__(self, name, hp, attack, defense, speed):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.hp = max(0, self.hp - actual_damage)
        return actual_damage

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return (f"{self.name} - HP: {self.hp}, 공격력: {self.attack}, "
                f"방어력: {self.defense}, 속도: {self.speed}")


class Hero(Character):
    def __init__(self, name, hp, attack, defense, speed, role):
        super().__init__(name, hp, attack, defense, speed)
        self.role = role
        self.exp = 0
        self.weapon = None
        self.armor = None
        self.level = 1

    def equip(self, equipment):
        if equipment.attack_bonus > 0:
            self.weapon = equipment
        elif equipment.defense_bonus > 0:
            self.armor = equipment
        print(f"{self.name}가 {equipment.name}을(를) 장착했습니다.")

    def calculate_attack(self):
        return self.attack + (self.weapon.attack_bonus if self.weapon else 0)

    def calculate_defense(self):
        return self.defense + (self.armor.defense_bonus if self.armor else 0)

    def gain_exp(self, amount):
        self.exp += amount
        print(f"{self.name}가 경험치 {amount}를 획득했습니다.")
        if self.exp >= 100:  # 레벨업 조건
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp = 0
        if self.role == "전사":
            self.hp += 30
            self.attack += 8
            self.defense += 5
            self.speed += 2
        elif self.role == "마법사":
            self.hp += 20
            self.attack += 10
            self.defense += 3
            self.speed += 3
        elif self.role == "궁수":
            self.hp += 25
            self.attack += 7
            self.defense += 4
            self.speed += 5
        print(f"{self.name}가 레벨업! 현재 레벨: {self.level}")


class Equipment:
    def __init__(self, name, grade, attack_bonus=0, defense_bonus=0):
        self.name = name
        self.grade = grade
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus

    def __str__(self):
        return (f"{self.name} ({self.grade}) - 공격력 보너스: {self.attack_bonus}, "
                f"방어력 보너스: {self.defense_bonus}")


class Monster(Character):
    def __init__(self, name, hp, attack, defense, speed, level):
        super().__init__(name, hp, attack, defense, speed)
        self.level = level

    def drop_loot(self):
        is_weapon = random.random() <= 0.5
        grade_roll = random.random()
        if grade_roll <= 0.5:
            grade = '일반'
            bonus = random.randint(1, 5)
        elif grade_roll <= 0.8:
            grade = '레어'
            bonus = random.randint(5, 10)
        else:
            grade = '전설'
            bonus = random.randint(10, 15)

        if is_weapon:
            return Equipment(f"{grade} 무기", grade, attack_bonus=bonus)
        else:
            return Equipment(f"{grade} 방어구", grade, defense_bonus=bonus)

    def exp_reward(self):
        return self.level * 20

    def level_up(self):
        self.level += 1
        self.hp += 15
        self.attack += 5
        self.defense += 3
        self.speed += 2