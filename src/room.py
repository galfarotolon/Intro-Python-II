
# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, item=[]):
        self.name = name
        self.description = description
        self.item = item
    
    def __str__(self):
        return f"you are in {self.name}, {self.description}"

    def print_items(self):
        for i,  p in enumerate(self.item):
            print(f"{i+1} - {p}")

    def add_item(self, item):
        self.append(item)

    def remove_item(self, item):
        self.remove(item)

  