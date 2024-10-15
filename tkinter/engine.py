import random

class TicTacToe():
    def __init__(self):
        self.board = None
        self.moves = ['X', 'O']

    def show(self):
        for element in [self.board[i:i + 3] for i in range(0, len(self.board), 3)]:
            print(element)

    def get_free_positions(self):
        """what spots are left empty?"""
        return [k for k, v in enumerate(self.board) if v is '-']


    def evaluate(self):
        for i in range(0,9,3):
            if(self.board[i]==self.board[i+1] and
               self.board[i+1]==self.board[i+2]):
                if self.board[i]=='X':
                    return -10
                elif self.board[i]=='O':
                    return 10

        for i in range(3):
            if(self.board[i]==self.board[i+3] and
               self.board[i+3]==self.board[i+6]):
                if self.board[i]=='X':
                    return -10
                elif self.board[i]=='O':
                    return 10

        if(self.board[0]==self.board[4] and
           self.board[4]==self.board[8]):
            if self.board[0]=='X':
                    return -10
            elif self.board[0]=='O':
                    return 10

        if(self.board[2]==self.board[4] and
           self.board[4]==self.board[6]):
            if self.board[2]=='X':
                    return -10
            elif self.board[2]=='O':
                    return 10
    

    def negamax(self, move, alpha=-float('inf'), beta=float('inf'), depth=0):
        score = self.evaluate()
        fp = self.get_free_positions()

        if score == 10:
            return score
        if score == -10:
            return score
        if len(fp) == 0:
            return 0

        best_value = -float('inf')

        for pos in fp:
            self.board[pos] = self.moves[move]
            value = -self.negamax(not move, -beta, -alpha, depth + 1)
            self.board[pos] = '-'

            best_value = max(best_value, value)
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return best_value


    def findBestMove(self, board):
        bestVal = -1000
        choices = []
        self.board = board

        if len(self.get_free_positions()) == 9:
            return 4

        for pos in self.get_free_positions():
            self.board[pos] = "O"
            val = self.negamax(False)
            self.board[pos] = '-'

            if val > bestVal:
                bestVal = val
                choices = [pos]
            elif val == bestVal:
                choices.append(pos)

        if choices != []:
            return random.choice(choices)
        else:
            return None


