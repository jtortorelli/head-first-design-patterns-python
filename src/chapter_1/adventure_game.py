class Character:
    def __init__(self):
        self.weapon_behavior = None

    def set_weapon(self, weapon_behavior):
        self.weapon_behavior = weapon_behavior

    def fight(self):
        self.weapon_behavior.use_weapon()


class Queen(Character):
    def __init__(self):
        super().__init__()
        self.weapon_behavior = KnifeBehavior()


class King(Character):
    def __init__(self):
        super().__init__()
        self.weapon_behavior = BowAndArrowBehavior()


class Troll(Character):
    def __init__(self):
        super().__init__()
        self.weapon_behavior = AxeBehavior()


class Knight(Character):
    def __init__(self):
        super().__init__()
        self.weapon_behavior = SwordBehavior()


class WeaponBehavior:
    def use_weapon(self):
        raise NotImplementedError


class KnifeBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Stabby stab stab")


class BowAndArrowBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Thwing!")


class AxeBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Whack!")


class SwordBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Thrust!")


knight = Knight()
king = King()
queen = Queen()
troll = Troll()
knight.fight()
king.fight()
queen.fight()
troll.fight()
