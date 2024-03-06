class Book:
    """
    Represents a book with properties and methods.
    """

    def __init__(self, title, author, genre, year_published, price):
        """
        Initializes a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            genre (str): The genre of the book.
            year_published (int): The year the book was published.
            price (float): The price of the book.
        """

        self.title = title
        self.author = author
        self.genre = genre
        self.year_published = year_published

        # Use a property to ensure non-negative price and format to two decimal places
        self._price = price

    @property
    def price(self):
        """
        Getter for the book's price, ensuring non-negative values and formatting.
        """
        return f"${self._price:.2f}"

    @price.setter
    def price(self, new_price):
        """
        Setter for the book's price, validating for non-negativity.
        """
        if new_price < 0:
            raise ValueError("Book price cannot be negative.")
        self._price = new_price

    def __str__(self):
        """
        Returns a string representation of the book object.
        """
        return f"{self.title} by {self.author} ({self.genre}) - ${self.price}"
