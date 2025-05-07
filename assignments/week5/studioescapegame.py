inventory = []
items_in_room = [
    {"name": "Guitar", "type": "instrument", "description": "A classic electric guitar used in 'Numb'."},
    {"name": "Microphone", "type": "tool", "description": "Capture your vocals like Chester."},
    {"name": "Energy Drink", "type": "food", "description": "Restores your focus."},
    {"name": "Lyrics Sheet", "type": "tool", "description": "Lyrics to an unreleased song."},
    {"name": "Hybrid Key", "type": "key", "description": "Unlocks the studio exit."},
    {"name": "Drumsticks", "type": "instrument", "description": "Used by Rob during live sessions."},
    {"name": "Pizza Slice", "type": "food", "description": "Because even legends need a break."}
]
MAX_INVENTORY_SIZE = 5


def show_inventory():
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Inventory:")
        for item in inventory:
            print(f"- {item['name']}")

def show_room_items():
    if not items_in_room:
        print("There are no items in this room.")
    else:
        print("Items in the room:")
        for item in items_in_room:
            print(f"- {item['name']}")

def pick_up(item_name):
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Inventory full. Drop something before picking up new items.")
        return
    for item in items_in_room:
        if item["name"].lower() == item_name.lower():
            inventory.append(item)
            items_in_room.remove(item)
            print(f"You picked up: {item['name']}")
            return
    print("That item is not in the room.")

def drop(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            inventory.remove(item)
            items_in_room.append(item)
            print(f"You dropped: {item['name']}")
            return
    print("You don't have that item in your inventory.")

def use(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            if item["type"] == "food" or item["type"] == "healing":
                print(f"You used the {item['name']}. You feel refreshed!")
                inventory.remove(item)
            elif item["type"] == "tool":
                print(f"You used the {item['name']} – maybe it did something.")
            elif item["type"] == "clue":
                print(f"You study the {item['name']} – it might be part of a lost track.")
            else:
                print("You can't use that item right now.")
            return
    print("You don't have that item.")

def examine(item_name):
    all_items = inventory + items_in_room
    for item in all_items:
        if item["name"].lower() == item_name.lower():
            print(f"{item['name']}: {item.get('description', 'No description available.')}")
            return
    print("You can't see that item here or in your inventory.")


def game_loop():
    print("🎧 Welcome to 'Escape the Studio – Linkin Park Lost Tracks'!")
    print("Find the lost lyrics and escape before security shows up.")
    print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], quit")
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            item_name = command[7:]
            pick_up(item_name)
        elif command.startswith("drop "):
            item_name = command[5:]
            drop(item_name)
        elif command.startswith("use "):
            item_name = command[4:]
            use(item_name)
        elif command.startswith("examine "):
            item_name = command[8:]
            examine(item_name)
        elif command == "quit":
            print("Thanks for playing! Don't let the studio eat you alive 🎤")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()
