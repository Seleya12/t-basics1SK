MAX_INVENTORY_SIZE = 5
inventory = []
current_room = "lobby"
game_won = False

rooms = {
    "lobby": {
        "description": "You are in the studio lobby. Posters of Linkin Park hang on the walls.",
        "items": [
            {"name": "Access Card", "type": "tool", "description": "Grants access to restricted studio areas."}
        ],
        "exits": ["recording_room"]
    },
    "recording_room": {
        "description": "You enter the recording room. A faint echo of vocals lingers in the air.",
        "items": [
            {"name": "Guitar Pick", "type": "tool", "description": "Mike's favorite pick. Still warm."},
            {"name": "Energy Drink", "type": "healing", "uses": 1, "description": "Restores your energy."}
        ],
        "exits": ["lobby", "archive"]
    },
    "archive": {
        "description": "You are surrounded by shelves of tapes and handwritten notes.",
        "items": [
            {"name": "Lyrics Sheet", "type": "clue", "description": "A lost verse from an unreleased track."}
        ],
        "exits": ["recording_room", "control_room"]
    },
    "control_room": {
        "description": "This is the heart of the studio. The soundboard awaits one final song.",
        "items": [],
        "exits": ["archive"]
    }
}

def show_inventory():
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Inventory:")
        for item in inventory:
            print(f"- {item['name']}")

def show_room_items():
    items = rooms[current_room]["items"]
    if not items:
        print("There are no items here.")
    else:
        print("Items in the room:")
        for item in items:
            print(f"- {item['name']}")

def pick_up(item_name):
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Your inventory is full.")
        return
    for item in rooms[current_room]["items"]:
        if item["name"].lower() == item_name.lower():
            inventory.append(item)
            rooms[current_room]["items"].remove(item)
            print(f"You picked up: {item['name']}")
            return
    print("That item is not here.")

def drop(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            inventory.remove(item)
            rooms[current_room]["items"].append(item)
            print(f"You dropped: {item['name']}")
            return
    print("You don't have that item.")

def use(item_name):
    global game_won
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            if item["type"] in ["healing", "food"]:
                print(f"You used the {item['name']} and feel refreshed.")
                inventory.remove(item)
                return
            elif item["type"] == "clue" and item["name"].lower() == "lyrics page":
                has_pick = any(i["name"].lower() == "guitar pick" for i in inventory)
                if has_pick and current_room == "control_room":
                    print("You place the Lyrics Sheet on the console and strum the Guitar Pick...")
                    print("The hidden track comes alive. You've restored the lost Linkin Park demo.")
                    game_won = True
                    return
                else:
                    print("You need to be in the control room and have the Guitar Pick to use this.")
                    return
            else:
                print(f"You used the {item['name']}.")
                return
    print("You don't have that item.")

def examine(item_name):
    all_items = inventory + rooms[current_room]["items"]
    for item in all_items:
        if item["name"].lower() == item_name.lower():
            print(f"{item['name']}: {item.get('description', 'No description.')}")
            return
    print("You see nothing like that here.")

def show_help():
    print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], help, quit")

def game_loop():
    global current_room
    print("Welcome to 'Escape the Studio – Linkin Park Lost Tracks'")
    player_name = input("Enter your name: ").strip() or "Soldier"
    print(f"Welcome, {player_name}! Type 'help' for a list of commands.")

    while not game_won:
        print(f"\n{rooms[current_room]['description']}")
        command = input("> ").strip().lower()

        if command == "":
            continue
        elif command == "help":
            show_help()
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            pick_up(command[7:])
        elif command.startswith("drop "):
            drop(command[5:])
        elif command.startswith("use "):
            use(command[4:])
        elif command.startswith("examine "):
            examine(command[8:])
        elif command.startswith("go "):
            destination = command[3:]
            if destination in rooms[current_room]["exits"]:
                current_room = destination
            else:
                print("You can't go there from here.")
        elif command == "quit":
            print(f"Goodbye, {player_name}.")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")

    if game_won:
        print("You won the game. Congratulations!")

if __name__ == "__main__":
    game_loop()
