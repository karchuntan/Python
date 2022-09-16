from dataclasses import dataclass, field

# set order=True for comparison
# set frozen=True for creating objects that are read-only
# @dataclass
# @dataclass(order=True)
@dataclass(order=True, frozen=True)
class Person:
    sort_index: int = field(init=False, repr=False) # sorting

    # specify the type of variable is important to let dataclass knows what type of data it's dealing with
    name: str
    job: str
    age: int
    strength: int = 100

    # after init
    def __post_init__(self):
        # sorting by age
        self.sort_index = self.age

person1 = Person("Kar Chun", "DevOps Engineer", 23, 99)
person2 = Person("Anson", "Software Engineer", 25)
person3 = Person("Anson", "Software Engineer", 25)

print(id(person2))
print(id(person3))

# it will print representation of the object like repr
print(person1)

# it will return True, as they contain the same data
print(person3 == person2)

# Comparison - sorting by age
print(person1 > person2)
