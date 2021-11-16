class AudioBook:
    items = []

    def __init__(self, title, author, language, narrator):
        self.title = title
        self.author = author
        self.language = language
        self.narrator = narrator
        self.time = 0
        self.listen_time = 0

    def __repr__(self):
        return f"Title : {self.title}, author: {self.author},language:{self.language},narrator:{self.narrator},time:{self.time}"

    @classmethod
    def add_audio_book(cls):
        title = input('enter book title:')
        author = input('enter books author name:')
        language = input('enter language:')
        narrator = input('enter narrator:')
        id = AudioBook.generate_id(title, author)
        if id in AudioBook.items:
            print('this is available in bookshelf!')
        else:
            AudioBook.items.append(id)
            return cls(title, author, language, narrator)

    @staticmethod
    def generate_id(str1, str2):
        return f"{str1.lower()}_{str2.lower()}"

    def set_time(self, time):
        if time > 0:
            self.time = time

    def listen(self, listen_time):
        if listen_time > 0 and listen_time < self.time:
            self.listen_time = listen_time

    def show_progress(self):
        return f"{self.listen_time} , out of {self.time}"


class Book:
    items = []

    def __init__(self, title, author, language):
        self.title = title
        self.author = author
        self.language = language
        self.pages = 0
        self.read_pages = 0

    def __repr__(self):
        return f"Title : {self.title}, author: {self.author},language:{self.language},page:{self.pages}"

    @classmethod
    def add_book(cls):
        title = input('enter book title:')
        author = input('enter books author name:')
        language = input('enter language:')
        id = Book.generate_id(title, author)
        if id in Book.items:
            print('this is available in bookshelf!')
        else:
            Book.items.append(id)
            return cls(title, author, language)

    @staticmethod
    def generate_id(str1, str2):
        return f"{str1.lower()}_{str2.lower()}"


    def set_page(self,page):
        if page > 0:
            self.pages = page

    def read(self, read_pages):
        if read_pages > 0 and read_pages < self.pages:
            self.read_pages = read_pages

    def show_progress(self):
        return f"{self.read_pages} , out of {self.pages}"


book_shelf = []
audio_book_shelf=[]
while True:
    print("1-add book", '\n', "2-add audiobook", '\n', "3-show books", '\n', "4-show audiobooks", '\n', "5-read a book",
          '\n', "6-listen to an audiobook", '\n', "7-show progress of books", '\n', "8-show progress of audiobook",
          '\n', "9-quit")
    a = int(input('select on of the uper menu:'))
    if a == 1:
        book_1 = Book.add_book()
        if book_1:
            book_shelf.append(book_1)
    elif a == 2:
        book_2 = AudioBook.add_audio_book()
        if book_2:
            audio_book_shelf.append(book_2)
    elif a == 3:
        print(book_shelf)
    elif a == 4:
        print(audio_book_shelf)
    elif a == 5:
        for j in book_shelf:
            p = int(input(f'enter number of {j.title} page= '))
            j.set_page(p)
        print(book_shelf)
        # print(shelf[0].__pages)

    elif a == 6:
        for j in audio_book_shelf:
            p = int(input(f'enter number of {j.title} time= '))
            j.set_time(p)
        print(audio_book_shelf)
    elif a == 7:
        for j in book_shelf:
            p = int(input(f'enter number of {j.title} readen pages= '))
            j.read(p)
            print(j.show_progress())
    elif a == 8:
        for j in audio_book_shelf:
            p = int(input(f'enter number of {j.title} listen time= '))
            j.listen(p)
            print(j.show_progress())
    elif a == 9:
        break
