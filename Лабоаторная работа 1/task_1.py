# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest

class Pool:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Создание и подготовка к работе объекта Бассейн
        :param capacity_volume: Объем бассейна
        :param occupied_volume: Объем занимаемой жидкости
        Примеры:
        >>> pool = Pool(2000, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем должен быть положительным числом")
        self.capacity_volume = capacity_volume  # объем бассейна
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume  # занятый объем бассейна

    def is_full_pool(self) -> bool:
        """
        Функция которая проверяет является ли бассейн полным

        :return: Является ли бассейн полным

        Примеры:
        >>> pool = Pool(2000, 0)
        >>> pool.is_full_pool()
        """
    def add_aqua_to_pool(self, aqua: float) -> None:
        """
        Добавление воды в бассейн
        :param aqua: Объем добавляемой воды

        :raise ValueError: Если количество добавляемой воды превышает свободное место в бассейне, то вызываем ошибку

        Примеры:
        >>> pool = Pool(2000, 0)
        >>> pool.add_aqua_to_pool(500)
        """
        if not isinstance(aqua, (int, float)):
            raise TypeError("Добавляемый объем воды должен быть типа int или float")
        if aqua < 0:
            raise ValueError("Добавляемый ообъем воды должен быть положительным числом")


class Pencil:
    def __init__(self, color: str):
        """
        Создание и подготовка к работе объекта Карандаш
        :param color: Цвет карандаша
        :param hardness: варианты твердости карандаша
        Примеры:
        >>> pencil = Pencil('Серый')  # инициализация экземпляра класса
        """
        self.color = color
        self.hardness = []    # создание пустого списка для карандаша

    def add_hardness(self, hardness: str) -> None:
        """
        Добавление твердости карандаша
        :param hardness: твердость карандаша
        Примеры:
        >>> pencil = Pencil('Серый')
        >>> pencil.add_hardness('НВ')
        """

    def check_hardness(self, hardness: str) -> bool:
        """
        Функция, которая проверяет, есть ли карандаш нужной твердости

        :return: Есть ли карандаш нужной твердости

        Примеры:
        >>> pencil = Pencil('Серый')
        >>> pencil.check_hardness('3В')
        """


class Storage:
    def __init__(self, products: str, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Создание и подготовка к работе объекта Склад
        :param products: вид продукции на складе
        :param capacity_volume: вместимость склада
        :param occupied_volume: количество продукции на складе
        Примеры:
        >>> storage = Storage('кирпичи',10000, 0)  # инициализация экземпляра класса
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
        self.occupied_volume = occupied_volume  # количество продукции на складе

    def is_empty_storage(self) -> bool:
        """
        Функция которая проверяет является ли склад пустым

        :return: Является ли склад пустым

        Примеры:
        >>> storage = Storage('кирпичи',10000, 0)
        >>> storage.is_empty_storage()
        """
    def add_products_to_storage(self, new_product: str, volume: Union[int, float]) -> None:
        """
        Заполнение склада.
        :param new_product: тип продукции

        :raise ValueError: Если количество добавляемой продукции превышает свободное место на складе, то вызываем ошибку

        Примеры:
        >>> storage = Storage('кирпичи',10000, 0)
        >>> storage.add_products_to_storage('кирпичи', 2000)
        """
        if not isinstance(volume, (int, float)):
            raise TypeError("Количество добавляемой продукции должно быть типа int или float")
        if volume < 0:
            raise ValueError("Количество добавляемой продукции должно быть положительным числом")


if __name__ == "__main__":
    doctest.testmod()


