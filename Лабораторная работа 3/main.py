class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        self._name = name
        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть типа str")
        self._author = author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = pages

    def __str__(self) -> str:
        """
        Здесь можно было бы перегрузить метод, если мы хотим выводить количесво страниц
        """
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self._pages})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("Продолжительность аудиокниги должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть больше 0")
        self._duration = duration

    def __str__(self):
        """
        Здесь можно было бы перегрузить метод, если мы хотим выводить продолжительность
        """
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self._duration})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность аудиокниги должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть больше 0")
        self._duration = new_duration
