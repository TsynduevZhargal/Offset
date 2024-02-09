from typing import Union


class IdCounter:   # счётчик покупателей
    id_count = 0

    @classmethod
    def increment_id_count(cls):
        """Метод, который увеличивает количество покупателей."""

        cls.id_count + 1

IdCounter_1 = IdCounter()    # обращение к атрибуту через экземпляр
print(IdCounter_1.id_count)

IdCounter_2 = IdCounter()   # обращение к атрибуту через класс
print(IdCounter.id_count)



class Password:   # проверка пароля
    def __init__(self):
        return self

    def check_password(self):




class Product:   # продукты
    def __init__(self, id, name, price, rating):
        self.id = id   # идентификатор
        self.name = name   # название
        self.price = price   # цена
        self.rating = rating   # рейтинг

    def check(self):     # метод check

    def __repr__(self) -> str:
        return f'Product({self.id}, {self.name}'

    def __str__(self) -> str:
        return str(self)



class Cart:   # корзина
    def __init__(self):


# магазин Автотоваров

class User:   # информация о покупателе
    def __init__(self):



class Store:   # магазин
    def __init__(self):


if __name__ == '__main__'