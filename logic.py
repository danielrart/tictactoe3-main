class Field:
    
    
    def __init__(self):
        #Generator of lists
        self.field = [[i + j for j in range(1, 4)]for i in range(0, 9, 3)]
        
                
    def print_field(self):
        for i in range(3):
            for j in range(3):
                print(self.field[i][j], end=' ')
            print()       
            
                    
    def winner(self,player):                  #this method tells who the winner is
        vertical, horinzontal, diagonal = 0, 0, 0
        for i in range(3):
            for j in range(3):
                if self.field[i][j] == player:
                    horizontal += 1
                if self.field[j][i] == player:
                    vertical += 1 
            if horizontal == 3:
                return True


            if vertical == 3:      # Das Feld auf dem das Spiel läuft
                return True

            horizontal, vertical = 0,0
                
            if self.field[i][i] == player:  # Die Bedingungen zum Sieg des Spiels
                diagonal += 1

        if diagonal == 3:
            return True

        if self.field[0][2] == self.field[1][1] == self.field[2][0] == player:
            return True 
            
    def cell_state(self, x, y):

        '''Die Methode Cell state prüft ob die Zelle leer ist um drinne eine Koordinate schreiben zu können wenn sie leer
        ist schick sie cell_fill ein Signal dass die zell leer um drinne eine koordinate schreiben zu können (return true)
        und wenn sie voll ist bekommt cell_fill keine Bestätigung (return False)'''
        if self.field[x][y] == 'X' or self.field[x][y] == '0':
            return False
        else:
            return True

    def cell_fill(self, x, y, player):
        if Field.cell_state(x, y):
            self.field[x][y] = player
            return True
        else:
            return False

    def convert(self, number):
        '''
        convert gets the information from the player and convertes it in to the coordinate of the cell
        '''
        tmp = 1
        for i in range(3):
            for j in range(3):
                if number == tmp:
                    return i, j
                else:
                    tmp = tmp + 1



class Player:

    def __init__(self, symbol):
        # when creating an instance of the Player class, it is specified whether the player will play for crosses or
        # zeros
        self.symbol = symbol

    def move(self):
        # Player chooses cell on the field
        data = input(f'your move, {self.symbol}: ')
        return data

    def data_check(self, data):
        # checks what the player has written
        try:
            number = int(data)
            if 0 < number <= 9:
                return number
            else:
                print(f'{number} is less than 1 or greater than 9')
                return False

        except:
            print(f'{data} is not a number')
            return False

