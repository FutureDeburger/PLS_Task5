

class GameBoard:
    """Инициализация игрового поля"""
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def print_board(self):
        for x in self.board:
            print(' '.join(map(str, x)))

    def check_to_add_piece(self, piece, x, y):
        for row in range(piece.height):
            for columns in range(piece.width):
                if piece.shape[row][columns] == 1:
                    board_x, board_y = x + row, y + columns

                    if board_x >= self.height or board_y >= self.width:
                        return False

                    if self.board[board_x][board_y] == 1:
                        return False
        return True

    def move_piece_on_board(self, piece, x, y):
        if self.check_to_add_piece(piece, x, y):
            for row in range(piece.height):
                for columns in range(piece.width):
                    if piece.shape[row][columns] == 1:
                        self.board[x + row][y + columns] = 1
            return True
        return False

    def delete_occupied_rows_and_columns(self):

        def remove_full_string(input_list):
            new_list = []
            for row in input_list:
                if sum(row) == self.width:
                    row = [0 for _ in range(self.width)]
                    new_list.append(row)
                else:
                    new_list.append(row)
            return new_list

        board_with_deleted_full_rows = remove_full_string(self.board) # удаляю заполненные строки
        zipped_board_with_deleted_full_rows = zip(*board_with_deleted_full_rows)
        transposed_board_with_deleted_full_rows = [list(_) for _ in zipped_board_with_deleted_full_rows] # здесь получил транспонированную матрицу
        board_with_deleted_full_columns = remove_full_string(transposed_board_with_deleted_full_rows) # удалил заполненные строки из транспонированной матрицы
        transposed_board_with_deleted_full_columns = [list(_) for _ in zip(* board_with_deleted_full_columns)] # получил двумерный массив
        self.board = transposed_board_with_deleted_full_columns

        return self.board

    # def find_piece_on_board_right_now(self, piece, x, y):
    #     list_of_pieces_on_board = []
    #     if self.move_piece_on_board(piece, x, y):
    #         list_of_pieces_on_board.append(piece)
    #     return print(list_of_pieces_on_board)

class GamePiece:
    """Инициализация фигур"""
    def __init__(self, shape: list, color):
        self.shape = shape
        self.color = color
        self.height = len(shape)
        self.width = len(shape[0])


class PieceManager:
    """Хранение фигур"""
    def __init__(self):
        self.pieces = {'a': GamePiece([[1]], 'b'), 'b': GamePiece([[1, 1]], 'g'), 'c': GamePiece([[1], [1]], 'r'), 'd': GamePiece([[1, 1, 1]], 'y'),
                       'e': GamePiece([[1], [1], [1]], 'b'),  'f': GamePiece([[1, 1, 1, 1]], 'y'), 'g': GamePiece([[1], [1], [1], [1]], 'c'),
                       'h': GamePiece([[1, 1], [1, 1]], 'g'), 'i': GamePiece([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 'r'), 'j': GamePiece([[0, 1], [1, 1]], 'c'),
                       'k': GamePiece([[1, 0], [1, 1]], 'y'), 'l': GamePiece([[1, 1], [0, 1]], 'b'), 'm': GamePiece([[1, 1], [1, 0]], 'r'),
                       'n': GamePiece([[1, 1, 1, 1, 1]], 'b'), 'o': GamePiece([[1], [1], [1], [1], [1]], 'r'), 'p': GamePiece([[0, 0, 1], [0, 0, 1], [1, 1, 1]], 'g'),
                       'q': GamePiece([[1, 0, 0], [1, 0, 0], [1, 1, 1]], 'c'), 'r': GamePiece([[1, 1, 1], [0, 0, 1], [0, 0, 1]], 'y'), 's': GamePiece([[1, 1, 1], [1, 0, 0], [1, 0, 0]], 'g')
                      }

    def print_piece(self, key: str):
        if key in self.pieces:
            for row in self.pieces[key].shape:
                print(' '.join(str(cell) for cell in row))
        else:
            print(f'Введённого ключа {key} не существует.')



board = GameBoard(10, 10) # создаю моё поле

manager = PieceManager()


piece1 = manager.pieces['n']
board.move_piece_on_board(piece1, 0, 0)
board.move_piece_on_board(piece1, 0, 5)
board.move_piece_on_board(piece1, 1, 0)
board.move_piece_on_board(piece1, 1, 5)


piece3 = manager.pieces['i']
board.move_piece_on_board(piece3, 7, 3)

piece4 = manager.pieces['k']
board.move_piece_on_board(piece4, 4, 0)


# piece5 = manager.pieces['o']
# board.move_piece_on_board(piece5, 0, 9)
# board.move_piece_on_board(piece5,5, 9)


board.print_board()
print("\n")

board.delete_occupied_rows_and_columns()

board.print_board()