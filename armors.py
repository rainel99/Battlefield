from abc import ABCMeta, abstractmethod
# def mi_decorador(funcion_original):
#     def funcion_envolvente(*args, **kwargs):
#         print("Código antes de la funcion_original()")
#         funcion_original(*args, **kwargs)
#         print("Código después de la funcion_original()")
#     return funcion_envolvente
from random import randint


class BassicArmor(object):
    __metaclass__ = ABCMeta

    def __init__(self, price) -> None:
        self.price = price

    @abstractmethod
    def dress_soldier(self, soldier):
        pass

    def __repr__(self) -> str:
        return type(self).__name__

# archer, gladiator, squire, Swordsman,lancers


class ArcherArmor(BassicArmor):
    def __init__(self, price) -> None:
        super().__init__(price)

    def dress_soldier(self, soldier):
        soldier.attack_range += 15

    def __repr__(self) -> str:
        return super().__repr__()


class GladiatorArmor(BassicArmor):
    def __init__(self, price) -> None:
        super().__init__(price)

    def dress_soldier(self, soldier):
        soldier.attack += 20
        soldier.defense += 20

    def __repr__(self) -> str:
        return super().__repr__()


class SquireArmor(BassicArmor):
    def __init__(self, price) -> None:
        super().__init__(price)

    def dress_soldier(self, soldier):
        soldier.defense += 60

    def __repr__(self) -> str:
        return super().__repr__()


class SwordsmanArmor(BassicArmor):
    def __init__(self, price) -> None:
        super().__init__(price)

    def dress_soldier(self, soldier):
        soldier.attack += 70
        soldier.speed += 7

    def __repr__(self) -> str:
        return super().__repr__()


class LancersArmor(BassicArmor):
    def __init__(self, price) -> None:
        super().__init__(price)

    def dress_soldier(self, soldier):
        soldier.attack_range += 3
        soldier.attack += 5

    def __repr__(self) -> str:
        return super().__repr__()


armors = [ArcherArmor(50), GladiatorArmor(70),
          SquireArmor(30), SwordsmanArmor(60), LancersArmor(35)]
min_price = min(armors, key=lambda armor: armor.price)


def buy_random_armors(armors: list[BassicArmor], actual_money):
    copy_armors = armors.copy()
    while len(copy_armors) > 0:
        r = randint(0, len(copy_armors) - 1)
        if copy_armors[r].price <= actual_money:
            return copy_armors[r].price, copy_armors[r]


def dress_army(solider_list, price, min_price):
    arms = []
    while price > min_price:
        p, armor = buy_random_armors(armors, price)
        price -= p
        arms.append(armor)
    for i, ar in enumerate(arms):
        solider_list[i].armor = ar
        solider_list[i].use_armor()
