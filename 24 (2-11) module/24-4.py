class Parent:
    children = []

    def __init__(self, name: str, age: int, children):
        self.name = name
        self.age = age
        for child in children:
            if age - child.age >= 16:
                self.children.append(child)

    def __str__(self):
        return self.name + ' ' + str(self.age) + '\n' + '\n'.join(str(child) for child in self.children)

    def calm_child(self, other_child):
        for child in self.children:
            if child is other_child:
                child.calm = True

    def feed_child(self, other_child):
        for child in self.children:
            if child is other_child:
                child.hunger = True


class Child:
    def __init__(self, name: str, age: int, calm: bool, hunger: bool):
        self.name = name
        self.age = age
        self.calm = calm
        self.hunger = hunger
