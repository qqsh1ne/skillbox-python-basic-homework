class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def collect(self):
        if self.state != 0:
            self.state = 0
        self.print_state()

    def is_ripe(self):
        return self.state == 3

    def print_state(self):
        print(f'Картошка {self.index} сейчас в состоянии: {Potato.states[self.state]}')


class PotatoGarden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка растет!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def collect_all(self):
        print('Картошка собрана!')
        for i_potato in self.potatoes:
            i_potato.collect()

    def get_potatoes_state(self):
        for potato in self.potatoes:
            print(potato.state)

    def are_all_ripe(self):
        if all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Вся картошка созрела!\n')
        else:
            print('Картошка ещё не созрела!\n')


class Gardener:
    def __init__(self, name: str, garden: PotatoGarden):
        self.name = name
        self.garden = garden

    def care(self):
        self.garden.grow_all()

    def gather(self):
        self.garden.collect_all()


gardener = Gardener('Садовник', PotatoGarden(5))
gardener.care()
gardener.care()
gardener.care()
gardener.gather()
