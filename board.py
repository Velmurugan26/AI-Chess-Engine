class ChessBoard:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board = [["--"]*8 for _ in range(8)]
        for i in range(8):
            board[1][i] = "WP"
            board[6][i] = "BP"
        return board

    def make_move(self, move, player):
        try:
            start_col = ord(move[0].lower()) - ord('a')
            start_row = 8 - int(move[1])
            end_col = ord(move[2].lower()) - ord('a')
            end_row = 8 - int(move[3])
        except:
            return False

        piece = self.board[start_row][start_col]
        if (player=="W" and piece.startswith("W")) or (player=="B" and piece.startswith("B")):
            self.board[end_row][end_col] = piece
            self.board[start_row][start_col] = "--"
            return True
        return False

    def get_all_moves(self, player):
        moves = []
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if (player=="W" and piece.startswith("W")) or (player=="B" and piece.startswith("B")):
                    direction = -1 if player=="W" else 1
                    new_r = r + direction
                    if 0 <= new_r < 8:
                        moves.append(f"{chr(c+97)}{8-r}{chr(c+97)}{8-new_r}")
        return moves

    def is_game_over(self):
        wp = bp = False
        for row in self.board:
            for piece in row:
                if piece.startswith("W"):
                    wp = True
                if piece.startswith("B"):
                    bp = True
        return not (wp and bp)

    def get_winner(self):
        wp = bp = False
        for row in self.board:
            for piece in row:
                if piece.startswith("W"):
                    wp = True
                if piece.startswith("B"):
                    bp = True
        if wp and not bp:
            return "White"
        elif bp and not wp:
            return "Black"
        else:
            return None
