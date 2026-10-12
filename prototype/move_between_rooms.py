"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


# TODO:rooms = {
    "Front Door": {"East": "Hallway"},
	"Hallway" :{"West" : "Front Door", "South" : "Kitchen"},
 	"Kitchen": {"North" : "Hallway","East": "Cellar"},
    "Cellar": {"West": "Kitchen","South": "Armory"},
    "Armory": {"North": "Armory" ,"West","Award Room"},
    "Award Room": {"East" : "Award Room","West":"Master Bedroom"},
    "Master Bedroom": {"East": "Master Bedroom","East": "Dragon Chamber"},
    "Dragon Chamber": {"South": "Dragon Dungeon"},
    "Dragon Dungeon": {}
}
 
current_room = "Front Door"
 
while current_room != "Dragon Dungeon":
    print("\nYou are in the", current_room)
 
    direction = input(
        "Enter a direction (North, South, East, West): "
    ).strip().title()
    if direction == "Exit":
      break 
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
    else:
        print("You cannot go that way.")
 
print("\nYou are in the Dragon Dungeon!")
print("You have reached the dragon!")


# TODO: Run and debug all milestone cases in prototype/README.md.
