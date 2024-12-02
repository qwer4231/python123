from character import Hero, Monster
from battle import Battle

def main():
    print("게임 시작")
    name = input("이름 입력:")
    role = input("직업 입력(전사/마법사/궁수)")

    hero = Hero("전사", hp=100, attack=15, defense=10, speed=12, role="전사")
    print(hero)

    monster = Monster("고블린", hp=50, attack=8, defense=5, speed=10, level=2)
    print(monster)

    battle = Battle()

    battle.fight(hero,monster)

    print(hero)

if __name__ == '__main__':
    main()

