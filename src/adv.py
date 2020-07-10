from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons.", ['Sword', 'Shield']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['Lamp', 'Relic']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['Rope', 'Map']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['Cloak', 'Wand']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! The treasure piles up beyond sight, with glittering jewels and countless pieces of gold.""", ['Gold', 'Jewels']),
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

def try_direction(player, player_input):
 #check player current location

    attribute  = player_input + '_to'

    #python hasattr checks if class has attribute

    if hasattr(player.current_room, attribute):

       player.current_room =  getattr(player.current_room, attribute)

# Print an error message if the movement isn't allowed.
    else:
        print("\nThere is nothing in that direction! Try again!")


player_name = input(f"\nHello adventurer! Please enter your name to continue: ")

# Make a new player object that is currently in the 'outside' room.

player = Player(player_name, room['outside'])

possible_directions = ["n", "s", "e", "w"]




item = {
    'Sword': Item('Greatsword', 'It is heavy when you lift it.'),
    "Shield": Item("Great shield", "it is heavy when you lift it."),
    'Lamp': Item('Old Lamp', 'This lamp has a little torch left.'),
    "Relic": Item("Old Relic", "Seems like an artifact from a long time ago. Might be valuable."),
    'Rope': Item('Rope', 'Sturdy rope, could come in handy for exploring further rooms.'),
    "Map": Item("Treasure Map", "Another adventurer might have dropped this."),
    'Cloak': Item('Thick Cloak', 'Winter Cloak to shroud from cold and darkness.'),
    "Wand": Item("Mage Wand", "Powerful in the right hands."),
    'Gold': Item('Piles of Gold', 'Gold and more gold until the eye can see.'),
    "Jewels": Item("Glittering Jewels", "More than could ever fit in an adventurer's inventory."),
   
}


#Game Rules and controls:

print('\nUse the following controls to play the game:')
print('Enter [n] North [s] South [w] West [e] East to move. Enter [q] to Quit')
print('Enter [i] to check inventory, [t] to take an item, and [d] to drop item')


print(player)


while True:


 
 
    # * Waits for user input and decides what to do.

    player_input = input("\nWhat do you want to do next? ").strip().lower().split()[0]
    player_input = player_input[0]


    
# If the user enters "q", quit the game.

    if player_input[0] == 'q':
        break
    
    # If the user enters a cardinal direction, attempt to move to the room there.


    if player_input in possible_directions:
        # check to see if we can go in that direction 
        # if we can, go there 
        try_direction(player, player_input)
        print(f"\nYou enter the {player.current_room.name}, {player.current_room.description}")
        print(f'Available items: {player.current_room.item}')



      
        player.take_item(player.current_room.item, player.current_room)


    elif player_input == 'i':
        # check inventory
        player.check_inventory()
      

    else:
        print("\nThat is not a valid command. Please enter 'n', 'e', 's' or 'w' to keep playing, or 'q' to quit your adventure.")


        ## OLD CODE

    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.

    # if player_input[0] == 'n':

    #     try_direction(player, player_input)


    #        # * Prints the current room name
    #        # * Prints the current description (the textwrap module might be useful here).
    #     print(f"\nYou enter the {player.current_room.name}, {player.current_room.description}")

    # elif player_input[0] == 's':
    #     try_direction(player, player_input)

    #     print(f"\nYou enter the {player.current_room.name}, {player.current_room.description}")
    # elif player_input[0] == 'e':
    #     try_direction(player, player_input)

    #     print(f"\nYou enter the {player.current_room.name}, {player.current_room.description}")
    # elif player_input[0] == 'w':
    #     try_direction(player, player_input)

    #     print(f"\nYou enter the {player.current_room.name}, {player.current_room.description}")
    
  
