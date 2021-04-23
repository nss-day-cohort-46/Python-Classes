from room import Room

# Classes can Inherit from other classes
# When Kitchen inherits from Room, we're saying a Kitchen is a type of Room
class Kitchen(Room):
    appliances = ['fridge', 'oven', 'dishwasher']

    def __init__(self, l, w, win, has_electric_oven):
        # Calling the parent's init will set the length, width, and number of windows on the kitchen instance
        super().__init__(l, w, win)
        self.has_electric_oven = has_electric_oven

    def add_appliance(self, appliance):
        self.appliances.append(appliance)

    # Child classes can overwrite methods on the parent
    # TODO: add a method to overwrite on the parent
    def overwrite_this_one(self):
        super().overwrite_this_one()
        print('running from the child class')


kitchen1 = Kitchen(3,4,5,True)
room1 = Room(2, 3, 7)
room1.overwrite_this_one()
kitchen1.overwrite_this_one()
