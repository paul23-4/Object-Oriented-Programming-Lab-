import pytest
from lib.book import Book  # Assuming your Book class is defined in a module named 'book'


class TestBook:
    def test_initialization(self):
        """
        Tests if the Book class is initialized correctly with the provided arguments.
        """
        title = "The Hitchhiker's Guide to the Galaxy"
        author = "Douglas Adams"
        genre = "Science Fiction"
        year_published = 1979
        price = 12.99

        book = Book(title, author, genre, year_published, price)

        assert book.title == title
        assert book.author == author
        assert book.genre == genre
        assert book.year_published == year_published
        assert book.price == "$12.99"  # Check the formatted price

    def test_book_invalid_price(self):
        """
        Tests if the Book class raises a ValueError for a negative price.
        """
        title = "The Lord of the Rings"
        author = "J.R.R. Tolkien"
        genre = "Fantasy"
        year_published = 1954

        with pytest.raises(ValueError):
            Book(title, author, genre, year_published, -10.0)

    def test_book_string_representation(self):
        """
        Tests if the Book class's __str__ method returns the expected string format.
        """
        title = "Pride and Prejudice"
        author = "Jane Austen"
        genre = "Romance"
        year_published = 1813
        price = 9.95

        book = Book(title, author, genre, year_published, price)

        expected_string = f"{title} by {author} ({genre}) - ${price:.2f}"
        assert str(book) == expected_string
