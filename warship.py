import _random
import random
import time

print('Консольная игра Морской Бой')


# создаем класс отрисовки поля
class DrawField:

    def __init__(self, field=None, field_comp=None, field_comp_hide=None) -> None:
        self.field = field if field else ['0' for _ in range(36)]
        self.field_comp = field_comp if field_comp else ['0' for _ in range(36)]
        self.field_comp_hide = field_comp_hide if field_comp_hide else ['0' for _ in range(36)]

    def draw_player(self):
        print(f"\t\tПоле игрока")
        print(f"  | 1 | 2 | 3 | 4 | 5 | 6 |")
        print(
            f"1 | {self.field[0]} | {self.field[1]} | {self.field[2]} | {self.field[3]} | {self.field[4]} | {self.field[5]} |")
        print(
            f"2 | {self.field[6]} | {self.field[7]} | {self.field[8]} | {self.field[9]} | {self.field[10]} | {self.field[11]} |")
        print(
            f"3 | {self.field[12]} | {self.field[13]} | {self.field[14]} | {self.field[15]} | {self.field[16]} | {self.field[17]} |")
        print(
            f"4 | {self.field[18]} | {self.field[19]} | {self.field[20]} | {self.field[21]} | {self.field[22]} | {self.field[23]} |")
        print(
            f"5 | {self.field[24]} | {self.field[25]} | {self.field[26]} | {self.field[27]} | {self.field[28]} | {self.field[29]} |")
        print(
            f"6 | {self.field[30]} | {self.field[31]} | {self.field[32]} | {self.field[33]} | {self.field[34]} | {self.field[35]} |\n")

    def draw_computer(self):
        print(f"\t\tПоле компьютера")
        print(f"  | 1 | 2 | 3 | 4 | 5 | 6 |")
        print(
            f"1 | {self.field_comp[0]} | {self.field_comp[1]} | {self.field_comp[2]} | {self.field_comp[3]} | {self.field_comp[4]} | {self.field_comp[5]} |")
        print(
            f"2 | {self.field_comp[6]} | {self.field_comp[7]} | {self.field_comp[8]} | {self.field_comp[9]} | {self.field_comp[10]} | {self.field_comp[11]} |")
        print(
            f"3 | {self.field_comp[12]} | {self.field_comp[13]} | {self.field_comp[14]} | {self.field_comp[15]} | {self.field_comp[16]} | {self.field_comp[17]} |")
        print(
            f"4 | {self.field_comp[18]} | {self.field_comp[19]} | {self.field_comp[20]} | {self.field_comp[21]} | {self.field_comp[22]} | {self.field_comp[23]} |")
        print(
            f"5 | {self.field_comp[24]} | {self.field_comp[25]} | {self.field_comp[26]} | {self.field_comp[27]} | {self.field_comp[28]} | {self.field_comp[29]} |")
        print(
            f"6 | {self.field_comp[30]} | {self.field_comp[31]} | {self.field_comp[32]} | {self.field_comp[33]} | {self.field_comp[34]} | {self.field_comp[35]} |")


# создаем класс размещения кораблей

