"""
Python Descriptor Example

Descriptors are objects that define how attributes are accessed, set, or deleted.
They implement one or more of: __get__, __set__, __delete__
"""


class Descriptor:
    """A simple descriptor that logs attribute access"""
    
    def __init__(self, name=None):
        self.name = name
    
    def __set_name__(self, owner, name):
        """Called when the descriptor is assigned to a class attribute"""
        self.name = name
    
    def __get__(self, obj, objtype=None):
        """Called when the attribute is accessed"""
        if obj is None:
            return self
        print(f"Getting {self.name}")
        return obj.__dict__.get(self.name, None)
    
    def __set__(self, obj, value):
        """Called when the attribute is set"""
        print(f"Setting {self.name} to {value}")
        obj.__dict__[self.name] = value
    
    def __delete__(self, obj):
        """Called when the attribute is deleted"""
        print(f"Deleting {self.name}")
        del obj.__dict__[self.name]


class ValidatedDescriptor:
    """A descriptor that validates the value before setting it"""
    
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, None)
    
    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.name} must be a number")
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be at least {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be at most {self.max_value}")
        obj.__dict__[self.name] = value


class Person:
    """Example class using descriptors"""
    name = Descriptor()
    age = ValidatedDescriptor(min_value=0, max_value=150)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Example usage
if __name__ == "__main__":
    print("=== Basic Descriptor Example ===")
    person = Person("Alice", 30)
    print(f"Name: {person.name}")
    print(f"Age: {person.age}")
    
    print("\n=== Changing values ===")
    person.name = "Bob"
    person.age = 25
    
    print("\n=== Validation Example ===")
    try:
        person.age = 200  # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        person.age = "thirty"  # This will raise an error
    except TypeError as e:
        print(f"Error: {e}")
    
    print("\n=== Property-based Descriptor ===")
    # Python's @property is actually a descriptor!
    
    class Circle:
        def __init__(self, radius):
            self._radius = radius
        
        @property
        def radius(self):
            """The radius property is a descriptor"""
            return self._radius
        
        @radius.setter
        def radius(self, value):
            if value < 0:
                raise ValueError("Radius cannot be negative")
            self._radius = value
        
        @property
        def area(self):
            """Computed property using descriptor"""
            return 3.14159 * self._radius ** 2
    
    circle = Circle(5)
    print(f"Circle radius: {circle.radius}")
    print(f"Circle area: {circle.area:.2f}")
    
    circle.radius = 10
    print(f"New radius: {circle.radius}")
    print(f"New area: {circle.area:.2f}")
