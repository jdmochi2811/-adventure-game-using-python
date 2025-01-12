import time

def slow_print(text, delay=0.05):
    """Prints text with a delay between characters for effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Main Game Functions
def character_creation():
    """Allows the player to create their character."""
    slow_print("Welcome to 'The Quest for the Golden Relic'!")
    name = input("Enter your character's name: ")
    slow_print(f"Greetings, {name}! Your journey begins now.")
    return {
        "name": name,
        "inventory": [],
        "quests_completed": 0,
        "points": 10,
        "keys": [],
    }

def display_inventory(player):
    """Displays the player's inventory."""
    if not player['inventory']:
        slow_print("Your inventory is empty.")
    else:
        slow_print("Your inventory contains:")
        for item in player['inventory']:
            slow_print(f"- {item}")

def buy_items(player):
    """Allows the player to buy items if they have enough points."""
    store = {
        "Health Potion": 5,
        "Sword": 10,
        "Shield": 8
    }
    slow_print("Welcome to the shop! Here are the items available:")
    for item, cost in store.items():
        slow_print(f"- {item}: {cost} points")

    while True:
        choice = input("Enter the name of the item you want to buy (or type 'exit' to leave): ").strip()
        if choice == "exit":
            break
        elif choice in store:
            if player['points'] >= store[choice]:
                player['inventory'].append(choice)
                player['points'] -= store[choice]
                slow_print(f"You bought {choice}!")
            else:
                slow_print("You don't have enough points to buy that item.")
        else:
            slow_print("Invalid choice. Please try again.")

def first_decision(player):
    """The first decision the player has to make."""
    slow_print("\nYou awaken in a mysterious forest, surrounded by towering trees and the faint glow of fireflies.")
    slow_print("A voice echoes in your mind: 'Seeker of treasures, the Golden Relic lies hidden deep within the Forbidden Cavern.'")
    slow_print("To find it, you must overcome trials, make choices, and gather keys to unlock the final gate.")
    slow_print("Beware, every decision shapes your destiny.")
    slow_print("\nAhead of you are three paths:")
    slow_print("1. The Overgrown Path: Thick with vines and thorns but closer to a rumored treasure stash.")
    slow_print("2. The Whispering River: A tranquil route that may hide dangers beneath the water.")
    slow_print("3. The Rocky Trail: Steep and challenging but possibly leading to shortcuts.")

    while True:
        choice = input("Which path will you choose? (1/2/3): ").strip()
        if choice == "1":
            player['points'] -= 5
            slow_print("You brave the Overgrown Path, enduring scratches from the thorns.")
            slow_print("But you find a Small Treasure Chest containing 10 points.")
            player['points'] += 10
            break
        elif choice == "2":
            player['points'] += 15
            slow_print("You follow the Whispering River, discovering hidden herbs that give you 15 points.")
            slow_print("Suddenly, you're attacked by river creatures! You lose 10 points.")
            player['points'] -= 10
            break
        elif choice == "3":
            player['points'] -= 10
            slow_print("The Rocky Trail is steep and challenging, and you lose some energy.")
            slow_print("But you find a Map Fragment that might help you later.")
            player['inventory'].append("Map Fragment")
            break
        else:
            slow_print("Invalid choice. Please choose 1, 2, or 3.")

def solve_riddle(player):
    """The riddle challenge with consequences."""
    slow_print("\nAt the end of your chosen path, you encounter a wise old hermit.")
    slow_print("He offers you a clue to the Relics location, but only if you solve his riddle:")
    slow_print("Im not alive, but I grow; I dont have lungs, but I need air. What am I?")

    while True:
        answer = input("What is your answer? ").strip().lower()
        if answer == "fire":
            player['points'] += 20
            player['keys'].append("Key 1")
            slow_print("Correct! The hermit hands you Key 1 and rewards you with 20 points.")
            break
        else:
            player['points'] -= 10
            slow_print("Incorrect answer. The hermit is disappointed, but allows you to attempt another task.")
            slow_print("You fetch water from a nearby stream, gaining Key 1.")
            player['keys'].append("Key 1")
            break

