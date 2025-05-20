import sys

inventory = []
INVENTORY_LIMIT = 5

rooms = {
    "lobby": {
        "items": [
            {"name": "Access Card", "type": "tool", "uses": 1},
            {"name": "Energy Drink", "type": "food", "uses": 1}
        ],
        "description": "You are in the studio lobby. Posters of Linkin Park hang on the walls."
    },
    "recording_room": {
        "items": [
            {"name": "Lyrics Sheet", "type": "tool", "uses": 2},
            {"name": "Guitar", "type": "tool", "uses": 2}
        ],
        "description": "This is the main recording room where echoes of 'Numb' still linger.",
        "requires": "Access Card"
    },
    "sound_lab": {
        "items": [
            {"name": "Mixer Console", "type": "tool", "uses": 1},
            {"name": "Protein Bar", "type": "food", "uses": 1}
        ],
        "description": "The studio's sound lab is filled with blinking lights and old tracks on tape.",
        "requires": "Lyrics Sheet"
    }
}
current_room = "lobby"
player_energy = 3
escaped = False


def show_room_items():
    print(f"\n{rooms[current_room]['description']}")
    items = rooms[current_room]["items"]
    if items:
        print("Items you can pick up:", ", ".join([item["name"] for item in items]))
        print("Use 'pickup <item>' to grab one, or 'examine <item>' to inspect it.")
    else:
        print("No items here to pick up.")

def show_rooms():
    print("\nPlaces you can move to:")
    for room_name, room_data in rooms.items():
        if room_name == current_room:
            print(f"- {room_name} (you are here)")
        elif "requires" in room_data and room_data["requires"] not in [i["name"] for i in inventory]:
            print(f"- {room_name} (locked, needs {room_data['requires']})")
        else:
            print(f"- {room_name} (accessible)")
    print("Use 'move <room>' to travel.")

def pick_up(item_name):
    items = rooms[current_room]["items"]
    for item in items:
        if item["name"].lower() == item_name.lower():
            if len(inventory) < INVENTORY_LIMIT:
                inventory.append(item)
                items.remove(item)
                print(f"Picked up {item['name']}.")
                return
            else:
                print("Inventory full! Drop something first.")
                return
    print(f"No {item_name} found in {current_room}.")

def drop(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            inventory.remove(item)
            rooms[current_room]["items"].append(item)
            print(f"Dropped {item['name']}.")
            return
    print(f"No {item_name} in inventory.")

def use(item_name):
    global player_energy, escaped
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            if item["type"] == "food":
                player_energy = min(player_energy + 1, 5)
                print(f"Used {item['name']}. Energy is now {player_energy}.")
                item["uses"] -= 1
            elif item["name"] == "Mixer Console" and "Guitar" in [i["name"] for i in inventory]:
                print("You remixed the final track! You've created a tribute masterpiece and escaped the studio legend!")
                escaped = True
            else:
                print(f"Used {item['name']}, but nothing major happened.")
                item["uses"] -= 1
            if item["uses"] <= 0:
                inventory.remove(item)
                print(f"{item['name']} is depleted.")
            return
    print(f"No {item_name} in inventory.")

def show_inventory():
    print(f"\nEnergy: {player_energy}/5")
    if inventory:
        print("Inventory:", ", ".join([item["name"] for item in inventory]))
    else:
        print("Your inventory is empty.")

def examine(item_name):
    for item in inventory + rooms[current_room]["items"]:
        if item["name"].lower() == item_name.lower():
            print(f"{item['name']}: Type: {item['type']}, Uses left: {item['uses']}")
            return
    print(f"No {item_name} found.")

def move_to_room(room_name):
    global current_room
    if room_name not in rooms:
        print("No such room.")
        return
    if room_name == current_room:
        print("You're already here.")
        return
    if "requires" in rooms[room_name] and rooms[room_name]["requires"] not in [i["name"] for i in inventory]:
        print(f"You need a {rooms[room_name]['requires']} to enter {room_name}.")
        return
    current_room = room_name
    print(f"Moved to {room_name}.")
    show_room_items()

def help_menu():
    print("\nCommands:")
    print("  inventory - Show your inventory and energy")
    print("  rooms - List all rooms and access")
    print("  pickup <item> - Pick up an item")
    print("  drop <item> - Drop an item")
    print("  use <item> - Use or consume an item")
    print("  examine <item> - View item details")
    print("  move <room> - Change rooms")
    print("  help - Show this menu")
    print("  quit - Exit game")
    print("\nGoal: Collect the Guitar and Mixer Console and use them to create a tribute track and escape the studio!")


def main():
    global player_energy, escaped
    print("Welcome to 'Escape the Studio: Linkin Park Edition'!")
    name = input("What's your name, soldier?\n> ").strip().title()
    if name:
        print(f"Good to have you with us, {name}. Let’s finish what we started.")
    else:
        name = "Soldier"
        print(f"Alright then, {name}.")

    print("Survive the creative chaos, gather musical relics, and remix the final tribute.")
    print("Type 'help' for a list of commands.")
    show_room_items()

    while not escaped and player_energy > 0:
        try:
            command = input("\n> ").strip().lower()
            if command == "quit":
                print("Thanks for playing!")
                break
            elif command == "help":
                help_menu()
            elif command == "inventory":
                show_inventory()
            elif command == "rooms":
                show_rooms()
            elif command.startswith("pickup "):
                pick_up(command[7:])
                player_energy -= 1
            elif command.startswith("drop "):
                drop(command[5:])
                player_energy -= 1
            elif command.startswith("use "):
                use(command[4:])
                player_energy -= 1
            elif command.startswith("examine "):
                examine(command[8:])
                player_energy -= 1
            elif command.startswith("move "):
                move_to_room(command[5:])
                player_energy -= 1
            else:
                print("Unknown command. Type 'help' for commands.")
            
            # Zeige Energie nach jeder Aktion
            if command not in ["help", "inventory", "rooms"]:
                print(f"Energy: {player_energy}/5")

            # Spiel beenden wenn gewonnen
            if escaped:
                print("\n🎉 Congratulations! You remixed the tribute track and escaped the studio legend! 🎉")
                break

        except KeyboardInterrupt:
            print("\nThanks for playing!")
            break

    if player_energy <= 0 and not escaped:
        print("\n💀 You're out of energy... The studio consumes another soul.")
        
if __name__ == "__main__":
    main()
