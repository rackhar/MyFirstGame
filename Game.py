print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)
mas = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def draw_table ():
   print(mas[0][0],mas[0][1],mas[0][2],"\n",mas[1][0],mas[1][1],mas[1][2],"\n",mas[2][0],mas[2][1],mas[2][2],"\n")


def take_input(player_token):
    draw_table()
    valid = False
    while not valid:
        input_column = input("Укажите столбец для " + player_token + "? ")
        input_line = input("Укажите строку для " + player_token + "? ")
        try:
            input_column = int(input_column)
            input_line = int(input_line)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue

        if all([input_column >= 0,
            input_column <= 2,
            input_line >= 0,
            input_line <= 2]

               ):

            if (str(mas[input_line][input_column]) not in "XO"):
                mas[input_line][input_column] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите верное число")

def check_win(mas):
    if any([all([mas[0][0] == "X", mas[0][1] == "X", mas[0][2] == "X"]),
            all([mas[1][0] == "X", mas[1][1] == "X", mas[1][2] == "X"]),
            all([mas[2][0] == "X", mas[2][1] == "X", mas[2][2] == "X"]),
            all([mas[0][0] == "X", mas[1][0] == "X", mas[2][0] == "X"]),
            all([mas[0][1] == "X", mas[1][1] == "X", mas[2][1] == "X"]),
            all([mas[0][2] == "X", mas[1][2] == "X", mas[2][2] == "X"]),
            all([mas[0][0] == "X", mas[1][1] == "X", mas[2][2] == "X"]),
            all([mas[0][2] == "X", mas[1][1] == "X", mas[2][0] == "X"]),

            ]):
        print("Победил Х! Поздравляем!")
        return "X"
        draw_table()
    elif any([all([mas[0][0] == "0", mas[0][1] == "0", mas[0][2] == "0"]),
              all([mas[1][0] == "0", mas[1][1] == "0", mas[1][2] == "0"]),
              all([mas[2][0] == "0", mas[2][1] == "0", mas[2][2] == "0"]),
              all([mas[0][0] == "0", mas[1][0] == "0", mas[2][0] == "0"]),
              all([mas[0][1] == "0", mas[1][1] == "0", mas[2][1] == "0"]),
              all([mas[0][2] == "0", mas[1][2] == "0", mas[2][2] == "0"]),
              all([mas[0][0] == "0", mas[1][1] == "0", mas[2][2] == "0"]),
              all([mas[0][2] == "0", mas[1][1] == "0", mas[2][0] == "0"]),
              ]):
        print("Победил 0! Поздравляем!")
        return 0
        draw_table()

    return False

def main():
    counter = 0
    win = False
    while not win:
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(mas)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            draw_table()
            break

main()
input("Нажмите Enter для выхода!")