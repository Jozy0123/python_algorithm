from StackAndQueue.StackAndQueue import SStack

class occupied(ValueError):
    pass

class outofbound(ValueError):
    pass

class queens:

    queen_num = 0

    def __init__(self, pos = (0, 0)):
        self.pos = pos
        self.attacking_pos = []
        for i in range(8):
            for j in range(8):
                if i == pos[0]:
                    self.attacking_pos.append((i, j))
                elif j == pos[1] and i != pos[0]:
                    self.attacking_pos.append((i, j))
                elif self.pos[0] - i == self.pos[1] - j:
                    self.attacking_pos.append((i, j))
                elif self.pos[0] - i == j - self.pos[1]:
                    self.attacking_pos.append((i, j))
        queens.queen_num += 1

    def attacking_pos_print(self):
        print(self.attacking_pos)

    @classmethod
    def get_queen_num(cls):
        return queens.queen_num


class chessBoard:

    def __init__(self, board_x = 8, board_y = 8):
        self.board_x = board_x
        self.board_y = board_y
        self.make_board()

    def make_board(self):
        bd = []
        for i in range(self.board_x):
            bd_1 = []
            for j in range(self.board_y):
                bd_1.append(0)
            bd.append(bd_1)
        self.board = bd

    def board_print(self):
        print(self.board)

    def is_occupy(self, pos):
        if pos[0] > 8 or pos[0] < 0 or pos[1] > 8 or pos[1] <0:
            return
        copy = self.board
        return copy[pos[0]][pos[1]] ==  1

    def occupy(self, pos):
        if pos[0] > 8 or pos[0] < 0 or pos[1] > 8 or pos[1] <0:
            raise outofbound("position not on board")
        if not self.is_occupy(pos):
            copy = self.board
            copy[pos[0]][pos[1]] = 1
            self.board = copy

    @staticmethod
    def get_next_pos(pos):
        x = pos[0]
        y = pos[1] + 1
        if y > 7:
            x, y = x + 1, 0
            if x > 7:
                return (-1, -1)
            new_pos = (x, y)
        else:
            new_pos = (x, y)
        return new_pos

    @staticmethod
    def validate_pos(pos):
        if pos[0] < 8 and pos[0] >= 0 and pos[1] < 8 and pos[0] >= 0:
            return True
        else:
            return False

    def occupy_next_pos(self, pos, occupy = True):

       new_pos = pos
       while True:
           new_pos = chessBoard.get_next_pos(new_pos)
           if not chessBoard.validate_pos(new_pos):
               return (-1, -1)
           elif not self.is_occupy(new_pos) and occupy:
               self.board[pos[0]][pos[1]] = 1
               return new_pos
           elif not self.is_occupy(new_pos) and occupy == False:
               return new_pos
           else:
               continue

    def put_queen(self, i, j):
        queen = queens((i,j))
        if self.is_occupy((i,j)):
            return
        self.occupy((i, j))
        for o in queen.attacking_pos:
            self.occupy(o)


if __name__ == "__main__":

    newboard = chessBoard()
    queens_list = []

    for i in range(8):
        for j in range(8):
            if len(queens_list) < 9:
                if not newboard.is_occupy((i,j)):
                    newboard.put_queen(i,j)
                    queens_list.append((i, j))
    print(queens_list)

    while True:
        if len(queens_list) < 9:
            # print(queens_list)
            latest_pos = queens_list.pop()
            if len(queens_list) == 0:
                init_queen = chessBoard.get_next_pos(latest_pos)
                if chessBoard.validate_pos(init_queen):
                    queens_list.append(init_queen)
                else:
                    break
            newboard = chessBoard()
            for k in queens_list:
                newboard.put_queen(k[0], k[1])
            next_pos = newboard.occupy_next_pos(latest_pos, False)
            while chessBoard.validate_pos(next_pos) and len(queens_list) < 9:
                if not chessBoard.validate_pos(next_pos):
                    break
                else:
                    new_queen = queens(next_pos)
                    queens_list.append(next_pos)
                    newboard.put_queen(next_pos[0], next_pos[1])
                    next_pos = newboard.occupy_next_pos(next_pos, occupy = False)
            if len(queens_list) == 8:
                print(queens_list)
            continue
        else:
            break
