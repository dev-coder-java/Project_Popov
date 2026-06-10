#Создаите базовый класс "Животное" со своиствами вид", количество лап", цвет
#шерсти". От этого класса унаследуйте класс "Собака" и добавьте в него свойства
#"кличка" и "порода".
class Animal:
    def __init__(self, species, num_legs, fur_color):
        self.species = species
        self.num_legs = num_legs
        self.fur_color = fur_color

    def __str__(self):
        return f"Species: {self.species}, Legs: {self.num_legs}, Fur color: {self.fur_color}"


class Dog(Animal):
    def __init__(self, species, num_legs, fur_color, name, breed):
        super().__init__(species, num_legs, fur_color)
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"{super().__str__()}, Name: '{self.name}', Breed: {self.breed}"


my_dog = Dog("Dog", 4, "White", "Bobik", "homeless")
print(my_dog)