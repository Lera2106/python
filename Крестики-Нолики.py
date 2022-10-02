field=[[" "," "," "] for i in range(3)]

def field_see():
    print(" 012")
    for i in range(3):
        print(f"{i}{field[i][0]}{field[i][1]}{field[i][2]}")

def enter_():
    while True:
        x,y=(map(int,input("Ваши координаты:").split()))
        if x<0 or x>2 or y<0 or y>2:
            print("Клетка вне диапазона!")
            continue
        if field[x][y]!=" ":
            print("Клетка занята!")
            continue
        return x,y



def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


num=0
while True:
    num+=1
    field_see()
    if num%2==1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x,y=enter_()
    if num % 2 == 1:
        field[x][y]="X"
    else:
        field[x][y]="0"

    if num==9:
        print("Ничья")
        break

    if check_win():
        break
