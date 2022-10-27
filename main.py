import random


class PencilGame:
    def __init__(self):
        self.players = ("Caleb", "Anna")

        self.pencil_count = None
        self.current_player = None

    def main(self):
        self.pencil_count = self.get_starting_pencil_count()
        self.current_player = self.set_first_turn()

        while self.pencil_count > 0:
            print("|" * self.pencil_count)
            print(f"{self.current_player}'s turn:")

            move = self.get_move_from_current_player()

            self.execute_move(move)
            self.check_for_winner()

            self.switch_players()

        return

    @staticmethod
    def get_starting_pencil_count():
        starting_pencils = input("How many pencils would you like to use:\n")
        while True:
            if not starting_pencils.isnumeric():
                print("The number of pencils should be numeric")
            elif starting_pencils == '0':
                print("The number of pencils should be positive")
            else:
                break

            starting_pencils = input()

        return int(starting_pencils)

    def get_move_from_current_player(self):
        if self.current_player == self.players[0]:
            move = self.get_legal_move_from_player()
        else:
            move = self.get_bot_move()
            print(move)  # We have to print the bot's move manually since it's not entered in manually via the console

        return move

    def set_first_turn(self):
        first_turn = input(f"Who will be the first ({', '.join(self.players)}):\n")
        while True:
            if first_turn not in self.players:
                first_turn = input(f"Choose between {self.players[0]} and {self.players[1]}\n")
            else:
                return first_turn

    def get_legal_move_from_player(self):
        while True:
            move = input()
            if move not in ('1', '2', '3'):
                print("Possible values: '1', '2' or '3'")
            elif int(move) > self.pencil_count:
                print("Too many pencils were taken")
            else:
                return int(move)

    def check_for_winner(self):
        if self.pencil_count == 0:
            winner = "Caleb" if (self.current_player == "Anna") else "Anna"
            print(f"{winner} won!")
        else:
            return

    def execute_move(self, move: int):
        self.pencil_count -= move
        return

    def get_bot_move(self):
        if self.pencil_count % 4 == 1:
            move = random.choice([i for i in range(1, min(self.pencil_count + 1, 4))])
        else:
            move = self.winning_strategy_move()

        return move

    def winning_strategy_move(self):
        for num in (1, 2, 3):
            if (self.pencil_count - num) % 4 == 1:
                return num

    def switch_players(self):
        self.current_player = "Caleb" if (self.current_player == "Anna") else "Anna"
        return


stage = PencilGame()
stage.main()
