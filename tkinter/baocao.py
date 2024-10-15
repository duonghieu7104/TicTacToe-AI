import tkinter as tk
from engine import TicTacToe
from tkinter.messagebox import showinfo

class user_interface():
    def __init__(self, root):
        self.row = 0
        self.col = 0
        self.cod = [
        [[[(22, 163), (163, 22)], [(22, 22), (163, 163)]],
        [[(222, 163), (363, 22)], [(222, 22), (363, 163)]],
        [[(422, 163), (563, 22)], [(422, 22), (563, 163)]]],
        [[[(22, 222), (163, 363)], [(22, 363), (163, 222)]],
        [[(222, 363), (363, 222)], [(222, 222), (363, 363)]],
        [[(422, 363), (563, 222)], [(422, 222), (563, 363)]]],
        [[[(22, 563), (163, 422)], [(22, 422), (163, 563)]],
        [[(222, 563), (363, 422)], [(222, 422), (363, 563)]],
        [[(422, 563), (563, 422)], [(422, 422), (563, 563)]]]
        ]
        self.center = [[[100, 100], [300, 100], [500, 100]], [[100, 300],
                       [300, 300], [500, 300]],[[100, 500],[300, 500],[500, 500]]]

        self.result  = 2
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.c = tk.Canvas(root, height=600, width=600, bg='white')
        self.c.pack(fill=tk.BOTH, expand=True)
        self.bot = TicTacToe()
        self.moves = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]

    def create_grid(self, event=None):
        w = self.c.winfo_width()
        h = self.c.winfo_height()
        self.c.delete('grid_line')
        
        for i in range(200, w-200, 200):
            self.c.create_line([(i, 0), (i, h)], width=10)
        
        for i in range(200, h-200, 200):
            self.c.create_line([(0, i), (w, i)], width=10)

    def valid(self, row, col):
        if self.board[row][col] == '-':
            return True
        return False

    def won(self):
        for i in range(0,3):
            if(self.board[i][0]==self.board[i][1] and
               self.board[i][1]==self.board[i][2]):
                if self.board[i][0]=='X':
                    return 1
                elif self.board[i][0]=='O':
                    return -1

        for i in range(3):
            if(self.board[0][i]==self.board[1][i] and
               self.board[1][i]==self.board[2][i]):
                if self.board[0][i]=='X':
                    return 1
                elif self.board[0][i]=='O':
                    return -1

        if(self.board[0][0]==self.board[1][1] and
           self.board[1][1]==self.board[2][2]):
            if self.board[0][0]=='X':
                    return 1
            elif self.board[0][0]=='O':
                    return -1

        if(self.board[0][2]==self.board[1][1] and
           self.board[1][1]==self.board[2][0]):
            if self.board[2][0]=='X':
                    return 1
            elif self.board[2][0]=='O':
                    return -1
        return 0

    def __get_block__(self, eventorigin):
        x = eventorigin.x
        y = eventorigin.y
        self.row = -1
        self.col = -1
        for i in range(0, 600, 200):
            if(x>i):
                self.col += 1
            if(y>i):
                self.row += 1
        
        return [self.row, self.col]

    def __draw_peices(self, eventorigin):
        row, col = self.__get_block__(eventorigin)
        if self.valid(row, col):
            self.c.create_line(self.cod[row][col][0], width=10, smooth=1,)
            self.c.create_line(self.cod[row][col][1], width=10, smooth=1,)
            self.board[row][col] = 'X'
            return True
        return False
        


    def __bot_peices(self):
        row, col = self.move
        self.c.create_oval(self.center[row][col][0]-50,
                      self.center[row][col][1]-50,
                      self.center[row][col][0]+50,
                      self.center[row][col][1]+50, fill="black")
        self.board[row][col] = 'O'

    def play(self, eventorigion):
        c = self.__draw_peices(eventorigion)
        if c:
            x = self.board[0]+self.board[1]+self.board[2]
            t = self.bot.findBestMove(x)
        try:
            if t != None:
                self.move = self.moves[t]
        except:
            pass
        if c:
            self.__bot_peices()
        if self.won() == 1:
            res = "You Win"
            self.result = 1
            self.c.unbind("<Button 1>")
            showinfo("Result", res)
            c = False
        elif self.won() == -1:
            res = "Bot Win"
            self.result = -1
            self.c.unbind("<Button 1>")
            showinfo("Result", res)
            c = False
        try:
            if t == None and self.result == 2:
                res = "Game Over It's a Tie"
                self.result = 0
                self.c.unbind("<Button 1>")
                showinfo("Result", res)
        except:
            pass
                


root = tk.Tk()
root.title("Tic Tac Toe")
x = user_interface(root)
x.c.bind('<Configure>', x.create_grid)
x.c.bind("<Button 1>", lambda event:x.play(event))
root.mainloop()
