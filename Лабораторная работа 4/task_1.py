if __name__ == "__main__":
    class Book:
        """
        Базовый класс, представляющий книгу.

        Атрибуты:
        - title (str): Название книги.
        - author (str): Автор книги.
        - year (int): Год издания.
        - _genre (str): Жанр книги (инкапсулированный атрибут).
        """

        def __init__(self, title: str, author: str, year: int, genre: str) -> None:
            """
            Конструктор класса Book.

            Аргументы:
            - title (str): Название книги.
            - author (str): Автор книги.
            - year (int): Год издания.
            - genre (str): Жанр книги.
            """
            self.title = title
            self.author = author
            self.year = year
            self._genre = genre  # Инкапсулированный атрибут, так как жанр не должен изменяться извне.

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта.

            Возвращает:
            - str: Строковое представление книги.
            """
            return f'"{self.title}" by {self.author} ({self.year}), жанр: {self._genre}'

        def __repr__(self) -> str:
            """
            Возвращает формальное строковое представление объекта.

            Возвращает:
            - str: Формальное строковое представление книги.
            """
            return f"Book(title={self.title}, author={self.author}, year={self.year}, genre={self._genre})"

        def get_summary(self) -> str:
            """
            Возвращает краткое описание книги.

            Возвращает:
            - str: Краткое описание книги.
            """
            return f"Книга '{self.title}' автора {self.author} в жанре {self._genre}."

        def open_book(self) -> str: # будет перезагружен, чтобы уточнить, как книга открывается
            """
            Метод, который описывает, как открывается книга.

            Возвращает:
            - str: Сообщение о том, что книга открыта.
            """
            return f"Книги '{self.title}' открыта."


    class PaperBook(Book):
        """
        Дочерний класс, представляющий бумажную книгу.

        Атрибуты:
        - pages (int): Количество страниц.
        - cover_type (str): Тип обложки (твердая/мягкая).
        """

        def __init__(self, title: str, author: str, year: int, genre: str, pages: int, cover_type: str) -> None:
            """
            Конструктор класса PaperBook.

            Аргументы:
            - title (str): Название книги.
            - author (str): Автор книги.
            - year (int): Год издания.
            - genre (str): Жанр книги.
            - pages (int): Количество страниц.
            - cover_type (str): Тип обложки.
            """
            super().__init__(title, author, year, genre)
            self.pages = pages
            self.cover_type = cover_type

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта.

            Возвращает:
            - str: Строковое представление бумажной книги.
            """
            return f'"{self.title}" by {self.author} ({self.year}), {self.pages} стр., {self.cover_type} обложка'

        def __repr__(self) -> str:
            """
            Возвращает формальное строковое представление объекта.

            Возвращает:
            - str: Формальное строковое представление бумажной книги.
            """
            return f"PaperBook(title={self.title}, author={self.author}, year={self.year}, pages={self.pages}, cover_type={self.cover_type})"

        def open_book(self, page: int) -> str:
            """
            Метод, который описывает, как открывается страница книги.

            Аргументы:
            - page (int): Номер страницы.

            Возвращает:
            - str: Сообщение о том, что страница открыта.
            """
            return f"Открыта страница {page} книги '{self.title}'."


    class AudioBook(Book):
        """
        Дочерний класс, представляющий аудиокнигу.

        Атрибуты:
        - duration (float): Длительность аудиокниги в часах.
        - narrator (str): Имя диктора.
        """

        def __init__(self, title: str, author: str, year: int, genre: str, duration: float, narrator: str) -> None:
            """
            Конструктор класса AudioBook.

            Аргументы:
            - title (str): Название книги.
            - author (str): Автор книги.
            - year (int): Год издания.
            - genre (str): Жанр книги.
            - duration (float): Длительность аудиокниги в часах.
            - narrator (str): Имя диктора.
            """
            super().__init__(title, author, year, genre)
            self.duration = duration
            self.narrator = narrator

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта.

            Возвращает:
            - str: Строковое представление аудиокниги.
            """
            return f'"{self.title}" by {self.author} ({self.year}), {self.duration} ч., диктор: {self.narrator}'

        def __repr__(self) -> str:
            """
            Возвращает формальное строковое представление объекта.

            Возвращает:
            - str: Формальное строковое представление аудиокниги.
            """
            return f"AudioBook(title={self.title}, author={self.author}, year={self.year}, duration={self.duration}, narrator={self.narrator})"

        def open_book(self) -> str:
            """
            Метод, который описывает, как воспроизводится аудиокнига.

            Возвращает:
            - str: Сообщение о том, что аудиокнига воспроизводится.
            """
            return f"Аудиокнига '{self.title}' воспроизводится."

    # Write your solution here
    pass
