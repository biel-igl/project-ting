from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = list()
        self.__length = 0

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        self._data.append(value)
        self.__length += 1

    def dequeue(self):
        if self.__length < 0:
            return None
        self.__length -= 1
        return self._data.pop(0)

    def search(self, index):
        if 0 <= index < len(self._data):
            return self._data[index]
        else:
            raise IndexError("Índice Inválido ou Inexistente")
