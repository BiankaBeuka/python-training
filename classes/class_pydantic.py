from typing import Annotated
from pydantic import BaseModel, BeforeValidator, ValidationError

# pydantic - python library, don't require an init function, it validates the data types automatically, you can catch the errors earlier



def parse_level(level: str) -> list[list[str]]:
    return [list(row) for row in level.strip().split()]


class Level(BaseModel):
    name: str
    level: Annotated[list[list[str]], BeforeValidator(parse_level)]

    def __str__(self) -> str:
        return "\n".join("".join(row) for row in self.level)

    class Config:
        extra = "forbid"  # Disallow unknown fields


level_one = Level(
    name="empty level",
    level="""
#############
#...........#
#...........#
#...........#
#...........#
#...........#
#...........#
#...........#
#...........#
#...........#
#...........#
#############""", # type: ignore
)
class Planet(BaseModel):
    name: str
    description: str
    connections: list[str] = []

    class Config:
        extra = "forbid"  # Disallow unknown fields

planet = Planet(
    name="Earth",
    description="You are on Earth. The stars are waiting for you.",
    connections=["Alpha Centauri", "Sirius"]
)

print(planet)



planet2= Planet(name='ee', description="You are on Earth. The stars are waiting for you.", connections=['a']) #this will raise an error because name should be str
print(planet2)

data = planet2.model_dump() # converts to dictionary
print(data)

planet3=Planet(**data) #unpacking the dictionary
print('\nplanet3',planet3)

planet2.model_dump_json() #converts to json
print('\nplanet2 json', planet2.model_dump_json())



