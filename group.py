"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = [Jill, Zalika, John, Nash]

class Node:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
    def relationship(self, relationship, other):
        self.relationship = other
        return f"{self.name} is {relationship} with {other.name}"

Jill = Node("Jill", 26, "Biologist")
Zalika = Node("Zalika", 28, "Artist")
John = Node("John", 27, "Writer")
Nash = Node("Nash", 34, "Chef")

Jill.relationship("friends", Zalika)
Jill.relationship("partner", John)
Zalika.relationship("friend", Jill)
John.relationship("partner", Jill)
Nash.relationship("cousin", John)
Nash.relationship("landlord", Zalika)

