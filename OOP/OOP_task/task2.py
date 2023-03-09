# Создайте класс, который представляет собой пользовательскую учетную запись с атрибутами имени пользователя и пароля.
# Используя property, реализуйте методы для получения и установки хеш-значения пароля.

class Account:
    def __init__(self, name, password):
        self._name = name
        self._password = password

    @property
    def hash_func(self):
        return self._password

    @hash_func.setter
    def hash_func(self, password):
        self._password = password
        return hash(password)


p1 = Account('Ivan', 123456)
print(p1.hash_func)
