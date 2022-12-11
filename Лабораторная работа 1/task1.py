import doctest


class Ribbon:
    def __init__(self, width: float, length: float):
        """
        Создание и подготовка к работе объекта "Стакан"
        :param width: Ширина ленты
        :param length: Длина ленты

        Примеры:
        >>> ribbon = Ribbon(10, 5)
        """
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина ленты должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина ленты должна быть положительным числом")
        self.width = width

        if not isinstance(length, (int, float)):
            raise TypeError("Длина ленты должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина ленты должна быть положительным числом")
        self.length = length


    def cut_length(self, cut_length: float) -> None:
        """
        Уменьшение длины ленты.
        :param cut_length: Длина отрезаемой части ленты

        :raise ValueError: Если длина отрезаемой части превышает длину ленты, то вызываем ошибку

        Примеры:
        >>> ribbon = Ribbon(10, 5)
        >>> ribbon.cut_length(2)
        """
        if not isinstance(cut_length, (int, float)):
            raise TypeError("Длина отрезаемой части должна быть типа int или float")
        if cut_length < 0:
            raise ValueError("Длина отрезаемой части должна быть не отрицательным числом")
        ...


    def cut_width(self, cut_width: float) -> None:
        """
        Уменьшение ширина ленты.
        :param cut_width: Ширина отрезаемой части ленты

        :raise ValueError: Если ширина отрезаемой части превышает ширину ленты, то вызываем ошибку

        Примеры:
        >>> ribbon = Ribbon(10,5)
        >>> ribbon.cut_width(2)
        """
        if not isinstance(cut_width, (int, float)):
            raise TypeError("Ширина отрезаемой части должна быть типа int или float")
        if cut_width < 0:
            raise ValueError("Ширина отрезаемой части должна быть не отрицательным числом")
        ...


class Engineer:
    def __init__(self, name: str, age: int, salary: int):
        """
        Создание и подготовка к работе объекта "Инженер"
        :param name: Имя
        :param age: Возраст
        :param salary: Зарплата

        Примеры:
        >>> engineer = Engineer('Антон', 30, 50000)
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.age = age

        if not isinstance(salary, int):
            raise TypeError("Зарплата должна быть целым цислом")
        if salary <= 0:
            raise ValueError("Зарплата должна быть положительным числом")
        self.salary = salary


    def engineer_young_employee(self) -> bool:
        """
        Функция, которая проверяет является ли инженер молодым сотрудником

        :return: Является ли инженер молодым сотрудником

        Примеры:
        >>> engineer = Engineer('Антон', 30, 50000)
        >>> engineer.engineer_young_employee()
        """
        ...


    def add_salary(self, add_sum: int) -> None:
        """
        Увеличение зарплаты инженера.
        :param add_sum: Сумма, на которую увеличивается зарплата

        Примеры:
        >>> engineer = Engineer('Антон', 30, 50000)
        >>> engineer.add_salary(3000)
        """
        if not isinstance(add_sum, int):
            raise TypeError("Сумма увеличения зарплаты должна быть типа int")
        ...


class User:
    def __init__(self, country: str, password: str):
        """
        Создание и подготовка к работе объекта "Пользователь"
        :param country: Страна
        :param password: Пароль

        Примеры:
        >>> user = User('Россия', '85a9a5a93')
        """
        if not isinstance(country, str):
            raise TypeError("Страна должна быть типом данных str")
        self.country = country
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть типом данных str")
        self.password = password


    def change_password(self, new_password:str) -> None:
        """
        Смена пароля.
        :param new_password: Новый пароль

        Примеры:
        >>> user = User('Россия', '85a9a5a93')
        >>> user.change_password('55555aallll9')

        :raise ValueError: Если длина пароля меньше min_size символов, то вызываем ошибку
        """
        if not isinstance(new_password, str):
            raise TypeError("Новый пароль должен быть типа str")
        min_size = 8  # Устанавливаем минимальную длину пароля
        if len(new_password) <= min_size:
            raise ValueError("Длинна пароля должна быть не меньше min_size символов")
        ...


    def change_country(self, new_country:str) -> None:
        """
        Смена страны.
        :param new_country: Новая страна

        Примеры:
        >>> user = User('Россия', '85a9a5a93')
        >>> user.change_country('Китай')
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
