from abc import ABC, abstractmethod
from typing import List


class WeaponBehavior(ABC):
    """
    The WeaponBehavior interface declares ways to attack of each character.
    """

    @abstractmethod
    def useWeapon(self):
        pass


class SwordBehavior(WeaponBehavior):

    def useWeapon():
        return "I am attacking with a Sword!"


class AxeBehavior(WeaponBehavior):

    def useWeapon():
        return "I am attacking with an Axe!"


class Character():

    def __init__(self, weaponBehavior: WeaponBehavior) -> None:
        """
        This Character accepts a weapon behavior through the constructor, but
        also provides a setter to change it in runtime.
        """

        self._weaponBehavior = weaponBehavior

    @property
    def useWeapon(self) -> WeaponBehavior:
        """
        The Character mantains a reference to one of the WeaponBehavior objects. The Character doesn't
        know the concrete class of a Weapon Behavior. It should work with all weapon behaviors via the
        WeaponBehavior Interface. 
        """

        return self._weaponBehavior.useWeapon()

    @useWeapon.setter
    def useWeapon(self, weaponBehavior: WeaponBehavior) -> None:
        """
        The character allows replacing a Weapon object in runtime.
        """

        self._weaponBehavior = weaponBehavior


class Paladin(Character):
    pass


if __name__ == '__main__':
    """
    The paladin can change weapons in runtime.
    """

    paladin = Character(SwordBehavior)
    print(paladin.useWeapon)

    paladin.useWeapon = AxeBehavior
    print(paladin.useWeapon)
