# Classes are a blueprint
class Room:
    # Variables outside of the init can be accessed by the class or the instance
    lights = 'on'
    has_ceiling = True
    __wall_color = 'White'
    

    def __init__(self, l, w, win):
        # __init__ is the class constructor that runs when a class instance is created
        # Variables that can change between instances can be set in the __init__
        self.length = l
        self.windows = win
        self.width = w

    # There are 3 types of methods

    # Instance Methods
    # Must have self as the first argument
    # Can update a single instances state
    def turn_on_lights(self):
        self.lights = 'on'


    # Class Methods
    # Must take cls as the first argument and have @classmethod decorator
    # Can update every instances state
    @classmethod
    def turn_off_all_lights(cls):
        cls.lights = 'off'
        
   
        

    # Static Methods
    # Cannot update class or instance state
    # Must have @staticmethod decorator
    @staticmethod
    def description():
        return "Has length, width, and windows"


    
    # Classes can have properties with getters and/or setters
    # Getters must have the @property decorator
    @property
    def area(self):
        return self.length * self.width
    
    # Does the same thing as the area property
    # Only difference is how the function or property is called
    # check out lines 76 and 77
    def calc_area(self):
        return self.length * self.width
    

    
    @property
    def paint_the_walls(self):
        print('Getting the wall color')
        return self.__wall_color

    
    def overwrite_this_one(self):
        print("running from the parent")

    
    # Setters must have a @<property name>.setter decorator
    @paint_the_walls.setter
    def paint_the_walls(self, color):
        print("painting the walls " + color)
        self.__wall_color = color

room1 = Room(3, 4, 2)
room2 = Room(3, 4, 5)
room1.area
room1.calc_area()

room1.paint_the_walls = 'Blue'
print(room1.paint_the_walls)
room2.paint_the_walls = "White"

print(room1.description())
print(Room.description())

# Turns off the lights for every Room instance
Room.turn_off_all_lights()

# Just turns the lights on in room1
room1.turn_on_lights()