class Ships(DrawField):
    def __init__(self, field=None, field_comp=None, field_comp_hide=None) -> None:
        super().__init__(field, field_comp, field_comp_hide)

    # формула конвертации координат в индексы
    def convert_index(self, x, y):
        return (x - 1) * 6 + (y - 1)

    # метод установки корабля

    def index_set(self, x, y, size):
        index = self.convert_index(x, y)
        # проверка на то что корабль влезает на поле
        if y + size - 1 > 6:
            print('Ваш корабль не влезает на поле.')
            return False
        # проверка на свободное растояние между кораблями

        if index % 6 != 0 and self.field[index - 1] == "\u25A0":
            print('Между кораблями должна быть 1 свободная клетка')
            return False

        if (index + size) % 6 != 0 and self.field[index + size] == "\u25A0":
            print('Между кораблями должна быть 1 свободная клетка')
            return False
        # проверка на то что клетки свободны
        for i in range(size):
            if self.field[index + i] != "0":
                print('Клетки уже заняты. Выберете другое свободное место')
                return False
        # размещение корабля
        for i in range(size):
            self.field[index + i] = "\u25A0"
        return True

    # ввод координат кораблей
    def add_ship(self, size):
        if size == 3:
            count = 1
        elif size == 2:
            count = 2
        elif size == 1:
            count = 4
        counter = 0
        while counter < count:
            ship_place = str(input(f'Введите координаты {size}ех клеточного корабля через пробел: '))
            ship_place = ship_place.split()
            if len(ship_place) != 2:
                print('Необходимо ввести две координаты через пробел.')
                continue
            try:
                x = int(ship_place[0])
                y = int(ship_place[1])

            except ValueError as e:
                print(f'Значение X должно быть цифрой от 1 до 6 {e}')

            else:
                if x < 1 or x > 6:
                    print('Значение X должно быть цифрой от 1 до 6')
                    continue
                elif y < 1 or y > 6:
                    print('Значение Y должно быть цифрой от 1 до 6')
                    continue

                ship1 = Ships(draw1.field)
                if ship1.index_set(x, y, size):
                    counter += 1
                    draw1.draw_player()
                    continue
        return True

    # генератор постановки кораблей компьютера
    def add_ship_comp(self, size):
        while True:
            x = random.randint(1, 6)
            y = random.randint(1, 6)
            index = self.convert_index(x, y)
            if y + size - 1 > 6:
                continue
            ship_placed_flag = True
            for i in range(size):
                if self.field_comp_hide[index + i] != '0':
                    ship_placed_flag = False
                    break

            if index % 6 != 0 and self.field_comp_hide[index - 1] == "1":
                ship_placed_flag = False
            if (index + size) % 6 != 0 and self.field_comp_hide[index + size] == "1":
                ship_placed_flag = False
            if ship_placed_flag:
                for i in range(size):
                    self.field_comp_hide[index + i] = "1"
                break



    def Game_mech(self):

        while True:

            super().draw_computer()
            cord = str(input(f'Введите координаты выстрела через пробел: '))
            cord = cord.split()
            if len(cord) != 2:
                print('Необходимо ввести две координаты через пробел.')
                continue
            try:
                x = int(cord[0])
                y = int(cord[1])

            except ValueError as e:
                print(f'Значение X должно быть цифрой от 1 до 6 {e}')

            else:
                if x < 1 or x > 6:
                    print('Значение X должно быть цифрой от 1 до 6')
                    continue
                elif y < 1 or y > 6:
                    print('Значение Y должно быть цифрой от 1 до 6')
                    continue

            index = self.convert_index(x, y)
            # выстрел игрока

            # проверка попадания в свободную клетку
            if self.field_comp[index] == '0' and self.field_comp_hide[index] == '0':
                self.field_comp[index] = 'T'
                print('Вы промахнулись')
                super().draw_computer()
                self.Comp_move()
                # проверка попадания в корабль
            elif self.field_comp[index] == '0' and self.field_comp_hide[index] == '1':
                self.field_comp[index] = 'X'
                print('Вы попали в корабль')
                super().draw_computer()
                if self.Game_end():
                    break
                else:
                    self.Comp_move()
                # проверка попадания в уже открытую клетку
            elif self.field_comp[index] == 'X' or self.field_comp[index] == 'T':
                print('Вы сюда уже били. Выберете другое поле')

                continue

    # ход компьютера
    def Comp_move(self):
        time.sleep(1)
        while True:
            x = random.randint(1, 6)
            y = random.randint(1, 6)
            index = self.convert_index(x, y)
            # проверка попадания в свободную клетку
            if self.field[index] == '0':
                self.field[index] = 'T'
                print('Компьютер промахнулся\n')
                super().draw_player()
                self.Game_mech()
                # проверка попадания в корабль
            elif self.field[index] == "\u25A0":
                self.field[index] = 'X'
                print('Компьютер попал в корабль\n')
                super().draw_player()

                if self.Game_end():
                    break
                else:
                    self.Game_mech()
                # проверка попадания в уже открытую клетку
            elif self.field[index] == 'X' or self.field[index] == 'T':
                continue

        # проверка на окончание игры

    def Game_end(self):
        if self.field.count("X") == 11:
            print('Компьютер победил')
            return True
        elif self.field_comp.count("X") == 11:
            print('Игрок выиграл. Вы настоящий адмирал!')
            return True



if __name__ == "__main__":
    draw1 = DrawField()
    draw1.draw_player()

    # Ввод кораблей
    ship = Ships(draw1.field)

    ship.add_ship(3)
    ship.add_ship(2)
    ship.add_ship(1)
    print('Благодарим за размещение кораблей')
    time.sleep(1)
    print('Устанавливаем корабли противника...')
    ship.add_ship_comp(3)
    for _ in range(2):
        ship.add_ship_comp(2)

    for _ in range(4):
        ship.add_ship_comp(1)
    time.sleep(1)
    print('Установка кораблей противника завершена')
    print('Готовимся к морскому бою...')
    ship.Game_mech()
