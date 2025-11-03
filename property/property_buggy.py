"""
the program contains 3 bugs
"""
class Game:

    name = "Pac using OpenCV"

    level: list[str] = [
        "######",
        "#....#",
        "#....#",
        "#....#",
        "######" ,       
    ]

    @property
    def remaining_dots(self) -> int:
        return sum(
            [row.count(".") for row in self.level]
        )

    @property
    def finished(self):
        return self.remaining_dots == 0
    
    @classmethod
    def get_name(cls):
        return cls.name
    
    # does not have any argument, does not depend on class or instance, it can be used to group functions inside a class
    # @staticmethod
    @staticmethod 
    def version():
        return "1.0"

    # @property
    # def version(self):
    #     return "1.0"


game = Game()

print(game.get_name())
print("version", game.version())
print("dots remaining:", game.remaining_dots) # no need to have (), because is annotated as property, dynamic attribute
print("finished:", game.finished)
