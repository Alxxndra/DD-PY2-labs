if __name__ == "__main__":
    class Car:
        """
        Базовый класс Car, представляющий общий интерфейс для всех автомобилей.
        """

        def __init__(self, make: str, model: str, year: int) -> None:
            """
            Конструктор для инициализации автомобиля.

            :param make: Производитель автомобиля.
            :param model: Модель автомобиля.
            :param year: Год выпуска автомобиля.
            Приватные атрибуты, так как не должны меняться извне
            """
            self._make = make  # Производитель (приватный атрибут)
            self._model = model  # Модель (приватный атрибут)
            self._year = year  # Год выпуска (приватный атрибут)

        def __str__(self) -> str:
            """
            Возвращает строковое представление автомобиля.
            """
            return f"Автомобиль {self._make} {self._model}"

        def __repr__(self) -> str:
            """
            Возвращает формальное представление автомобиля.
            """
            return f"{self.__class__.__name__}(make='{self._make!r}', model='{self._model!r}', year={self._year!r})"

        def start_engine(self) -> str:
            """
            Запускает двигатель автомобиля.

            :return: Строка с сообщением о запуске двигателя.
            """
            return f"The engine of {self} is starting."

        def honk_horn(self) -> str:
            """
            Издает сигнал автомобилем.

            :return: Строка с сообщением о звуке сигнала.
            """
            return f"{self._make} {self._model} goes 'Beep beep!'"


    class Sedan(Car):
        """
        Класс Sedan, представляющий легковой автомобиль.
        """

        def __init__(self, make: str, model: str, year: int, passenger_capacity: int) -> None:
            """
            Конструктор для инициализации легкового автомобиля.

            :param make: Производитель легкового автомобиля.
            :param model: Модель легкового автомобиля.
            :param year: Год выпуска легкового автомобиля.
            :param passenger_capacity: Вместимость пассажиров.
            """
            super().__init__(make, model, year)  # Вызов конструктора базового класса
            self.__passenger_capacity = passenger_capacity  # Вместимость пассажиров (приватный атрибут)

        def __repr__(self) -> str:
            """
            Возвращает формальное представление автомобиля.
            """
            return (f"{self.__class__.__name__}(make='{self._make!r}', model='{self._model!r}', year={self._year!r}, "
                    f"passenger_capacity={self.__passenger_capacity!r})")

        def start_engine(self) -> str:
            """
            Запускает двигатель легкового автомобиля.

            Переопределенный метод, чтобы добавить информацию о бесшумности двигателя легкового автомобиля.
            """
            return f"The engine of {self} is starting silently!"


    class Truck(Car):
        """
        Класс Truck, представляющий грузовой автомобиль.
        """

        def __init__(self, make: str, model: str, year: int, load_capacity: float) -> None:
            """
            Конструктор для инициализации грузового автомобиля.

            :param make: Производитель грузового автомобиля.
            :param model: Модель грузового автомобиля.
            :param year: Год выпуска грузового автомобиля.
            :param load_capacity: Грузоподъемность автомобиля.
            """
            super().__init__(make, model, year)  # Вызов конструктора базового класса
            self.__load_capacity = load_capacity  # Грузоподъемность (приватный атрибут)

        def __repr__(self) -> str:
            """
            Возвращает формальное представление автомобиля.
            """
            return (f"{self.__class__.__name__}(make='{self._make!r}', model='{self._model!r}', year={self._year!r}, "
                    f"load_capacity={self.__load_capacity!r})")

        def start_engine(self) -> str:
            """
            Запускает двигатель грузового автомобиля.

            Переопределенный метод, чтобы добавить информацию о мощности двигателя грузовика.
            """
            return f"The powerful engine of {self} is starting with a roar!"


    class Animal:
        """
        Базовый класс, представляющий животное.

        Атрибуты:
        - name (str): Имя животного.
        - age (int): Возраст животного.
        - _species (str): Вид животного (инкапсулированный атрибут).
        """

        def __init__(self, name: str, age: int, species: str) -> None:
            """
            Конструктор класса Animal.

            Аргументы:
            - name (str): Имя животного.
            - age (int): Возраст животного.
            - species (str): Вид животного.
            """
            self.name = name
            self.age = age
            self._species = species  # Инкапсулированный атрибут, так как вид животного не должен изменяться извне.

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта.

            Возвращает:
            - str: Строковое представление объекта.
            """
            return f"{self.name} ({self._species}), возраст: {self.age} лет"

        def __repr__(self) -> str:
            """
            Возвращает формальное строковое представление объекта.

            Возвращает:
            - str: Формальное строковое представление объекта.
            """
            return f"{self.__class__.__name__}(name={self.name}, age={self.age}, species={self._species})"

        def make_sound(self) -> str:
            """
            Возвращает звук, который издает животное.

            Возвращает:
            - str: Звук животного.
            """
            return "Неизвестный звук"

        def action(self) -> str:
            """
            Метод, который описывает, что животное выполняет действие.
            Метод наследуется, т.к. факт действия не зависит от вида животного
            Возвращает:
            - str: Сообщение о том, что животное выполняет действие.
            """
            return f"{self.name} выполняет действие"


    class Dog(Animal):
        """
        Дочерний класс, представляющий собаку.

        Атрибуты:
        - breed (str): Порода собаки.
        """

        def __init__(self, name: str, age: int, breed: str) -> None:
            """
            Конструктор класса Dog.

            Аргументы:
            - name (str): Имя собаки.
            - age (int): Возраст собаки.
            - breed (str): Порода собаки.
            """
            super().__init__(name, age, species="Собака")
            self.breed = breed

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта.

            Возвращает:
            - str: Строковое представление объекта.
            """
            return f"{self.name} ({self.breed}), возраст: {self.age} лет"

        def __repr__(self) -> str:
            """
            Возвращает формальное строковое представление объекта.

            Возвращает:
            - str: Формальное строковое представление объекта.
            """
            return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"

        def make_sound(self) -> str:
            """
            Возвращает звук, который издает собака.

            Возвращает:
            - str: Звук собаки.
            """
            return "Гав-гав!"

        def fetch(self, item: str) -> str:
            """
            Метод, который описывает, как собака приносит предмет.

            Аргументы:
            - item (str): Предмет, который нужно принести.

            Возвращает:
            - str: Сообщение о том, что собака принесла предмет.
            """
            return f"{self.name} принес(ла) {item}"

    class Cat(Animal):
        """
        Дочерний класс, представляющий кошку.

        Атрибуты:
        - color (str): Цвет кошки.
        """

        def __init__(self, name: str, age: int, color: str) -> None:
            """
            Конструктор класса Cat.

            Аргументы:
            - name (str): Имя кошки.
            - age (int): Возраст кошки.
            - color (str): Цвет кошки.
            """
            super().__init__(name, age, species="Кошка")
            self.color = color

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта.

            Возвращает:
            - str: Строковое представление объекта.
            """
            return f"{self.name} ({self.color}), возраст: {self.age} лет"

        def __repr__(self) -> str:
            """
            Возвращает формальное строковое представление объекта.

            Возвращает:
            - str: Формальное строковое представление объекта.
            """
            return f"Cat(name={self.name}, age={self.age}, color={self.color})"

        def make_sound(self) -> str:
            """
            Возвращает звук, который издает кошка.

            Возвращает:
            - str: Звук кошки.
            """
            return "Мяу!"

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