def second_decision(player):
    """The treasure hunt decision."""
    slow_print("\nYou arrive at a clearing with three hidden treasures:")
    slow_print("1. A Buried Chest (requires digging).")
    slow_print("2. A Locked Chest (requires a key).")
    slow_print("3. A Suspended Chest hanging from a tree.")

    while True:
        choice = input("Which treasure will you pursue? (1/2/3): ").strip()
        if choice == "1":
            player['points'] += 15
            player['points'] -= 5
            slow_print("You dig up a buried chest and gain 15 points, but it takes time (-5 points).")
            break
        elif choice == "2" and "Key 1" in player['keys']:
            player['points'] += 30
            slow_print("You use Key 1 to open the Locked Chest and find 30 points inside.")
            break
        elif choice == "2":
            slow_print("The chest remains locked. You need Key 1 to open it.")
            break
        elif choice == "3":
            player['points'] += 20
            player['points'] -= 10
            slow_print("You climb a tree to retrieve the suspended chest. It contains 20 points, but you lose 10 points when you fall.")
            break
        else:
            slow_print("Invalid choice. Please choose 1, 2, or 3.")

def guardian_challenge(player):
    """The Guardian's challenge."""
    slow_print("\nA mighty guardian blocks your path to the Forbidden Cavern.")
    slow_print("He demands that you pass a challenge:")
    slow_print("1. Solve a Math Puzzle (e.g., rearrange numbers to make a total of 25).")
    slow_print("2. Engage in a Combat Trial using a weapon found earlier.")
    slow_print("3. Trade one of your treasures to gain passage.")

    while True:
        choice = input("What will you do? (1/2/3): ").strip()
        if choice == "1":
            player['points'] += 20
            player['keys'].append("Key 2")
            slow_print("You solve the puzzle and gain Key 2 and 20 points.")
            break
        elif choice == "2":
            player['points'] -= 10
            slow_print("You engage in a combat trial. You lose 10 points but gain passage.")
            break
        elif choice == "3":
            slow_print("You trade a treasure to the guardian and gain passage without further harm.")
            break
        else:
            slow_print("Invalid choice. Please choose 1, 2, or 3.")

def final_task(player):
    """The final labyrinth and moral decision."""
    slow_print("\nYou have reached the Forbidden Cavern, where the Golden Relic is hidden.")
    slow_print("To enter, you must use both Key 1 and Key 2.")

    if "Key 1" in player['keys'] and "Key 2" in player['keys']:
        slow_print("The keys unlock the labyrinth's gate.")
        slow_print("\nInside, you encounter:")
        slow_print("1. A Trap Room: Disarm traps to avoid losing 15 points.")
        slow_print("2. The False Relic Room: Identify the true relic among decoys. Choose correctly to gain 50 points.")
        slow_print("3. A Final Guardian: Answer a moral question to prove your worth.")

        while True:
            choice = input("Which challenge will you face? (1/2/3): ").strip()
            if choice == "1":
                player['points'] -= 15
                slow_print("You disarm the traps, but lose 15 points in the process.")
                break
            elif choice == "2":
                correct = input("Which relic is the true one? ").strip().lower()
                if correct == "golden relic":
                    player['points'] += 50
                    slow_print("You identify the true relic and gain 50 points.")
                else:
                    player['points'] -= 20
                    slow_print("You chose incorrectly and lose 20 points.")
                break
            elif choice == "3":
                slow_print("The Final Guardian asks: 'Would you share this relic with the world or keep it for yourself?'")
                moral_choice = input("Your answer? (share/keep): ").strip().lower()
                if moral_choice == "share":
                    slow_print("You choose to share the relic with the world. Your generosity earns you the title of Ultimate Treasure Hunter!")
                    player['points'] += 100
                else:
                    slow_print("You choose to keep the relic for yourself. The world remains unaware of its power.")
                break
            else:
                slow_print("Invalid choice. Please choose 1, 2, or 3.")
    else:
        slow_print("You do not have both keys required to enter the labyrinth. Your journey ends here.")

def main():
    """The main game loop."""
    player = character_creation()

    while True:
        slow_print("\nWhat would you like to do next?")
        slow_print("1. View inventory")
        slow_print("2. Go on a quest")
        slow_print("3. Visit shop")
        slow_print("4. Exit game")
        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            display_inventory(player)
        elif choice == "2":
            if player['quests_completed'] == 0:
                first_decision(player)
                solve_riddle(player)
                second_decision(player)
                guardian_challenge(player)
                final_task(player)
                player['quests_completed'] += 1
            else:
                slow_print("You have already begun your quest. Continue where you left off.")
        elif choice == "3":
            buy_items(player)
        elif choice == "4":
            slow_print("Thank you for playing! Goodbye.")
            break
        else:
            slow_print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
