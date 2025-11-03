from __future__ import annotations
from copy import copy, deepcopy

#use the code from academis.eru to implement the planet class
# and create the 5 planets from the game here
# run this file.

# optional: implement the show_connections() method
# hing: copy the loop from space_game.py (close to the bottom, before the input())

class Planet:
    """
    A location in the space game
    """
    def __init__(self, name:str, description: str):
        self.name = name
        self.description = description
        self.connections: list[Planet] = []

    def __repr__(self) -> str:
        return f"Planet(name={self.name}, description={self.description})"
    
    def __del__(self): #this is called automatically (not implementation needed)
        print(f"Planet {self.name} is being deleted")

    def add_connection(self, planet):
        """adds another connection"""
        self.connections.append(planet)

    def show_connections(self):
        """
        prints a menu with all connected planets        
        """
        # ...
        print("Connections from", self.name)
        for i, planet in enumerate(self.connections, start=1):
            print(f"[{i}] {planet.name}")   

planets2={
        "earth": Planet("Earth", "You are on Earth. The stars are waiting for you."),
        "centauri": Planet("Alpha Centauri", "You are on Alpha Centauri. All creatures are welcome here."),
        "sirius": Planet("Sirius", "You are on Sirius. The system is full of media companies and content delivery networks."),
        "earth1": Planet("Earth1", "You are on Earth1. Beautiful is better than ugly."),
        "jupiter": Planet("Jupiter", "You are on Jupiter. Giant planet with a red spot.")
    }

def __main__():
    earth = Planet("Earth", "You are on Earth. The stars are waiting for you.")
    centauri = Planet("Alpha Centauri", "You are on Alpha Centauri. All creatures are welcome here.")
    sirius = Planet("Sirius", "You are on Sirius. The system is full of media companies and content delivery networks.")
    earth1 = Planet("Earth1", "You are on Earth1. Beautiful is better than ugly.")
    jupyter = Planet("Jupiter", "You are on Jupiter. Giant planet with a red spot.")
    print(earth.name, earth.description)
    print(earth)
    # earth.show_connections()
    other= copy(earth) #shallow copy, does not copy .connections

    other.name = "mars"

    print(other.name, other.description)
    print('\n')
    other.__repr__()
    # earth.add_connection(centauri)
    # earth.add_connection(sirius)
    # earth.show_connections()

    # centauri.add_connection(earth)
    # centauri.add_connection(sirius) 
    # centauri.add_connection(earth1)
    # centauri.add_connection(jupyter)    
    # centauri.show_connections()

    # planets= {
    #     "earth": earth,
    #     "centauri": centauri,
    #     "sirius": sirius,
    #     "earth1": earth1,
    #     "jupiter": jupyter
    # }

    # for name, planet in planets.items():
    #     print(f"Planet {name} description: {planet.description}")
    
    # print(planets.items())

    # planets2={
    #     "earth": Planet("Earth", "You are on Earth. The stars are waiting for you."),
    #     "centauri": Planet("Alpha Centauri", "You are on Alpha Centauri. All creatures are welcome here."),
    #     "sirius": Planet("Sirius", "You are on Sirius. The system is full of media companies and content delivery networks."),
    #     "earth1": Planet("Earth1", "You are on Earth1. Beautiful is better than ugly."),
    #     "jupiter": Planet("Jupiter", "You are on Jupiter. Giant planet with a red spot.")
    # }
    # planets2_list= list(planets2.values())
    # for planet in planets2_list:
    #     print(f"Planet {planet.name} description: {planet.description}")

    # print(list(planets2.items()))

__main__()