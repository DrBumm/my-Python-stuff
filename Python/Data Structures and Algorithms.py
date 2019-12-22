# Data Structures and Algorithms

class Maps:
    """
    We want to make a system that works similar to google maps
    Here our map:

    Store a --> Store B ---- School
      | |--------^/^ |            |
     Home ------ Park ----> Intersection

    Street :
        - = Left and right
        / = Slant straight on and back
        | = Up and back

        -> = Only right
        |^ = Only up
        ^/^ = Only diagonally straight on but only if your target where it pointing
        <- = Only left
        ^| = Only back
        ^/ = Only only diagonally back

    coordinates: 
        location : coordinates

        Home : 2.0, 0.0
        Store a : 2.0, 1.0
        Store b : 1.0, 1.0
        School : 0.0, 1.0
        Intersection : 0.0, 0.0
    
    Possibilities from 1 point to another:
        Home to Store a
        Store a to Home
        Home to Store b
        Store a to Store b
        Store b to School
        School to Store b
        School to Intersection
        Intersection to School
        Home to Intersection
    Shorter:
        Home:          Store a, Store b, Intersection
        Store a:       Home, Store b
        Store b:       School
        School:        Store b, Intersection
        Intersection:  School
        
    Your task:
        Make a system that shows me the shortest path from input 1 to input 2 and if it would go at all.
        And make your own Docstring that explains much what you do in your code!
        The input should not always be the same
    """
    
    def __init__(self):
        self.coordinates = {
            "Home": (2.0, 0.0),
            "Park": (1.0, 0.0),
            "Store a": (2.0, 1.0),
            "Store b": (1.0, 1.0),
            "School": (0.0, 1.0),
            "Intersection": (0.0, 0.0)
        }
        self.buildings = {
            (2.0, 0.0): "Home",
            (1.0, 0.0): "Park",
            (2.0, 1.0): "Store a",
            (1.0, 1.0): "Store b",
            (0.0, 1.0): "School",
            (0.0, 0.0): "Intersection"
        }
        self.possibilities = {
            "Home": ["Store a", "Store b", "Intersection", "School"],
            "Store a": ["Home", "Store b", "Intersection", "School"],
            "Store b": ["School", "Intersection"],
            "School": ["Store b", "Intersection"],
            "Intersection": ["School", "Store b"]
        }
    
    def get_way(self, start_point, end_point):
        if end_point in self.possibilities[start_point]:
            print("Way is possible.\nCoordinates of start point: " +
                  str(self.coordinates[start_point]) + "\nCoordinates of end point: " + str(self.coordinates[end_point]))
            
            i = self.coordinates[start_point]
            f = self.coordinates[end_point]
            while True:
                if i[0] == f[0]:
                    a=1
                elif start_point == "Home" and end_point == "Store b":
                    # Yaaay from Home to Store b works jet Yaaay ... i should use my knowlegde about python but i'm 
                    i = (i[0]-1, i[1]+1)
                    print("Go to " + self.buildings[i])
                elif i[0] > f[0]:
                    i = (i[0]-1, i[1])
                    print("Go to " + self.buildings[i])
                else:
                    i = (i[0]+1, i[1])
                    print("Go to " + self.buildings[i])

                if i[1] == f[1]:
                    a=1
                elif i[1] > f[1]:
                    i = [i[0], i[1]-1]
                    print("Go to " + self.buildings[i])
                else:
                    i = (i[0], i[1]+1)
                    print("Go to " + self.buildings[i])

                if i[0] == f[0] and i[1] == f[1]:
                    print("You have reached the finish")
                    return "200 Found"
            
        else:
            print("Way isn't possible")
            return "403 Forbidden"
        
    def display_map(self):
        print("""
            MAP:
            
            Store a --> Store B ---- School
            | |--------^/^ |            |
            Home ------ Park ----> Intersection
            """)

new_map = Maps()
#new_map.get_way("Home", "School")
#new_map.display_map()
while True:
    print("[1]Find way\n[2]Show Map\n[3]Exit")
    choice = int(input())
    if choice == 1:
        print("Where do you want to start?\nHome, Store a, Store b, School, Park, Intersection")
        choice = input()
        print("Where do you want to go:\nHome, Store a, Store b, School, Park, Intersection")
        choice2 = input()
        new_map.get_way(choice, choice2)
    elif choice == 2:
        new_map.display_map()
    elif choice == 3:
        break
