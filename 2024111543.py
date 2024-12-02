class Battle:
    def start_battle(hero, monster):
        print(f"{hero.name}와 {monster.name}의 전투 시작!")
        turn = 1 

      
        if hero.speed >= monster.speed:
            turn_order = [hero, monster]
        else:
            turn_order = [monster, hero]

        while hero.is_alive() and monster.is_alive():
            print(f"== 턴 {turn} ==")  
            for character in turn_order:
                if not hero.is_alive() or not monster.is_alive():
                    break

                if character == hero:
                    damage = hero.calculate_attack()
                    actual_damage = monster.take_damage(damage)
                    print(f"{hero.name}가 {monster.name}에게 {actual_damage}의 피해를 입혔습니다.")
                else:
                    damage = monster.attack
                    actual_damage = hero.take_damage(damage)
                    print(f"{monster.name}가 {hero.name}에게 {actual_damage}의 피해를 입혔습니다.")
            
            turn += 1 

        
        if hero.is_alive():
            print(f"{hero.name}가 승리했습니다!")
            exp_reward = monster.exp_reward()
            hero.gain_exp(exp_reward)
            loot = monster.drop_loot()
            print(f"{monster.name}이(가) {loot}을(를) 드롭했습니다.")
            if loot:
                hero.equip(loot) 
        else:
            print(f"{monster.name}가 승리했습니다.")
