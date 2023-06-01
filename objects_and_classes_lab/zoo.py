class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):

        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)} \n" \
                    f"Total animals: {Zoo.__animals}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)} \n" \
                    f"Total animals: {Zoo.__animals}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)} \n" \
                   f"Total animals: {Zoo.__animals}"



name_zoo = input()
zoo = Zoo(name_zoo)
numbers = int(input())

for x in range(numbers):
    animal = input().split(" ")
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))



