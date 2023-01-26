class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name  # Делаем атрибут защищенным
        self._author = author  # Делаем атрибут защищенным

    @property
    def name(self):
        """Возвращает название книги"""
        return self._name

    @property
    def author(self):
        """Возвращает автора книги"""
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Бумажная книга"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)  # Вызывает метод родительского класса
        self.pages = pages  # Отработка setter свойства

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге"""
        return self.pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге"""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = new_pages

    def __str__(self):
        super().__str__()  # Вызывает метод родительского класса

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """Аудио книга"""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """Возвращает продолжительность книги"""
        return self.duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """Устанавливает продолжительность книги"""
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность книги должно быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность книги должно быть положительным числом")
        self.duration = new_duration

    def __str__(self):
        super().__str__()  # Вызывает метод родительского класса

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
