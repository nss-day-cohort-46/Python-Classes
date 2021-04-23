from bathroom import BathRoom
from kitchen import Kitchen
from living_room import LivingRoom


class Studio:
    def __init__(self, lr, kitchen, br):
        # classes can hold instances of other classes as variables (Composition)
        # A Studio has a Living Room vs. Studio is a type of Living Room
        # TODO: Create variables for living room, kitchen, and bedroom
        self.living_room = lr
        self.kitchen = kitchen
        self.bathroom = br
        

    def turn_on_living_room_lights(self):
        self.living_room.turn_on_lights()

    def __str__(self):
        return "Studio instance"


living_room = LivingRoom(4, 6, 7)
kitchen = Kitchen(3, 4, 5, True)
bathroom = BathRoom(2, 4, 5)

studio = Studio(living_room, kitchen, bathroom)
print(studio.kitchen.appliances)
studio.turn_on_living_room_lights()
print(studio.living_room.lights)

