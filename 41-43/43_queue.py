# Реализовать класс Queue с методами enqueue (добавить элемент в очередь, принимает элемент для добавления в очередь),
# dequeue (удалить элемент из очереди), empty (проверить, пуста ли очередь, возвращает True или False),
# front (получить первый элемент), back (получить последний элемент).


class QueueItem:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        if self.head is None:
            self.head = QueueItem(value)
            self.tail = self.head
        else:
            item = QueueItem(value)
            self.tail.next = item
            self.tail = item

    def dequeue(self):
        if self.head is None:
            raise Exception
        result = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return result

    def empty(self):
        return self.head is None

    def front(self):
        if self.head is None:
            raise Exception
        return self.head.value

    def back(self):
        if self.head is None:
            raise Exception
        return self.tail.value
