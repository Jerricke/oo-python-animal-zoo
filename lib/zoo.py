class Zoo:
    all_zoo = []

    def __init__(self, name, location):
        self.name = name
        self.location = location
        Zoo.all_zoo.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if isinstance(value, str):
            self._location = value

    def animal_species(self):
        # result = []
        # for animal in Animal.all_animal:
        #     if animal.zoo == self.name:
        #         result.append(animal.species)
        # return set(result)

        return set(
            [animal.species for animal in Animal.all_animal if animal.zoo == self.name]
        )

    pass

    def find_by_species(self, target):
        res = []
        for animal in Animal.all_animal:
            if animal.zoo == self.name:
                if animal.species == target:
                    res.append(animal)
        return res

    def animal_nicknames(self):
        # res = []
        # for animal in Animal.all_animal:
        #     if animal.zoo == self.name:
        #         res.append(animal.nickname)
        # return res
        return [
            animal.nickname for animal in Animal.all_animal if animal.zoo == self.name
        ]

    @classmethod
    def find_by_locations(cls, target):
        res = []
        for zoo in cls.all_zoo:
            if zoo.location == target:
                res.append(zoo)
        return res


if __name__ == "__main__":
    import ipdb
    from animal import Animal

    zoo1 = Zoo("Denver Zoo", "Denver")
    zoo2 = Zoo("LA Zoo", "LA")
    zoo3 = Zoo("Flatiron Zoo", "Denver")
    animal1 = Animal("Dog", 10, "Doggo", "Denver Zoo")
    animal2 = Animal("Cat", 10, "Catto", "Denver Zoo")
    animal3 = Animal("Cat", 10, "Kitty", "Denver Zoo")
    animal4 = Animal("Cat", 10, "Kiten", "LA Zoo")
    animal5 = Animal("Sheep", 10, "SheepDog", "Denver Zoo")
    animal6 = Animal("Dog", 10, "Doggers", "LA Zoo")

    ipdb.set_trace()
