# Text-based survival adventure game: Escape from a Linkin Park-inspired post-apocalyptic world
# Player must collect and use items to survive and find a way to freedom, themed around Linkin Park's music

import sys

# Inventory system
inventory = []
INVENTORY_LIMIT = 5

# Room system: Areas inspired by Linkin Park themes (e.g., dystopian, emotional, industrial)
rooms = {
    "wasteland": {
        "items": [
            {"name": "Energy Cell", "type": "tool", "uses": 3},
            {"name": "Rations", "type": "food", "uses": 1}
        ],
        "description": "A barren wasteland under a crimson sky, like the world of 'Somewhere I Belong.' Scattered tech lies around."
    },
    "ruins": {
        "items": [
            {"name": "Wire Coil", "type": "tool", "uses": 2},
            {"name": "Protein Bar", "type": "food", "uses": 1}
        ],
        "description": "Crumbling ruins of a city, echoing 'In the End.' You need a Decoder to navigate the locked gates.",
        "requires": "Decoder"
    },
    "bunker": {
        "items": [
            {"name": "Decoder", "type": "tool", "uses": 5},
            {"name": "Signal Flare", "type": "tool", "uses": 3}
        ],
        "description": "A dark bunker, like the hideout in 'Crawling.' Something high-tech is stashed here."
    }
}
current_room = "wasteland"

# Player status
player_energy = 3  # Max 5, decreases over time, restored by food
escaped = False

def show_room_items():
    """Display items in the current room."""
    print(f"\n{rooms[current_room]['description']}")
    items = rooms[current_room]["items"]
    if items:
        print("Items here:", ", ".join([item["name"] for item in items]))
    else:
        print("No items here.")

def pick_up(item_name):
    """Pick up an item from the room if inventory isn't full."""
    global inventory
    items = rooms[current_room]["items"]
    for item in items:
        if item["name"].lower() == item_name.lower():
            if len(inventory) < INVENTORY_LIMIT:
                inventory.append(item)
                items.remove(item)
                print(f"Picked up {item['name']}.")
                return
            else:
                print("Inventory full! Drop something first, like letting go in 'Numb.'")
                return
    print(f"No {item_name} found in {current_room}.")

def drop(item_name):
    """Drop an item from inventory to the room."""
    global inventory
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            inventory.remove(item)
            rooms[current_room]["items"].append(item)
            print(f"Dropped {item['name']}.")
            return
    print(f"No {item_name} in inventory.")

def use(item_name):
    """Use an item based on its type, with special events for certain items."""
    global player_energy, escaped
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            if item["type"] == "food":
                player_energy = min(player_energy + 1, 5)
                print(f"Consumed {item['name']}. Energy restored to {player_energy}, pushing through like 'Breaking the Habit.'")
                item["uses"] -= 1
            elif item["name"] == "Signal Flare" and "Energy Cell" in [i["name"] for i in inventory]:
                print("Used Signal Flare with Energy Cell to send a beacon! A rescue craft spots you, like the hope in 'The Catalyst!'")
                escaped = True
            else:
                print(f"Used {item['name']}... but nothing happened.")
                item["uses"] -= 1
            if item["uses"] <= 0:
                inventory.remove(item)
                print(f"{item['name']} is depleted.")
            return
    print(f"No {item_name} in inventory.")

def show_inventory():
    """Display player's inventory and energy."""
    print(f"\nEnergy: {player_energy}/5")
    if inventory:
        print("Inventory:", ", ".join([item["name"] for item in inventory]))
    else:
        print("Inventory is empty, like the void in 'Shadow of the Day.'")

def examine(item_name):
    """Examine an item in inventory or room for details."""
    for item in inventory + rooms[current_room]["items"]:
        if item["name"].lower() == item_name.lower():
            print(f"{item['name']}: Type: {item['type']}, Uses left: {item['uses']}")
            return
    print(f"No {item_name} found.")

def move_to_room(room_name):
    """Attempt to move to a new room, checking requirements."""
    global current_room
    if room_name not in rooms:
        print("No such place!")
        return
    if room_name == current_room:
        print("You're already here!")
        return
    if "requires" in rooms[room_name] and rooms[room_name]["requires"] not in [i["name"] for i in inventory]:
        print(f"You need a {rooms[room_name]['requires']} to enter the {room_name}.")
        return
    current_room = room_name
    print(f"Moved to {room_name}.")
    show_room_items()

def help_menu():
    """Display available commands."""
    print("\nCommands:")
    print("  inventory - Show your inventory and energy")
    print("  pickup <item> - Pick up an item")
    print("  drop <item> - Drop an item")
    print("  use <item> - Use an item")
    print("  examine <item> - Examine an item")
    print("  move <room> - Move to another area (wasteland, ruins, bunker)")
    print("  help - Show this menu")
    print("  quit - Exit game")

def main():
    """Main game loop."""
    global player_energy
    print("Welcome to Escape the Broken World!")
    print("In a dystopian land inspired by Linkin Park, you must survive and signal for rescue.")
    print("Type 'help' for commands.")
    show_room_items()

    while not escaped and player_energy > 0:
        # Energy decreases gradually (simulating harsh environment)
        player_energy = max(player_energy - 0.1, 1)
        if player_energy <= 1:
            print("You're too drained to continue... Game Over, fading like 'Leave Out All the Rest.'")
            break

        try:
            command = input("\n> ").strip().lower()
            if command == "quit":
                print("Thanks for playing!")
                break
            elif command == "help":
                help_menu()
            elif command == "inventory":
                show_inventory()
            elif command.startswith("pickup "):
                pick_up(command[7:])
            elif command.startswith("drop "):
                drop(command[5:])
            elif command.startswith("use "):
                use(command[4:])
            elif command.startswith("examine "):
                examine(command[8:])
            elif command.startswith("move "):
                move_to_room(command[5:])
            else:
                print("Unknown command. Type 'help' for commands.")
        except KeyboardInterrupt:
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()
