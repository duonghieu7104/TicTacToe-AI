import streamlit as st
from easyAI import TwoPlayersGame, AI_Player, Negamax
from easyAI.Player import Human_Player

class GameController(TwoPlayersGame):
    def __init__(self, players):
        self.players = players
        self.nplayer = 1  # Người chơi hiện tại là người chơi số 1
        self.board = [0] * 9

    def possible_moves(self):
        return [str(a+1) for a, b in enumerate(self.board) if b == 0]

    def make_move(self, move):
        self.board[int(move)-1] = self.nplayer

    def unmake_move(self, move):  # Cần thiết cho thuật toán Negamax
        self.board[int(move)-1] = 0

    def loss_condition(self):
        # Định nghĩa các trường hợp thắng cuộc
        winning_positions = [[1,2,3], [4,5,6], [7,8,9],
                             [1,4,7], [2,5,8], [3,6,9],
                             [1,5,9], [3,5,7]]
        return any(all(self.board[pos-1] == self.nopponent
                       for pos in line) for line in winning_positions)

    def is_over(self):
        return (self.possible_moves() == []) or self.loss_condition()

    def show(self):
        # Hiển thị bàn cờ trong terminal hoặc console
        print('\n'+'\n'.join([' '.join([['.', 'X', 'O'][self.board[3*j+i]]
                                         for i in range(3)]) for j in range(3)]))

    def scoring(self):
        return -100 if self.loss_condition() else 0

    def switch_player(self):
        self.nplayer = 2 if self.nplayer == 1 else 1

# Tạo giao diện Streamlit
st.title('Tic Tac Toe with AI')

# Khởi tạo trò chơi
if 'game' not in st.session_state:
    st.session_state.game = GameController([Human_Player(), AI_Player(Negamax(7))])

# Tạo một container duy nhất cho bảng trò chơi
board_container = st.container()

def show_board(board):
    # Xóa container cũ trước khi tạo container mới
    
    
    with board_container:
        cols = st.columns(3)
        for i in range(3):
            for j in range(3):
                cell_index = 3*i + j
                unique_key = f'button_{cell_index}_{str(board)}'
                if board[cell_index] == 0:
                    if cols[j].button(' ', key=unique_key):
                        st.session_state.game.make_move(str(cell_index + 1))
                        st.session_state.game.switch_player()
                else:
                    cols[j].write('X' if board[cell_index] == 1 else 'O')


show_board(st.session_state.game.board)

# Kiểm tra kết thúc trò chơi
if st.session_state.game.is_over():
    if st.session_state.game.loss_condition():
        st.write(f'Player {3 - st.session_state.game.nplayer} wins!')
    else:
        st.write('It\'s a tie!')

# Chạy AI nếu đến lượt nó
if st.session_state.game.nplayer == 2 and not st.session_state.game.is_over():
    ai_player = st.session_state.game.players[1]
    move = ai_player.ask_move(st.session_state.game)
    st.session_state.game.make_move(move)
    st.session_state.game.switch_player()
    st.experimental_rerun()
    show_board(st.session_state.game.board)