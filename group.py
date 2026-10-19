"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...



class Node:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
        self.relationship = []
    def set_relationship(self, relationship, other):
        self.relationship.append([other, relationship])
        return f"{self.name} is {relationship} with {other.name}"
    def describe(self):
        if self.relationship == []:
            return f"{self.name} is {self.age}, a {self.job} and has no relationships."
        str = ""
        for i in self.relationship:
            str += f"and {self.name} is {i[0].name}'s {i[1]}. "

        return f"{self.name} is {self.age}, a {self.job} and {str}"
Jill = Node("Jill", 26, "Biologist")
Zalika = Node("Zalika", 28, "Artist")
John = Node("John", 27, "Writer")
Nash = Node("Nash", 34, "Chef")

Jill.set_relationship("friends", Zalika)
Jill.set_relationship("partner", John)
Zalika.set_relationship("friend", Jill)
John.set_relationship("partner", Jill)
Nash.set_relationship("cousin", John)
Nash.set_relationship("landlord", Zalika)

my_group = [Jill, Zalika, John, Nash]

for person in my_group:
    print(person.describe())