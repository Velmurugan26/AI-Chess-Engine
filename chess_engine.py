import copy

class ChessAI:
    def __init__(self, depth=3):
        self.depth = depth

    def evaluate_board(self, board):
        score = 0
        for row in board.board:
            for piece in row:
                if piece == "WP":
                    score += 1
                elif piece == "BP":
                    score -= 1
        return score

    def minimax(self, board, depth, maximizing_player, alpha, beta):
        if depth == 0 or board.is_game_over():
            return self.evaluate_board(board)

        if maximizing_player:
            max_eval = float('-inf')
            for move in board.get_all_moves("B"):
                new_board = copy.deepcopy(board)
                new_board.make_move(move, "B")
                eval = self.minimax(new_board, depth-1, False, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in board.get_all_moves("W"):
                new_board = copy.deepcopy(board)
                new_board.make_move(move, "W")
                eval = self.minimax(new_board, depth-1, True, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def get_best_move(self, board):
        best_move = None
        max_eval = float('-inf')
        for move in board.get_all_moves("B"):
            new_board = copy.deepcopy(board)
            new_board.make_move(move, "B")
            eval = self.minimax(new_board, self.depth-1, False, float('-inf'), float('inf'))
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return best_move
