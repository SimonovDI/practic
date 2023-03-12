# Создайте класс, который представляет собой ленту новостей с атрибутами заголовка и текста статьи.
# Используя property, реализуйте метод для получения общего числа символов в заголовке и тексте статьи.
class Lenta:
    def __init__(self, title, txt):
        self._title = title
        self._txt = txt

    @property
    def count_itog(self):
        total = len((self._title + self._txt).replace(' ', ''))
        return total

    @count_itog.setter
    def count_itog(self, title, txt):
        self._title = title
        self._txt = txt


p1 = Lenta('Заголовок', 'Эта книга адресована всем, кто изучает русский язык. Но состоит она не из правил, упражнений и'
                        ' учебных текстов.')
print(p1.count_itog)
