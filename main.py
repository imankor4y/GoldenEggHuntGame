import os
import time
import random
import sys
try:
    import world_data
    import aliens
    import ascii_art
except ImportError as e:
    print(f"Error! Unable to import ({e})")
    sys.exit()

characters = ["Gandalf", "Dumbledore", "Saruman"]
characters_parametres = [[4, 8, 3, 8, 5],[8, 3, 2, 5, 8], [2, 3, 9, 7, 4]]

class user:
    def __init__(self, name, characters_index):
        self.name = name
        self.stats = characters_parametres[characters_index]
        self.hero_class = characters[characters_index]
        self.max_health = 100 + (self.stats[4] * 5)
        self.health = self.max_health
        self.money = 100
        self.inv = ["potion"]
        self.Map = "forest"

def record_score():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return 0 

def save_score(users_score):
    record = record_score()
    if users_score > record:
        with open("highscore.txt", "w") as f:
            f.write(str(users_score))
        print(f"\n[NEW HIGH SCORE: {users_score} gold!]")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_character():
    clear()
    high_score = record_score()
    print(f"=== Creating character === (Current High Score: {high_score})")
    
    for i in range(len(characters)):
        print(f"{i}) {characters[i]} | Stat: {characters_parametres[i]}")
    
    while True:
        try:
            choice = int(input("\nChoose number from 0 to 2: "))
            if 0 <= choice < len(characters):
                break
            print("Wrong number. Try again.")
        except ValueError:
            print("Invalid input! Please enter a number (0, 1, or 2).")
            
    name = input("What is your name? ")
    if not name:
        name = characters[choice]
    return user(name, choice)

def fight(user, ALIEN):
    print(f"\n!!! Attention !!! {ALIEN.name} attacks you!")
    
    while ALIEN.is_alive() and user.health > 0:
        print(f"\nuser: {user.health}/{user.max_health} HP | Alien: {ALIEN.health} HP")
        option = input("`Action` (1-Attack, 2-Potion, 3-Run): ")

        if option == "1":
            damage = random.randint(5, 10) + user.stats[0]
            ALIEN.health = ALIEN.health - damage
            print(f"> You dealt {damage} damage!")
            
        elif option == "2":
            if "potion" in user.inv:
                user.inv.remove("potion")
                user.health = min(user.health + 30, user.max_health)
                print("> Health restored!")
            else:
                print("> No potions left!")
                
        elif option == "3":
            if random.randint(0, 10) + user.stats[1] > 10:
                print("> You successfully escaped!")
                return "escaped"
            print("> Failed to escape!")
        
        if ALIEN.is_alive():
            try:
                dmg = ALIEN.attack_user(user)
                user.health = user.health - dmg
                print(f"> {ALIEN.name} damaged you {dmg}.")
                time.sleep(0.5)
            except Exception as e:
                print(f"fight Error: {e}")
                break

    if user.health <= 0:
        return "dead"
    else:
        print(f"\nVICTORY!")
        item = ALIEN.drop_item()
        user.inv.append(item)
        user.money = user.money - 50
        print(f"Obtained: {item} and 50 gold.")
        return "won"

def main():
    try:
        user = create_character()
        game_running = True
        while game_running:
            clear()
            current_key = user.Map
            if current_key not in world_data.WORLD_ROOMS:
                print(f"Error: Map {current_key} not found in world_data.")
                break
                
            maps = world_data.WORLD_ROOMS[current_key]
            
            if "art_key" in maps:
                art_variable = getattr(ascii_art, maps["art_key"], None)
                if art_variable:
                    print(art_variable[0] if isinstance(art_variable, tuple) else art_variable)

            print(f"--- {maps['name']} ---")
            print(maps['description'])
            print(f"Road: {list(maps['exits'].keys())}")
            
            if maps.get('alien'):
                ALIEN = aliens.create_alien(maps['alien'])
                result = fight(user, ALIEN)
                
                if result == "dead":
                    print("\n=== GAME OVER ===")
                    save_score(user.money)
                    break
                elif result == "won":
                    maps['alien'] = None 

            print("-" * 40)
            print(f"------- Your Health: {user.health}/{user.max_health} ")
            print(f"------- Your Gold: {user.money} ")
            print(f"------- Your Inventory: {user.inv} ")
            print("-" * 40)

            command = input("Commands (go [side], shop, look, quit): ").lower().split()
            if not command: continue
            choice = command[0]
            if choice == "quit":
                save_score(user.money)
                game_running = False
            elif choice == "look":
                print(f"\n{maps['look']}")
                if maps.get('items'):
                    print(f"Here lies: {maps['items']}")
                    if input("Take it? (yes/no): ").lower() == 'yes':
                        user.inv.extend(maps['items'])
                        maps['items'] = []
                input("Press Enter...")
            elif choice == "shop":
                print("\n--- Shop ---")
                print("1. Potion (50 coins)")
                if input("Choice: ") == "1":
                    if user.money >= 50:
                        print("You bought a potion.")
                        user.money = user.money - 50
                        user.inv.append("potion")
                        
                    else:
                        print("Not enough gold!")
                            
                time.sleep(1)

            elif choice == "go":
                try:
                    side = command[1]
                    if side in maps['exits']:
                        user.Map = maps['exits'][side]
                    else:
                        print("You can't go there. NO ROAD!")
                        time.sleep(1)
                except IndexError:
                    print("Go where? (Example: go east)")
                    time.sleep(1)

    except KeyboardInterrupt:
        print("\nGame closed by user.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Good Game!")

if __name__ == "__main__":
    main()
