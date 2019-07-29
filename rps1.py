import random


class Player():
    human_input = 0
    opponents_move = 0

    moves = ['rock', 'paper', 'scissors']

    def move(self):
        return 'rock'

    def learn(self, human_input, opponents_move):
        return human_input, opponents_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            human_input = input("Rock, paper, scissors?").lower()
            if human_input in self.moves:
                return human_input
            else:
                print("Please choose again."
                      " Don't forget to check your spelling!")
        return human_input


class ReflectPlayer(Player):
    def move(self):
        if self.opponents_move == 0:
            return random.choice(self.moves)
        return self.opponents_move

    def learn(self, human_input, opponents_move):
        self.opponents_move = opponents_move


class CyclePlayer(Player):
    def __init__(self):
        self.index = 0
        super(CyclePlayer, self).__init__()

    def move(self):
        if self.index > 2:
            self.index = 0

        self.human_input = moves[self.index]
        self.index += 1
        return self.human_input


class Game():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0
        

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nHuman Player: {move1}  Opponent: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            self.p1_score += 1
            print("\n* Human Player wins for this round! *")
        elif beats(move2, move1):
            self.p2_score += 1
            print("\n* Opponent wins for this round! *")
        else:
            print("\n* TIE for this round *")
        print(f"\n(score) Human Player: {self.p1_score}, "
              f"Opponent: {self.p2_score} ")

    def play_game(self):
        print("Game start!\n""Rock, Paper, Scissors?\n")
        for round in range(5):
            print(f"Round{round}:")
            self.play_round()
        print(f"\n(score) Human Player: {self.p1_score}, "
              f"Opponent: {self.p2_score} ")

        if self.p1_score > self.p2_score:
            print("\n*** Human Player wins! ***")
        elif self.p1_score < self.p2_score:
            print("\n*** Opponent wins! ***")
        else:
            print("\n*** Tie ***")
        print("\nGame Over!")


if __name__ == '__main__':
    game = Game(Human_player(), Opponent())
    game.play_game()
