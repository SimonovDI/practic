# Реализуйте класс - Singleton, у которого может быть только один экземпляр..

class Singleton:
    def __new__(cls, *args, **kwargs):
        if hasattr(cls, 'copy'):
            raise NameError('This class is created')
        cls.copy = super(Singleton, cls).__new__(cls)
        return cls


s = Singleton()
print("Object created", s)
