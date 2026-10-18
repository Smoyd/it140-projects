"""Project Two starter for the student's text-based adventure game."""

# TODO: Add the full-name comment required by Project Two directions.


def show_instructions():
    """Display the game objective and available commands."""
    print("Welcome to Halloween Dragon Face-Off!")
    print("Collect all 6 items before entering the Dragon Dungeon.")
    print("If you enter the dungeon without all 6 items, you lose.")
    print("Commands:")
    print("  go North")
    print("  go South")
    print("  go East")
    print("  go West")
    print("  get item name")
    print("  exit")


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print("\n")
    print("You are in the", current_room)
    print("Inventory:", inventory)

    if rooms[current_room]["item"] is not None:
        print("You see:", rooms[current_room]["item"])

    print("")


def main():
    """Run the main gameplay loop."""

    # Create the room dictionary.
    rooms = {
        "Front Door": {
            "East": "Hallway",
            "item": None
        },
        "Hallway": {
            "West": "Front Door",
            "South": "Kitchen",
            "item": "Flashlight"
        },
        "Kitchen": {
            "North": "Hallway",
            "East": "Cellar",
            "item": "Healing Potion"
        },
        "Cellar": {
            "West": "Kitchen",
            "South": "Armory",
            "item": "Dragonfire Antidote"
        },
        "Armory": {
            "North": "Cellar",
            "West": "Award Room",
            "item": "Dragon-Slaying Sword"
        },
        "Award Room": {
            "East": "Armory",
            "West": "Master Bedroom",
            "item": "Magic Shield"
        },
        "Master Bedroom": {
            "East": "Award Room",
            "South": "Stairwell",
            "item": "Dragon Key"
        },
        "Stairwell": {
            "North": "Master Bedroom",
            "East": "Dragon Dungeon",
            "item": None
        },
        "Dragon Dungeon": {
            "West": "Stairwell",
            "item": None
        }
    }

    # Set the player's starting room.
    current_room = "Front Door"

    # Create the player's inventory.
    inventory = []

    # Set the number of items needed to win.
    total_items = 6

    # Display the game instructions.
    show_instructions()

    # Create the gameplay loop.
    while True:
        show_status(current_room, inventory, rooms)

        # Check whether the player has reached the dragon.
        if current_room == "Dragon Dungeon":
            if len(inventory) == total_items:
                print("Congratulations! You have collected all items")
                print("and defeated the dragon!")
                print("Thanks for playing the game. Hope you enjoyed it.")
            else:
                print("Oh no! You entered the Dragon Dungeon")
                print("without collecting all 6 items.")
                print("The dragon has defeated you!")
                print("Game over. Thanks for playing.")
            break

        # Get the player's next command.
        command = input(
            "Enter your command: "
        ).strip()

        # Allow the player to exit the game.
        if command.lower() == "exit":
            print("Thanks for playing the game.")
            break

        # Handle movement commands.
        if command.lower().startswith("go "):
            direction = command[3:].strip().title()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You cannot go that way.")

        # Handle item collection commands.
        elif command.lower().startswith("get "):
            item_choice = command[4:].strip().lower()
            room_item = rooms[current_room]["item"]

            if room_item is not None and item_choice == room_item.lower():
                inventory.append(room_item)
                rooms[current_room]["item"] = None
                print("You picked up the", room_item + "!")
            else:
                print("That item is not in this room.")

        # Handle invalid commands.
        else:
            print("Invalid command.")
            print("Use 'go North', 'go South',")
            print("'go East', 'go West', or 'get item name'.")


if __name__ == "__main__":
    main()




