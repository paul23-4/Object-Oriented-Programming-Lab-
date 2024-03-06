class Shoe:
    """
    Represents a shoe with properties and methods.
    """

    def __init__(self, brand, size, style, color, price):
        """
        Initializes a Shoe object.

        Args:
            brand (str): The brand of the shoe.
            size (float): The size of the shoe.
            style (str): The style of the shoe (e.g., sneaker, sandal).
            color (str): The color of the shoe.
            price (float): The price of the shoe.
        """

        self.brand = brand
        self.size = size
        self.style = style
        self.color = color
        self.price = price  # No need for extra validation or formatting here

    def __str__(self):
        """
        Returns a string representation of the shoe object.
        """
        return f"{self.brand} {self.style} (size {self.size}, {self.color}) - ${self.price:.2f}"
