
import chess
import chess.engine
from RobotArmControl import RobotArmControl


class ChessLogic: 
    def __init__(self):
        self.board = chess.Board()
        self.engine_path = 'C:\\Users\\mrena\\Downloads\\stockfish-windows-x86-64\\stockfish\\stockfish-windows-x86-64.exe'  
        self.engine = chess.engine.SimpleEngine.popen_uci(self.engine_path)
        self.robot_arm_control = RobotArmControl(port = 'COM3')


    def new_game(self):
        self.board.reset()

    # def get_piece_type_and_color(square):
    #     piece = chess.Board.piece_at(square)
    #     if piece is not None:
    #         piece_type = chess.piece_name(piece.piece_type).capitalize()
    #         color = "White" if piece.color == chess.WHITE else "Black"
    #         return f"{color} {piece_type}"
    #     else:
    #         return "No piece"
    
    
    def get_best_move(self, time_limit=2.1):
        result = self.engine.play(self.board, chess.engine.Limit(time=time_limit))
        return result.move 


    def make_move(self, move):
        try:
            move_obj = self.board.parse_san(move)  # SAN (Standard Algebraic Notation)
            if move_obj in self.board.legal_moves:
                self.board.push(move_obj)
                return True
            else:
                return False
        except ValueError:
            return False


    def current_board_state(self):
        return str(self.board)


    def close_engine(self):
        self.engine.quit()


# Game loop
    def play_game(self):
        self.new_game()
        while not self.board.is_game_over():
            print(self.current_board_state())


# Human move
            human_move = input("Enter your move: ")
            if not self.make_move(human_move):
                print("Invalid move, try again.")
                continue

            # Check if the game is over after the human move
            if self.board.is_game_over():
                break


#Engine move must be move  belonging to robot
            engine_move = self.get_best_move()

            if self.board.is_capture(chess.Move.from_uci(engine_move.uci())):
                print(f"bedebil")
                #usun figure
                print(f"removing a captured piece from : {(engine_move.uci()[2:4])}")
                self.robot_arm_control.remove_piece((engine_move.uci()[2:4]))
            else:
                print(f"niebede")

            self.make_move(engine_move.uci())
            print(f"Stockfish/Dobot plays: {engine_move.uci()}")
            # print(f"{engine_move.uci()}")


#Display current piece on start/end position
            # start_arm_coords_piece = self.chess_position_to_coordinates(engine_move.uci()[:2])
            # end_arm_coords_piece = self.chess_position_to_coordinates('e6')
            # print(f"start_arm_coords_piece: {start_arm_coords_piece}")
            print(f"end_arm_coords_piece: {(engine_move.uci()[2:4])}")
            print(f"end_arm_coords_piece: {chess.parse_square(engine_move.uci()[2:4])}")
            print(f"end_arm_coords_piece: {self.board.piece_at(chess.parse_square(engine_move.uci()[2:4]))}")
               

            self.robot_arm_control.execute_move(engine_move.uci())
             #print(f"Stockfish/Dobot plays")

                #if self.board.is_game_over():
           
        print("Game Over")
        print(self.current_board_state())

        # When done
        self.close_engine()



#if __name__ == "__main__":      
chess_logic = ChessLogic()
chess_logic.play_game()
