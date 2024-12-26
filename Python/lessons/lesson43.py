class Book:
    def __init__(self, title, author, year):
        self.title, self.author, self.year = title, author, year

    def return_info(self) -> dict:
        return {'title': self.title, 'author': self.author, 'year': self.year}


class Reader:
    my_books: list = []

    def __init__(self, name):
        self.name = name

    def show_info(self) -> str:
        return self.name

    def show_my_books(self) -> list:
        return self.my_books


class Library:
    reader: str = ''
    readers: list = []
    book: dict = {}
    books: list = []
    stories: list = []

    def add_book(self, book):
        self.book = book.return_info()
        self.books.append(self.book)
        self.stories.append(f'Книга {self.book} добавлена в библиотеку.')

    def borrow_book(self, reader):
        reader.my_books.append(self.book)
        self.reader = reader.show_info()
        self.readers.append(self.reader)
        self.stories.append(f'{self.reader} взял книгу {self.book}.')

    def return_book(self, reader):
        reader.my_books.pop()
        self.stories.append(f'{self.reader} вернул книгу {self.book}.')

    def show_readers(self) -> list:
        print('Читатели нашей библиотеки: ', end='')
        return self.readers

    def show_books(self) -> list:
        return self.books

    def show_history(self) -> list:
        return self.stories


c = Book('Cat', 'Mr. Cat', '2024')
d = Reader('Anton')
b = Library()
b.add_book(c)
b.borrow_book(d)
print(*d.show_my_books())
b.return_book(d)
print(*d.show_my_books())
print(*b.show_readers(), sep=', ')
print(*b.show_books(), sep='\n')
print(*b.show_history(), sep='\n')
