class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (f"Property at {self.address}, Area: {self.area} sqm, "
                f"Rooms: {self.rooms}, Price: ${self.price}")

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"House at {self.address}, Area: {self.area} sqm, Rooms: {self.rooms}, "
                f"Price: ${self.price}, Plot Size: {self.plot} sqm")

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Flat at {self.address}, Area: {self.area} sqm, Rooms: {self.rooms}, "
                f"Price: ${self.price}, Floor: {self.floor}")

house = House(area=120, rooms=5, price=350000, address="123 Maple Street", plot=500)
flat = Flat(area=70, rooms=3, price=200000, address="456 Oak Avenue", floor=3)

print(house)
print(flat)
