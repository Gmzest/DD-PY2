class Nucleus:
    """
    Базовый класс нуклида
    """

    def __init__(self, protons: int, neutrons: int, excitation_energy: (float, int)):
        """
        Подготовка и создание объекта 'Nucleus'

        :param protons: Число протонов в ядре
        :param neutrons: Число нейтронов в ядре
        :param excitation_energy: Энергия возбуждения ядра
        :param mass_of_proton: Масса протона
        :param mass_of_neutron: Масса нейтрона

        Примеры:
        >>> bor = Nucleus(9, 11, 0.0)
        """

        if not isinstance(protons, int):
            raise TypeError("Число протонов должно быть типа int")
        if protons <= 0:
            raise ValueError("Число протонов должно быть положительным")
        self.count_of_protons = protons
        if not isinstance(neutrons, int):
            raise TypeError("Число нейтронов должно быть типа int")
        if neutrons < 0:
            raise ValueError("Число нейтронов должно быть неотрицательным")
        self.count_of_neutrons = neutrons
        if not isinstance(excitation_energy, (float, int)):
            raise TypeError("Энергия возбуждения должна быть типа floar или int")
        if excitation_energy < 0:
            raise ValueError("Энергия возбуждения должна быть неотрицательной")
        self.excitation_energy = excitation_energy
        self.mass_of_neutron = 0.2
        self.mass_of_proton = 0.1

    def bound_energy(self, mass_of_nucleus: float) -> float:
        """
        Расчет энергии связи в ядре

        :param: mass_of_nucleus: Масса ядра [кг]
        :return: Энергия связи [МэВ]

        Примеры:
        >>> bor = Nucleus(9, 11, 1)
        >>> type(bor.bound_energy(11)) == float
        True
        """
        return (self.count_of_protons * self.mass_of_proton +
                self.count_of_neutrons * self.mass_of_neutron - mass_of_nucleus) * 931.5

    def disexcitation(self) -> str:
        """
        Метод показывает каким механизмом ядро снимет энергию возбуждения

        :return: 'Название механизма'

        Примеры:
        >>> bor = Nucleus(9, 11, 0.7)
        >>> type(bor.disexcitation()) == str
        True
        """
        return 'Название механизма'

    def __str__(self):
        """
        :return: Магический метод возвращает строковое представление класса
        """
        return f'Нуклид с зарядом {self.count_of_protons} и массовым числом {self.count_of_neutrons + self.count_of_protons}'

    def __repr__(self):
        """
        :return: Магический метод возвращает строку, которая показывает как инициализировать экземпляр класса
        """
        return f'{self.__class__.__name__}(protons={self.count_of_protons}, neutrons={self.count_of_neutrons}, excitation_energy={self.excitation_energy})'


class DropModel(Nucleus):
    """
    Класс для создания нуклида в капельной модели
    Наследник класса Nucleus
    """

    def __init__(self, protons: int, neutrons: int, excitation_energy: float, alpha: float, beta: float, gamma: float,
                 sigma: float, zetta: float):
        """
        Конструктор дочернего класса DropModel
        Подготовка и создание объекта нуклида в капельной модели

        :param protons: Число протонов
        :param neutrons: Число нейтронов
        :param excitation_energy: Энерги возбуждения ядра
        :param alpha: Коэффициент альфа
        :param beta: Коэффициент бетта
        :param gamma: Коэффициент гамма
        :param sigma: Коэффициент сигма
        :param zetta: Коэффициент зетта
        Все коэффициенты табличные (эмперические)
        """
        super().__init__(protons, neutrons, excitation_energy)
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.sigma = sigma
        self.zetta = zetta

    def bound_energy(self, **kwargs) -> float:
        """
        Расчет энергии связи в ядре.
        Перегрузили метод, так как в данной модели можно произвести расчет по полуэмпирической формуле.
        :return: Энергия связи [МэВ]

        """
        A = self.count_of_neutrons + self.count_of_protons
        return self.alpha * A - self.beta * A ** (2 / 3) - self.gamma * \
               self.count_of_protons * (self.count_of_protons - 1) / A ** (1 / 3) \
               - self.sigma * (A - 2 * self.count_of_protons) ** 2 / A - self.zetta * A ** (-3 / 4)

    def __repr__(self):
        """

        :return: Магический метод был перегружен, так как дополнились атрибуты для инициализации
        """
        return f'{self.__class__.__name__}(protons={self.count_of_protons}, neutrons={self.count_of_neutrons},' \
               f' excitation_energy={self.excitation_energy}, alpha={self.alpha}, beta={self.beta},' \
               f' gamma={self.gamma}, sigma={self.sigma}, zetta={self.zetta})'


class LayersModel(Nucleus):
    """
    Класс для создания нуклида в оболочечной модели
    Наследник класса Nucleus
    """

    def __init__(self, protons: int, neutrons: int, excitation_energy: float):
        """
        Конструктор дочернего класса LayersModel
        Подготовка и создание объекта нуклида в оболочечной модели

        :param protons: Число протонов
        :param neutrons: Число нейтронов
        :param excitation_energy: Энергия возбуждения ядра
        """
        super().__init__(protons, neutrons, excitation_energy)

    def disexcitation(self) -> str:
        """
        Метод показывает каким механизмом ядро снимет энергию возбуждения
        Перегрузили метод, так как в этой модели можно утвердить, что ядро будет устойчиво ("магическое ядро")
        :return: "Название механизма" / "Магическое ядро"
        """
        return 'Название механизма'


if __name__ == "__main__":
    import doctest

    doctest.testmod()
