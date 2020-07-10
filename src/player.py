# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room
from item import Item


class Player:
    def __init__(self, player_name, current_room, inventory=[] ):
        self.player_name = player_name
        self.current_room = current_room
        self.inventory = inventory
        
    def __str__(self):
        return f"\nWelcome {self.player_name}! You find yourself {self.current_room.name} {self.current_room.description}"

#    def take_item(self, item):
#         self.inventory.append(item)
#         print(f"You picked up an {item}")

    # def take_item(self, item):
    #     self.inventory.append(item)
    #     print(f"You picked up: {item}")

    def drop_item(self, item):
        self.inventory.remove(item)
        print(f"You dropped: {item}")
    
    def check_inventory(self):
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f'You have {len(self.inventory)} items in your inventory: {item}.')
        else:
            print("Nothing in your inventory right now!")

    # def inspect(self):
    #     for item in self.inventory:
    #         print(f'{item}')

    # def inventory_status(self):
    #     print(f"Items in inventory: ")
    #     for p in self.inventory:
    #         p.print_item()

    def take_item(self, item, room):

        item_is_taken = input(f"You can pick up items by typing 'take' followed by the item's name: ").split(' ')

        # print("items in inventory: ")
        # for i in self.inventory:
        #     i.print_name()

        # self.inventory.append(item)
        # print(f"You picked up: {item}")
    

        if item_is_taken[0] == 'take':
            self.inventory.append(item_is_taken[1])
        elif item_is_taken[0] == 'drop':
            self.inventory.remove(item_is_taken[1])
        else:
            print('The item is left behind. You continue your quest.')
        
        if len(self.inventory) > 0:
            print(f"items in inventory: {self.inventory}")