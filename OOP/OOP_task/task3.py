# Создайте класс, который представляет собой список покупок с атрибутами списка продуктов.
# Используя property, реализуйте метод для получения количества товаров в списке.

class Shopping_list:
    def __init__(self, spisok):
        self._spisok = spisok

    @property
    def lst(self):
        return len(self._spisok)


p1 = Shopping_list(['яблоко', 'груша', 'банан'])
print(p1.lst)
