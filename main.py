import random
import os

HIGH_SCORE_FILE = "highscore.txt"  

PLAYER = "[P]" 
EGG    = " G " 
ROAD  = " . " 
ALIEN  = " A " 

player = {"x": 0, "y": 0, "score": 0, "high_score": 0}
egg = {"x": random.randint(-10, 10), "y": random.randint(-10, 10)}
alien = {"x": random.randint(-10, 10), "y": random.randint(-10, 10)}

def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        try:
            with open(HIGH_SCORE_FILE, "r") as f:
                return int(f.read().strip())
        except ValueError:
            return 0 
    return 0

def save_high_score(score):
    try:
        with open(HIGH_SCORE_FILE, "w") as f:
            f.write(str(score))
    except IOError:
        print("Error saving high score")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_map(current_high_score):
    print(f"Score: {player['score']} | High Score: {current_high_score}")
    print(f"Position: {player['x']}, {player['y']}")
    print("-" * 66)

    for y in range(10, -10 - 1, -1):
        row_display = ""
        for x in range(-10, 10 + 1):
            
            if x == player["x"] and y == player["y"]:
                row_display += PLAYER
            elif x == egg["x"] and y == egg["y"]:
                row_display += EGG
            elif x == alien["x"] and y == alien["y"]:
                row_display += ALIEN
            else:
                row_display += ROAD
        
        print(f"| {row_display} |")
    
    print("-" * 66)
    print("Commands: w (Up), s (Down), a (Left), d (Right), q (Quit)")

def move_alien():
    move = random.choice(['w', 'a', 's', 'd'])
    if move == 'w' and alien['y'] < 10: alien['y'] += 1
    elif move == 's' and alien['y'] > -10: alien['y'] -= 1
    elif move == 'a' and alien['x'] > -10: alien['x'] -= 1
    elif move == 'd' and alien['x'] < 10: alien['x'] += 1

def main():
    game_running = True
    high_score = load_high_score()

    while game_running:
        clear_screen()
        draw_map(high_score)
        if player["x"] == egg["x"] and player["y"] == egg["y"]:
            print("\YOU FOUND THE GOLDEN EGG. +5 POINTS!")
            player["score"] += 5
            if player["score"] > high_score:
                high_score = player["score"]
                save_high_score(high_score) 
                print("NEW HIGH SCORE!")
            egg["x"] = random.randint(-10, 10)
            egg["y"] = random.randint(-10, 10)
            input("Press Enter to continue...")
            continue 
        if player["x"] == alien["x"] and player["y"] == alien["y"]:
            print("\n!!! The Alien got you!")
            print(f"Final Score: {player['score']}")
            break
        try:
            action = input("\nMove > ").lower().strip()
        except KeyboardInterrupt:
            print("\nExiting...")
            break

        if action == "q":
            game_running = False
            print("Bye!")
        
        elif action == "w":
            if player["y"] < 10: player["y"] += 1
            else: print("WALL")
        elif action == "s":
            if player["y"] > -10: player["y"] -= 1
            else: print("WALL")
        elif action == "a":
            if player["x"] > -10: player["x"] -= 1
            else: print("WALL")
        elif action == "d":
            if player["x"] < 10: player["x"] += 1
            else: print("WALL")
        else:
            print("Unknown command.")
            input("Press Enter...")
        
        move_alien()

if __name__ == "__main__":
    main()