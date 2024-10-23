

class Node:
    """ Узел
        value - значение хранящееся в узле
        next_node - ссылка на следующий узел
    """
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class CyclicList:
    """ Круговой список
        head_node - начало кругового списка
        end_node - конец
    """
    def __init__(self):
        self.head_node = None
        self.end_node = None

    def append(self, value):
        """ Добавляет узел в конец списка и переносит ссылка на head на новый конечный узел"""
        if not self.head_node:
            self.head_node = Node(value)
            self.head_node.next_node = self.head_node
            self.end_node = self.head_node
        else:
            new_node = Node(value, self.head_node)
            self.end_node.next_node = new_node
            self.end_node = new_node

    def append_list(self, value_list):
        """ Добавляет коллекцию в конец списка"""
        if hasattr(value_list, '__iter__'):
            for el in value_list:
                self.append(el)
        else:
            self.append(value_list)

    def display(self):
        """ Распечатывает всю коллекцию начиная с head"""
        if not self.head_node:
            print('Список пуст')
            return
        print('head = ', end='')
        current_node = self.head_node
        while True:
            print(current_node.value, end='-> ')
            current_node = current_node.next_node
            if current_node == self.head_node:
                break
        print('(head)')

    def get_node(self, index):
        """ Возвращает узел по индексу"""
        index = index % len(self)
        current_node = self.head_node
        current_index = 0
        while True:
            if current_index == index:
                return current_node

            current_node = current_node.next_node
            current_index += 1

    def __len__(self):
        if not self.head_node:
            return 0
        length = 0
        current_node = self.head_node
        while True:
            length += 1
            current_node = current_node.next_node
            if current_node == self.head_node:
                return length

    def __getitem__(self, index):
        if isinstance(index, slice):
            start = index.start if index.start is not None else 0
            stop = index.stop if index.stop is not None else len(self)

            step = index.step if index.step is not None else 1

            if index.step:
                raise IndexError('шаг в срезе не поддерживается!!!')

            if start > stop:
                raise IndexError('стоп не может быть меньше старта')

            result_list = []
            multiplier = start // len(self)
            start = start % len(self)
            stop = stop - multiplier * len(self) - start
            current_node = self.get_node(start)
            while stop:
                result_list.append(current_node.value)
                current_node = current_node.next_node
                stop -= 1

            return result_list

        # Отрицательная индексация не поддерживается
        if index < 0:
            raise KeyError('Индекс должен быть положительным')

        return self.get_node(index).value

        # current_node = self.head_node
        # current_index = 0
        # while True:
        #     if current_index == index:
        #         return current_node.value
        #
        #     current_node = current_node.next_node
        #     current_index += 1


if __name__ == '__main__':
    ciclic_list = CyclicList()
    ciclic_list.append(26)
    ciclic_list.append(3)
    ciclic_list.append(4)
    ciclic_list.append(5)
    ciclic_list.display()

    ciclic_list.append_list(290)
    ciclic_list.append_list([12, 4])
    ciclic_list.display()

    print(len(ciclic_list))
    print('---Index---')
    print('0', ciclic_list[0])
    print('1', ciclic_list[1])
    print('2', ciclic_list[2])
    print('3', ciclic_list[3])
    print('4', ciclic_list[4])
    print('5', ciclic_list[5])

    print('---Slice---')
    print(ciclic_list[:9])
    print(ciclic_list[40:42])
    print(ciclic_list[1_000_000:1_000_005])

