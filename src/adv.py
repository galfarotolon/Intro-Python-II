from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

player_name = input(f"Hello adventurer! Please enter  your name to continue: ")

# Make a new player object that is currently in the 'outside' room.

new_player = Player(player_name, current_room=room['outside'])

print(new_player)


# Write a loop that:

# * Prints the current description (the textwrap module might be useful here).



# Print an error message if the movement isn't allowed.
#


while True:
 
 
    # * Waits for user input and decides what to do.

    direction = input("Which direction do you want to go next? Please enter 'n', 'e', 's' or 'w':  ")

# If the user enters "q", quit the game.

    if direction == 'q':
        break
    
    # If the user enters a cardinal direction, attempt to move to the room there.
    elif direction == 'n':
        new_player.current_room = room['outside'].n_to

           # * Prints the current room name
        print(f"You enter the {new_player.current_room.name}, {new_player.current_room.description}")


    else:
        print("That is not a valid command. Please enter 'n', 'e', 's' or 'w' to keep playing, or 'q' to quit your adventure.")

    

