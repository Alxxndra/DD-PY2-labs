class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
        Создание и подготовка к работе объекта Книга
        :param name: Название книги
        :param author: Автор книги
        """
        self.__name = name
        self.__author = author

    @property
    def name(self) -> str:
        return self.__name

    @property
    def author(self) -> str:
        return self.__author

    def __str__(self):
        """
        Функция, которая возвращает строку с названием книги
        :return: Книга "название_книги"
        """
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        """
        Функция, которая возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр
        :return: Book(name='test_name_1', author='Пушкин')
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс книги. """
    def __init__(self, name: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта Бумажная книга
        :param name: Название книги
        :param author: Автор книги
        :param pages: Кол-во страниц в бумажной книге
        """
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        """
        Функция, которая возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр
        :return: PaperBook(name='test_name_1', author='Пушкин', pages=200)
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self) -> int:
        return self._pages
    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages


class AudioBook(Book):
    """ Дочерний класс книги. """
    def __init__(self, name: str, author: str, duration: float):
        """
        Создание и подготовка к работе объекта Аудиокнига
        :param name: Название книги
        :param author: Автор книги
        :param duration: Продолжительность аудиокниги
        """
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self):
        """
        Функция, которая возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр
        :return: AudioBook(name='test_name_1', author='Пушкин', duration=200)
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
    @property
    def duration(self) -> float:
        return self._duration
    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, (float, int)):
            raise TypeError("Длительность аудиокниги должна быть int или float")
        if new_duration <= 0:
            raise ValueError("Длительность аудиокниги должна быть положительным числом")
        self._duration = new_duration
