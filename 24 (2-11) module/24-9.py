class Cell:
    states = {
        0: ' ',
        1: 'X',
        2: 'O'
    }

    def __init__(self, index: int):
        self.index = index
        self.state = 0

    def __str__(self):
        return f'{self.index}' if self.is_free() else f'{Cell.states[self.state]}'

    def set_state(self, state: states):
        if self.is_free():
            self.state = state

    def is_free(self):
        return self.state == 0


class Player:
    def __init__(self, name: str):
        self.name = name
        self.symbol = 0
        self.goes_now = False

    def set_symbol(self, symbol: str):
        if symbol == 'X':
            self.symbol = 1
        else:
            self.symbol = 2

    def make_move(self, board, other):
        my_cell = int(input(f'{self.name} выбирает ячейку: '))
        if board.cells[my_cell - 1].is_free():
            board.turn(self, my_cell - 1)
            self.goes_now = False
            other.goes_now = True
        else:
            print('Данная ячейка уже занята')

    def set_figures(self, other):
        while True:
            answer = input(f'\nЧем будет ходить {player_1.name}? (X, 0) ')
            if answer.lower() == 'x' or answer.lower() == 'х':
                self.symbol = 1
                other.symbol = 2
                break
            elif answer == '0' or answer.lower() == 'o' or answer.lower() == 'о':
                self.symbol = 2
                other.symbol = 1
                break

    def choose_first(self, other):
        while True:
            answer = input(f'\nКто будет ходить первым:\n1 - {player_1.name} или 2 - {player_2.name}\nВыбор: ')
            if answer == '1':
                self.goes_now = True
                break
            elif answer == '2':
                other.goes_now = True
                break


class Board:
    def __init__(self):
        self.cells = [Cell(index) for index in range(1, 10)]
        self.can_continue = True

    def check_win(self):
        win_indexes = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for indexes in win_indexes:
            if self.cells[indexes[0]].state == self.cells[indexes[1]].state == self.cells[indexes[2]].state \
                    and self.cells[indexes[0]].state + self.cells[indexes[1]].state + self.cells[indexes[2]].state:
                self.can_continue = False
                return True
        return False

    def draw_board(self):
        for i in range(3):
            print(self.cells[0 + i * 3], self.cells[1 + i * 3], self.cells[2 + i * 3])

    def count_free_cell(self):
        count = 0
        for cell in self.cells:
            if cell.state == 0:
                count += 1
        return count

    def turn(self, player: Player, cell: int):
        self.cells[cell].set_state(player.symbol)
        if self.check_win():
            print(f'{player.name} победил, играя "{Cell.states[player.symbol]}"!')
            self.draw_board()
        if self.count_free_cell() == 0:
            self.can_continue = False
            self.draw_board()
            print('\nНичья. Кончились ячейки.')

    def play(self, p1, p2):
        while True:
            self.draw_board()
            if p1.goes_now:
                p1.make_move(board, p2)
            elif p2.goes_now:
                p2.make_move(board, p1)
            if not self.can_continue:
                break


player_1 = Player(input('Введите имя первого игрока: '))
player_2 = Player(input('Введите имя второго игрока: '))
board = Board()

player_1.set_figures(player_2)
player_1.choose_first(player_2)
board.play(player_1, player_2)


