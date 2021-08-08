class Flower:
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements

    is_happy = False

    def water(self, amount):
        if amount >= self.water_requirements:
            self.is_happy = True
        else:
            self.is_happy = False

    def status(self):
        if self.is_happy is True:
            return f"{self.name} is happy"
        elif self.is_happy is False:
            return f"{self.name} is not happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
