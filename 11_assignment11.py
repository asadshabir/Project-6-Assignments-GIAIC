# 11. Class Methods
# Assignment_11:
'''Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.'''


class Book:
    total_books = 0  # Class variable
    
    def __init__(self, title):
        self.title = title  # Instance variable
        Book.increment_book_count()  # Increment count when a book is created
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # Increase the count

# Testing
print("Creating books...")
book1 = Book("Python Programming")  # Increments count
book2 = Book("Data Science")        # Increments count
print(f"Total books: {Book.total_books}\n\t Book Titles > {book1.title,book2.title}")  # Book Titles > ('Python Programming', 'Data Science')

book3 = Book("Machine Learning")    # Increments count
book4 = Book("AI Basics")           # Increments count
print(f"Total books: {Book.total_books}\n\t Book Titles > {book1.title,book2.title,book3.title,book4.title}")  # Output: Book Titles > ('Python Programming', 'Data Science', 'Machine Learning', 'AI Basics')``



