# Напишите класс "Очередь", который содержит список элементов. Используйте магический метод len,
# чтобы определить, сколько элементов находится в очереди..
class Queue:

    def __init__(self, line):
        self._line = line

    def __len__(self):
        return len(self._line)


p1 = Queue([1, 2, 3, 4, 5])
print(len(p1))



