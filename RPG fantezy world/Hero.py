import random
class Hero:
    'Создание персонажа.'
    def __init__(self, name, age, hp, stamina, mana, strenght, intelligence):
        self.name = name
        self.age = age
        self.level = 1
        self.exp = 0
        self.hp = hp
        self.stamina = stamina
        self.mana = mana
        self.strenght = strenght
        self.intelligence = intelligence
    def create_hero(name, age, race, distant):
        hp = 100
        stamina = 50
        mana = 50
        strenght = 1
        intelligence = 1
        if race == race_list[0]:
            hp += 50
            stamina += 100
            strenght += 2
            intelligence += 1     
        elif race == race_list[1]:
            hp += 100
            mana += 100
            strenght += 50
            intelligence += 2
        elif race == race_list[2]:
            hp += 50
            stamina += 50
            mana += 50
            strenght += 1 
            intelligence += 1
        else:
            print('Я не знаю что это за раса.')
        if distant == distant_list[0]:
            hp += 250
            stamina += 75
            strenght += 2   
            intelligence += 1  
        elif distant == distant_list[1]:
            hp += 300
            mana += 50
            strenght += 4
            intelligence += 2
        elif distant == distant_list[2]:
            hp += 400
            stamina += 75
            mana += 50
            strenght += 5 
            intelligence += 1
        elif distant == distant_list[3]:
            hp += 600
            stamina += 75
            mana += 50
            strenght += 5 
            intelligence += 1
        elif distant == distant_list[4]:
            hp += 300
            stamina += 75
            mana += 50
            strenght += 5 
            intelligence += 1
        elif distant == distant_list[5]:
            hp += 700
            stamina += 75
            mana += 50
            strenght += 7
            intelligence += 5
        elif distant == distant_list[6]:
            hp += 700
            stamina += 75
            mana += 50
            strenght += 7
            intelligence += 5
        elif distant == distant_list[7]:
            hp += 700
            stamina += 75
            mana += 50
            strenght += 7
            intelligence += 5
        elif distant == distant_list[8]:
            hp += 1000
            stamina += 100
            mana += 300
            strenght += 9
            intelligence += 20
        else:
            print('я не знаю что это за ')
        return Hero(name, age, hp, stamina, mana, strenght ,intelligence)
    def attack(self, enemy):
        if self.intelligence > self.strenght:
            enemy.hp -= self.intelligence * 5
        else:
            enemy.hp -= self.strenght *5
        if enemy.hp <= 0:
            print(f'{enemy.name} побежден!!!')
            weapon = random.randint(1, 3)
            if weapon == 1:
                weapon_loot = random.choice(weapon_list)
                if weapon_loot == weapon_list[0]:
                    weapon_intelligence = 5
                    weapon_strenght = 1
                elif weapon_loot == weapon_list[1]:
                    weapon_intelligence = 1
                    weapon_strenght = 5
                elif weapon_loot == weapon_list[2]:
                    weapon_intelligence = 3
                    weapon_strenght = 3
                print(f'Вам выпало оружие {weapon_loot}')
                weapon_answer = input('Хотите взять это оружие: ')
                if weapon_answer == 'да':
                    print('Вы взяли оружие.')
                    self.intelligence += weapon_intelligence
                    self.strenght += weapon_strenght
                else:
                    print('Вы отказались от оружия.')
            else:
                print('Вам не выпало оружие(')
            self.exp += random.randint(10, 21)
            if self.exp >= 100 * self.level:
                self.level_up()
            return True    
        else:
            print(f'У врага {enemy.name}\n осталось {enemy.hp} здоровья.\n')
            return False
    def level_up(self):
        self.level += 1
        self.hp += 10
        self.strenght += 1
        self.intelligence += 1
        self.mana += 10
        self.stamina += 10
        print(f'ПОЗДРАВЛЯЮ!! {self.name} твой уровень повышен. Текущий уровень {self.level}')
        self.exp = 0
            
    
        
        
        
class Enemy:
    'Создание врага'
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def create_enemy():
        rnd_name = random.choice(enemy_name_list) 
        rnd_hp = random.randint(50, 600)
        rnd_damage = random.randint(10, 41)
        return Enemy(rnd_name, rnd_hp, rnd_damage)
    def attack(self, hero):
        hero.hp -= self.damage
        if hero.hp <= 0:
            print(f'Герой {hero.name} повержен.')
        else:
            print(f'У героя {hero.name} осталось {hero.hp} здоровья. ') 

def fight_choise():
    answer = input(f'Готов ли ты сразиться с {enemy.name}:\nХП: {enemy.hp}\nУрон: {enemy.damage}\n').lower()
    if answer == 'да':
        result = hero.attack(enemy)
        if result == False:
            enemy.attack(hero)
            fight_choise()
    elif answer =='нет':
        print(f'ВЫ сбежали от врага {enemy.name}')
    else:
        print('Я вас не понимаю.')
        fight_choise()
    
               
                
        
        
        
                     
                 
                 
                                
enemy_name_list =['валькирия', "хог", 'электрогигант''элитные варворы', 'ведьма', 'электро дракон', 'кольт', 'шелли', 'гигант']
race_list =['гном', 'эльф', 'человек']
distant_list =[ 'маг', 'лучник', 'варвар']
weapon_list =['посох', 'меч', 'лук']
hero_race = input('Введите расу вашего персонажа:\n ').lower()
hero_distant = input('Введите профессию вашего персонажа: ').lower()
hero = Hero.create_hero('Вася', 15, hero_race, hero_distant)

print(f'Твои характиристики:\nИмя {hero.name}\nВозраст {hero.age}\nХп {hero.hp}\nМана {hero.mana}\nСтамина {hero.stamina}\nСила {hero.strenght}\nИнтеллект {hero.intelligence}\n')
while True:
    event = random.randint(1, 3)
    if event == 1:
        enemy = Enemy.create_enemy()
        print(f'ОГО!!! Это новый враг {enemy.name}')
        fight_choise()
    else:
        print('Вам не кто не встретился.') 
        
        
    
