# Создайте класс, который представляет собой пользовательскую учетную запись с атрибутами имени пользователя и пароля.
# Используя property, реализуйте методы для получения и установки хеш-значения пароля.

class Account:
    def __init__(self, name, password):
        self._name = name
        self._password = hash(password)

    @property
    def hash_password(self):
        if not isinstance(self._name, str):
            raise TypeError("Error name")
        else:
            return self._password

    @hash_password.setter
    def hash_password(self, password):
        self._password = password


p1 = Account('Ivan', '1234')
print(p1.hash_password)


