class Duck:
    def __init__(self):
        self.quack_behavior = None
        self.fly_behavior = None

    def set_fly_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def display(self):
        raise NotImplementedError

    def swim(self):
        print("All ducks float, even decoys!")


class MallardDuck(Duck):
    def display(self):
        print("I'm a real Mallard duck")

    def __init__(self):
        super().__init__()
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWings()


class ModelDuck(Duck):

    def __init__(self):
        super().__init__()
        self.quack_behavior = Quack()
        self.fly_behavior = FlyNoWay()

    def display(self):
        print("I'm a model duck")


class FlyBehavior:
    def fly(self):
        raise NotImplementedError


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!!")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")


class QuackBehavior:
    def quack(self):
        raise NotImplementedError


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")


mallard = MallardDuck()
mallard.perform_quack()
mallard.perform_fly()

model = ModelDuck()
model.perform_fly()
model.set_fly_behavior(FlyRocketPowered())
model.perform_fly()