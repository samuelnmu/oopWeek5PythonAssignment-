class Car:
    def __init__ (self, brand, model, color,year):
        self.brand = brand
        self.mode = model
        self.color = color
        self.year = year

#Object
machine = Car("Benz", "GLC", "Mate", 2024)

print(f"My dream car is {machine.mode}")