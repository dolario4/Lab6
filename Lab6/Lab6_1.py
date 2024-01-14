class Book:
    def __init__(self, name:str, id:int, pages:int):
        self.name = name
        self.id = id
        self.pages = pages
    def __str__(self)->str:
        return f"Книга: {self.name}"
    def __repr__(self)->str:
        return f"Book(id_ = {self.id} ,name = '{self.name}', pages = {self.pages})"



book1 = Book("Война и мир",1,200)
book2 = Book("test_name_1",1,200)
print(book1)
print(f"{book2!r}")

class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        else:
            return self.books[-1][0] + 1

    def get_index_by_book_id(self, book_id):
        for index, (id, _) in enumerate(self.books):
            if id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


my_library = Library([(32, "Book1"), (33, "Book2"), (34, "Book3")])
print(my_library.get_next_book_id())
print(my_library.get_index_by_book_id(33))
