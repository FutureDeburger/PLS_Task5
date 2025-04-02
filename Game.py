
class GameBoard:
    """Инициализация игрового поля"""
    def __init__(self, width: int, height: int):
        self.height = height
        self.width = width
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
        list_of_pieces_on_board = [] # в дальнейшем хочу использовать для создания блокчейна карты
        if self.check_to_add_piece(piece, x, y):
            for row in range(piece.height):
                for columns in range(piece.width):
                    if piece.shape[row][columns] == 1:
                        self.board[x + row][y + columns] = 1
            return True
        return False


    # def find_piece_on_board_right_now(self):
    #     list_of_pieces_on_board = []
    #     if self.move_piece_on_board(self):
    #         list_of_pieces_on_board.append(piece + x + y)
    #     print(list_of_pieces_on_board)


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
#board.print_board()
manager = PieceManager()
#manager.print_piece('a')

piece1 = manager.pieces['h']
board.move_piece_on_board(piece1, 5, 5)

piece2 = manager.pieces['f']
board.move_piece_on_board(piece2, 1, 2)

board.print_board()

