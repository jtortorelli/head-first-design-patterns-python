class Beverage:
    def __init__(self):
        self.description = "Unknown Beverage"

    def get_description(self):
        return self.description

    def cost(self):
        raise NotImplementedError


class CondimentDecorator(Beverage):

    def get_description(self):
        raise NotImplementedError

    def cost(self):
        raise NotImplementedError


class Espresso(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "Espresso"

    def cost(self):
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "House Blend Coffee"

    def cost(self):
        return 0.89


class Decaf(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "Decaf"

    def cost(self):
        return 1.05


class DarkRoast(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "Dark Roast"

    def cost(self):
        return 0.99


class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return 0.20 + self.beverage.cost()


class Soy(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def cost(self):
        return 0.15 + self.beverage.cost()


class Whip(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Whip"

    def cost(self):
        return 0.10 + self.beverage.cost()


class SteamedMilk(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Steamed Milk"

    def cost(self):
        return 0.10 + self.beverage.cost()


b = Espresso()
print(f"{b.get_description()} ${b.cost()}")
b2 = DarkRoast()
b2 = Mocha(b2)
b2 = Mocha(b2)
b2 = Whip(b2)
print(f"{b2.get_description()} ${b2.cost()}")
b3 = HouseBlend()
b3 = Soy(b3)
b3 = Mocha(b3)
b3 = Whip(b3)
print(f"{b3.get_description()} ${b3.cost()}")
