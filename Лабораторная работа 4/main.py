if __name__ == "__main__":
    class Car:
        """ Базовый класс автомобили. """

        def __init__(self, brand: str, mileage: float, price: float):
            self.brand = brand
            self.mileage = mileage
            self.price = price

        def __str__(self) -> str:
            """Магический метод, возвращающий строковый объект"""
            return f"Автомобиль {self.brand}. Пробег {self.mileage}. Цена {self.price}"

        def __repr__(self) -> str:
            """Магический метод, возвращающий строковый объект"""
            return f"{self.__class__.__name__}(brand={self.brand!r}, mileage={self.mileage!r}, price={self.price!r})"

        def mileage_in_miles(self) -> float:
            """Перевод пробега из км в мили"""
            return self.mileage * 0.621

        def price_with_discount(self) -> float:
            """Цена со скидкой"""
            ...


    class TruckCar(Car):
        """Дочерний класс Грузовой автомобиль"""

        def __init__(self, brand: str, mileage: float, price: float, capacity: float):
            super().__init__(brand, mileage, price)  # Вызывает метод родительского класса
            self.capacity = capacity

        def __str__(self) -> str:
            """Перегрузка метода, чтобы выводил Грузовой автомобиль и аргумент Допустимая нагрузка"""
            return f"Грузовой автомобиль {self.brand}. Пробег {self.mileage}. Цена {self.price}. Допустимая нагрузка {self.capacity}"

        def __repr__(self) -> str:
            """Перегрузка метода, чтобы выводил аргумент Допустимая нагрузка"""
            return f"{self.__class__.__name__}(brand={self.brand!r}, mileage={self.mileage!r}, price={self.price!r}, capacity={self.capacity!r})"

        def price_with_discount(self) -> float:
            """Цена со скидкой.
            Пусть скидка зависит от грузоподъемности, тогда перегружаем метод, чтобы задать свою реализацию в классе"""
        ...

    pass
