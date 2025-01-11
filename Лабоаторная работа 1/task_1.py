# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest


class Bottle:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Создание и подготовка к работе объекта Бутылка
        :param capacity_volume: Объем бутылки
        :param occupied_volume: Объем занимаемой жидкости
        Примеры:
        >>> bottle = Bottle(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем должен быть положительным числом")
        self.capacity_volume = capacity_volume  # объем бутылки
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume  # занятый объем бутылки

    def is_full_bottle(self) -> bool:
        """
        Функция которая проверяет является ли бутылка полной

        :return: Является ли бутылка полной

        Примеры:
        >>> bottle = Bottle(500, 0)
        >>> bottle.is_full_bottle()
        """
    def add_water_to_bottle(self, water: float) -> None:
        """
        Добавление воды в бутылку.
        :param water: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в бутылке, то вызываем ошибку

        Примеры:
        >>> bottle = Bottle(500, 0)
        >>> bottle.add_water_to_bottle(200)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна быть положительным числом")


class Cat:
    def __init__(self, name: str):
        """
        Создание и подготовка к работе объекта Собака
        :param name: Имя кошки
        :param tricks: список трюков, которым обучена кошка
        Примеры:
        >>> cat = Cat('Пушок')  # инициализация экземпляра класса
        """
        self.name = name
        self.tricks = []    # создание пустого списка для каждой собаки

    def add_trick(self, trick: str) -> None:
        """
        Добавление трюков для кошки.
        :param trick: название трюка
        Примеры:
        >>> cat = Cat('Пушок')
        >>> cat.add_trick('Голос')
        """

    def check_trick(self, trick: str) -> bool:
        """
        Функция которая проверяет обучена ли кошка трюку

        :return: Знает ли кошка трюк

        Примеры:
        >>> cat = Cat('Пушок')
        >>> cat.check_trick('Перевернись')
        """


class Box:
    def __init__(self, products: str, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Создание и подготовка к работе объекта Ящик
        :param products: вид продукции в ящике
        :param capacity_volume: вместимость ящика
        :param occupied_volume: количество продукции в ящике
        Примеры:
        >>> box = Box('яблоки',500, 0)  # инициализация экземпляра класса
        """
        self.products = products    # вид продукции на складе
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Вместимость должна быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Вместимость должна быть положительным числом")
        self.capacity_volume = capacity_volume  # вместимость ящика
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество продукции на складе должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество продукции на складе не может быть отрицательным числом")
        self.occupied_volume = occupied_volume  # количество продукции в ящике

    def is_empty_box(self) -> bool:
        """
        Функция которая проверяет является ли ящик свободным

        :return: Является ли ящик свободным

        Примеры:
        >>> box = Box('яблоки',500, 0)
        >>> box.is_empty_box()
        """
    def add_products_to_box(self, new_product: str, volume: Union[int, float]) -> None:
        """
        Заполнение ящика.
        :param new_product: тип продукции

        :raise ValueError: Если количество добавляемой продукции превышает свободное место в ящике, то вызываем ошибку
        :raise TypeError: Если новая продукция не совпадает с находящейся в ящике

        Примеры:
        >>> box = Box('яблоки',500, 0)
        >>> box.add_products_to_box('яблоки', 200)
        """
        if not isinstance(volume, (int, float)):
            raise TypeError("Количество добавляемой продукции должно быть типа int или float")
        if volume < 0:
            raise ValueError("Количество добавляемой продукции должно быть положительным числом")


if __name__ == "__main__":
    doctest.testmod()


