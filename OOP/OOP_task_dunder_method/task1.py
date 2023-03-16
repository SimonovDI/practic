# Напишите класс "Пользователь", который содержит информацию об имени, электронной почте и пароле.
# Используйте магический метод getattribute, чтобы скрыть значение пароля при его получении.
class User:
    def __init__(self, name, email, password):
        self._name = name
        self._email = email
        self._password = password

    def __getattribute__(self, item):
        if item == '_password':
            raise ValueError("Private attribute")
        return super().__getattribute__(item)


p1 = User('Ivan', 'ivan@google.com', 165842)
print(p1._password)

