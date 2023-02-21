



sticks = 20

class Player:

    def __init__(self, name):
        self.name = name
        self.flag = False
    def input_sticks(self):
        print('Сколько палочек вытащить')
        try:
            sticks_player = int(input())
        except ValueError:
            print('NONONONONONONONOONONONONO')
            sticks_player = self.input_sticks()
        return sticks_player

    def move(self):
            print(f'Игрок {self.name} ходит')
            sticks_player = self.input_sticks()
            while(sticks_player > 3 or sticks_player < 1):
                print('Введено неправильное число, можно взять от одной до трех палочек')
                sticks_player = self.input_sticks()
            global sticks
            sticks -= sticks_player
            if sticks < 0: sticks = 0
            if sticks > 0: self.flag = True
            if sticks == 0: print(f'Win is {self.name}')
            return 0




if __name__ == '__main__':
    player1 = Player('Bob')
    player2 = Player('Balera')
    print('Игра началась')
    while sticks:
        print(f'палочек {sticks}')
        player1.move()
        print(f'палочек {sticks}')
        if(sticks == 0):break
        player2.move()


