from Backpack import Backpack
class Jetpack(Backpack):
    """A Jetpack class that inherits from the Backpack class. Adds fuel-related functionality.

        Attributes:
            name (str): the name of the jetpack's owner.
            color (str): the color of the jetpack.
            max_size (int, optional): the maximum capacity of the jetpack's storage (default is 2).
            amount_of_fuel (int): the amount of fuel in the jetpack (default is 10).
    """
    def __init__(self, name, color, max_size=2, amount_of_fuel=10):
        """Initialize a Jetpack object with a given name, color, max_size, and amount_of_fuel.

               Parameters:
                   name (str): the name of the jetpack's owner.
                   color (str): the color of the jetpack.
                   max_size (int, optional): the maximum capacity of the jetpack's storage (default is 2).
                   amount_of_fuel (int, optional): the initial amount of fuel in the jetpack (default is 10).
        """
        super().__init__(name,color,max_size)
        self.amount_of_fuel = amount_of_fuel
    def fly(self, amount_of_burned_fuel):
        """Simulate flying with the jetpack by burning a specified amount of fuel.

               Parameters:
                   amount_of_burned_fuel (int): the amount of fuel to burn during flight.

               Notes:
                   If there is enough fuel, the specified amount will be burned.
                   If there is not enough fuel, a message 'Not enough fuel!' will be printed.
        """
        if self.amount_of_fuel > amount_of_burned_fuel:
            self.amount_of_fuel -= amount_of_burned_fuel
        else:
            print("Not enough fuel!")
    def dump(self):
        """Reset the contents of the jetpack and set the amount of fuel to 0."""
        super().dump()
        self.amount_of_fuel = 0

    def __eq__(self, other):
        """Check if two Backpack objects are equal."""
        if isinstance(other, Jetpack):
            return (super().__eq__(other) and
                    self.amount_of_fuel == other.amount_of_fuel)
        return False
    def __str__(self):
        """Return a string representation of the Backpack object."""
        return (super().__str__() + '\n' +
                f"Amount of fuel: {self.amount_of_fuel}")




