

class Struct:

    k = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def createGrid(self, c, s):
        self.k[c-1] = s
        print('   ' + self.k[0] + ' |' + ' ' + self.k[1] + ' |' + ' ' + self.k[2] + ' ')
        print('  ---|---|---')
        print('   ' + self.k[3] + ' |' + ' ' + self.k[4] + ' |' + ' ' + self.k[5] + ' ')
        print('  ---|---|---')
        print('   ' + self.k[6] + ' |' + ' ' + self.k[7] + ' |' + ' ' + self.k[8] + ' ')

    def ckVal(self, c, ch):
        if c == None:
            return False
        if c=='1' or c=='2' or c=='3' or c=='4' or c=='5' or c=='6' or c=='7' or c=='8' or c=='9':
            pass
        else:
            return False
        for i in ch:
            if i == int(c):
                return False

        return True

    def ckResult(self,ch,p1,p2):
        if self.k[0] == 'X' and self.k[1] == 'X' and self.k[2] == 'X':
            print(p1.upper() + " WINS")
            return False
        elif self.k[3] == 'X' and self.k[4] == 'X' and self.k[5] == 'X':
            print(p1.upper() + " WINS")
            return False
        elif self.k[6] == 'X' and self.k[7] == 'X' and self.k[8] == 'X':
            print(p1.upper() + " WINS")
            return False
        elif self.k[0] == 'X' and self.k[3] == 'X' and self.k[6] == 'X':
            print(p1.upper() + " WINS")
            return False
        elif self.k[1] == 'X' and self.k[4] == 'X' and self.k[7] == 'X':
            print(p1.upper() + " WINS")
            return False
        elif self.k[2] == 'X' and self.k[5] == 'X' and self.k[8] == 'X':
            print(p1.upper() + " WINS")
            return False
        elif self.k[0] == 'X' and self.k[4] == 'X' and self.k[8] == 'X':
            print(p1.upper() + " WINS")
            return False
        elif self.k[0] == 'O' and self.k[1] == 'O' and self.k[2] == 'O':
            print(p2.upper() + " WINS")
            return False
        elif self.k[3] == 'O' and self.k[4] == 'O' and self.k[5] == 'O':
            print(p2.upper() + " WINS")
            return False
        elif self.k[6] == 'O' and self.k[7] == 'O' and self.k[8] == 'O':
            print(p2.upper() + " WINS")
            return False
        elif self.k[0] == 'O' and self.k[3] == 'O' and self.k[6] == 'O':
            print(p2.upper() + " WINS")
            return False
        elif self.k[1] == 'O' and self.k[4] == 'O' and self.k[7] == 'O':
            print(p2.upper() + " WINS")
            return False
        elif self.k[2] == 'O' and self.k[5] == 'O' and self.k[8] == 'O':
            print(p2.upper() + " WINS")
            return False
        elif self.k[0] == 'O' and self.k[4] == 'O' and self.k[8] == 'O':
            print(p2.upper() + " WINS")
            return False
        elif len(ch) == 9:
            print(" GAME DRAW")
            return False
        else:
            return True


print("  TIC TAC TOE")
print()
print("  Press Q to quit")
print()
print("Rules:-")
print(" - Both player has to choose the position between 1 - 9 one by one")
print(" - If any position is selected, it cannot be selected again")
print(" - The first player to get 3 of his/her marks in a row (up, down, across, or diagonally) is the winner.")
print(" - When all 9 blocks are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")
print()

a = True
p1 = input("Enter name of Player 1\n")
if p1 == "Q":
    a = False

p2 = input("Enter name of Player 2\n")
if p2 == "Q":
    a = False
ch = []
b = 1

while a:
    d = b % 2
    if b % 2 == 1:
        c = input(p1.upper() + " CHANCE\n")
        s = 'X'
    else:
        c = input(p2.upper() + " CHANCE\n")
        s = 'O'

    if c == "Q":
        a = False
        break

    obj = Struct()
    ck = obj.ckVal(c, ch)

    if ck == False:
        print("  INVALID CHOICE\n  PLEASE TRY AGAIN")
        b -= 1
    else:
        ch.append(int(c))
        obj.createGrid(int(c), s)
        a = obj.ckResult(ch,p1,p2)

    b += 1

print("THANKS FOR PLAYING")
