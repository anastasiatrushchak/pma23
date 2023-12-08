class Backpack:

    """A Backpack object class. Has a name, color, list of contents, and a maximum capacity.

    Attributes:
        name (str): the name of the backpack's owner.
        color (str): the color of the backpack.
        max_size (int): the maximum capacity of the backpack.
        contents (list): the contents of the backpack.
    """
    def __init__(self, name, color, max_size=5):
        """Set the name, color, and initialize an empty list of contents.

        Parameters:
            name (str): the name of the backpack's owner.
            color (str): the color of the backpack.
            max_size (int, optional): the maximum capacity of the backpack (default is 5).
        """
        self.name = name
        self.color = color
        self.max_size = max_size
        self.contents = []

    def put(self, item):
        """Add an item to the backpack's list of contents if there is room."""
        if len(self.contents) < self.max_size:
            self.contents.append(item)
        else:
            print("No Room!")

    def take(self, item):
        """Remove an item from the backpack's list of contents."""
        self.contents.remove(item)

    def dump(self):
        """Reset the contents of the backpack to an empty list."""
        self.contents = []
    def __eq__(self, other):
        """Check if two Backpack objects are equal."""
        if isinstance(other, Backpack):
            return (self.name == other.name and
                    self.color == other.color and
                    self.max_size == other.max_size and
                    self.contents == other.contents)
        return False
    def __str__(self):
        """Return a string representation of the Backpack object."""
        return (f"Owner: \t\t\t{self.name}\n"
                f"Color: \t\t\t{self.color}\n"
                f"Size: \t\t\t{len(self.contents)}\n"
                f"Max size: \t\t{self.max_size}\n"
                f"Contents: \t\t{self.contents}")


