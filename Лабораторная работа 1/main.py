import doctest
import re


class Safe:

    def __init__(self, color: str = 'blue', password: str = 'abcd', status: bool = False):
        """
        Создание и подготовка к работе объекта "Сейф"

        :param color: Цвет сейфа
        :param password: Пароль для открытия сейфа
        :param status: Сейф закрыт или открыт

        Примеры:
        >>> safe = Safe('gray', '1034', False)  # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет сейфа должен быть типа str")
        self.color = color

        if not isinstance(password, str):
            raise TypeError("Пароль от сейфа должен быть типа str")
        if len(password) != 4:
            raise ValueError("Пароль должен содержать 4 символа")
        self.password = password

        if not isinstance(status, bool):
            raise TypeError("Сейф либо закрыт(0), либо открыт(1)")
        self.status = status

    def set_color(self, new_color) -> None:
        """
        Функция которая перекрашивает сейф

        :param new_color: Новый цвет

        Примеры:
        >>> safe = Safe('gray', '1042')
        >>> safe.set_color('green')
        """
        if not isinstance(new_color, str):
            raise TypeError("Цвет сейфа должен быть типа str")
        if new_color == self.color:
            raise ValueError("Введите новый цвет")
        self.color = new_color

    def open_safe(self, password: str) -> str:
        """

        :param password: Пароль, который вводим
        :return: Сейф открылся или нет

        Примеры:
        >>> safe = Safe()
        >>> safe.open_safe('abcc')
        """
        if not isinstance(password, str):
            raise TypeError("Вводимый пароль должен быть типа str")
        if self.status:
            raise ValueError("Safe already is opened")
        if password == self.password:
            self.status = True
        else:
            return "Password is wrong! Safe closed"
        return 'Safe opened'

    def close_safe(self) -> str:
        """

        :return: Закрылся ли сейф
        """
        if not self.status:
            raise ValueError("Safe already is closed")
        self.status = False
        return 'Safe closed'


class Phone:

    def __init__(self, name: str, number: str, type_of_phone: str):
        """
        Создание и подготовка объекта "Телефон"

        :param name: Название телефона (как зарегистрирован пользователем)
        :param number: Номер телефона
        :param type_of_phone: Модель телефона

        Примеры:
        >>> my_phone = Phone('android_my', '+79130010022', 'iphone')
        """
        if not isinstance(name, str):
            raise TypeError("Название телефона должно быть типа str")
        self.name = name
        if not isinstance(name, str):
            raise TypeError("Номер телефона должен быть типа str")
        if not re.fullmatch(
                r'\+?\d{0,3}[\s\(\-]?([0-9]{2,3})[\s\)\-]?([\s\-]?)([0-9]{3})[\s\-]?([0-9]{2})[\s\-]?([0-9]{2})',
                number):
            raise ValueError("Неправильно введен номер, введите '+7(___)___-__-__'")
        self.number = number
        if not isinstance(name, str):
            raise TypeError("Модель телефона должна быть типа str")
        self.type_of_phone = type_of_phone

    def get_number(self) -> str:
        """
        Узнать свой номер

        :return: Номер вашего телефона
        """
        return self.number

    def call_to_contact(self, contact) -> None:
        '''
        Позвонить на номер 'contact'

        :param contact: Кому звоним (номер абонента)
        '''
        if not re.fullmatch(
                r'\+?\d{0,3}[\s\(\-]?([0-9]{2,3})[\s\)\-]?([\s\-]?)([0-9]{3})[\s\-]?([0-9]{2})[\s\-]?([0-9]{2})',
                contact):
            ValueError("Number is wrong")
        ...


class Dron:

    def __init__(self, x: float = 0, y: float = 0, height: float = 0):
        """
        Создание подготовка к работе обхъекта "Дрон"

        :param x: Начальная координата дрона по x
        :param y: Начальная координата дрона по y
        :param height: Начальная координата дрона по высоте

        Примеры:
        >>> dron1 = Dron(0.5, 0.6, 4)
        """
        if not isinstance(x, (float, int)):
            raise TypeError("Значение координаты x должно быть типа float или int")
        self.x = x
        if not isinstance(y, (float, int)):
            raise TypeError("Значение координаты y должно быть типа float или int")
        self.y = y
        if not isinstance(height, (float, int)):
            raise TypeError("Значение координаты height должно быть типа float или int")
        if height < 0:
            raise ValueError("Значение height >= 0")
        self.height = height
        self.velocity = 0

    def move(self, x: float = None, y: float = None, height: float = None) -> None:
        """
        Перемещение дрона

        :param x: Перемещение дрона по координате x
        :param y: Перемещение дрона по координате y
        :param height: Перемещение дрона по координате height

        Примеры:
        >>> dron1 = Dron()
        >>> dron1.move(2, 3.5, -2)
        """
        if self.x:
            if not isinstance(x, (float, int)):
                raise TypeError("Значение координаты x должно быть типа float или int")
            self.x += x
        if self.y:
            if not isinstance(y, (float, int)):
                raise TypeError("Значение координаты y должно быть типа float или int")
            self.y += y
        if self.height:
            if not isinstance(height, (float, int)):
                raise TypeError("Значение координаты height должно быть типа float или int")
            if self.height + height < 0:
                raise ValueError("Dron don't move into Earth, please change height value")
            else:
                self.height += height

    def change_velocity(self, velocity: float) -> None:
        """
        Изменение скорости дрона

        :param velocity: Задать значение скорости

        Примеры:
        >>> dron1 = Dron()
        >>> dron1.change_velocity(2)
        """
        if not isinstance(velocity, (float, int)):
            raise TypeError("Значение скорости должно быть типа float или int")
        if self.velocity + velocity < 0:
            raise ValueError("Command is wrong, dron can't interpret velocity < 0")
        self.velocity += velocity

    def stop_dron(self) -> str:
        """
        Остановка дрона

        :return: Остановился ли дрон
        """
        if self.velocity == 0:
            return 'Dron is already stopped'
        self.velocity = 0
        return 'Dron is stopped'

    def get_time_to_coordinate(self, x: float, y: float, height: float) -> float:
        """
        Функция чтобы узнать за какое время дрон долетит до точки

        :param x: Точка до которой нужно добраться по коородинате x
        :param y: Точка до которой нужно добраться по коородинате y
        :param height: Точка до которой нужно добраться по коородинате height
        :return: Возвращает время за которое дрон доберется до заданной точки
        """
        if not isinstance(x, (float, int)):
            raise TypeError("Значение координаты x должно быть типа float или int")

        if not isinstance(y, (float, int)):
            raise TypeError("Значение координаты y должно быть типа float или int")

        if not isinstance(height, (float, int)):
            raise TypeError("Значение координаты height должно быть типа float или int")
        ...
        return ...

if __name__ == "__main__":
    doctest.testmod()
