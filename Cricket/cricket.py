"""
PROGRESS :-
> out function               done!.
> switch player              done!.
> avoid overloading          done!.
> avoid more than 6 error player bat and ball  done!.
> already win problem + (exclude last element) done!.
> ultimate legendary GUI version :)            done!.
"""
import random

sum_computer = 0
sum_player = 0


def instructions():
    print(
        """
first you can choose to bat or ball.
if you choose bat,the game will be like ->

player: bats
computer: balls

The player can press the number between [1-6] to bat and score.
The computer will choose any number between [1-6] and the ball.
if the number that player batted and computer balled is the same
results in 'PLAYER OUT'

then (after switching),
computer: bats
player: balls

The computer will choose any number between [1 and 6] to bat and score.
The player can press the number between [1-6] to ball.
If the number that the computer batted and the player balled is the same, it results in 'COMPUTER OUT'

If a player gets the computer 'OUT' before it scores more than the player, the player wins.
if the computer scores more than the player, the computer wins.
          """
    )


def player_play():
    global sum_player
    score_player = []

    while True:
        # player = random.randint(1, 6)  # Automate batting

        player = None
        while player not in [1, 2, 3, 4, 5, 6]:
            player = input("Player bats    : ")

            if player.isdigit():
                player = int(player)

        computer = random.randint(1, 6)

        score_player.append(player)

        print(f"Computer balls : {computer}\n")

        if player == computer:
            score_player.pop()
            print("*******************************")
            print("Game status   = Player out!")
            print("score board   =", score_player)
            for x in score_player:
                sum_player = sum_player + x
            print("Player scored =", sum_player, "runs")
            print("*******************************")
            break
    return sum_player


def computer_play():
    global sum_computer
    score_computer = []
    while True:
        computer = random.randint(1, 6)

        # player = random.randint(1, 6)  # Automate Balling.

        player = None
        while player not in [1, 2, 3, 4, 5, 6]:
            player = input("Player balls   : ")

            if player.isdigit():
                player = int(player)

        score_computer.append(computer)

        print("Computer bats : {}\n".format(computer))

        if computer == player:
            score_computer.pop()
            print("*******************************")
            print("Game status     = Computer out!")
            print("Score board     =", score_computer)
            for x in score_computer:
                sum_computer = sum_computer + x
            print("Computer scored =", sum_computer, "runs")
            print("*******************************")
            break
    return sum_computer


def check_runs(a, b):
    print()
    print(">>>>>>>> 'RESULT' <<<<<<<<")

    if a > b:
        z = a - b
        print(" Player won for", str(z), "runs")
        print(">>>>>>>>>>>>:)<<<<<<<<<<<<")

    elif b > a:
        v = b - a
        print(" Computer won for", str(v), "runs")
        print(">>>>>>>>>>>>:(<<<<<<<<<<<<")

    elif a == b:
        print("           Draw!")
        print(">>>>>>>>>>>>:|<<<<<<<<<<<<")


def play():
    global sum_computer, sum_player
    print("Welcome to PyCricket")

    while True:
        toss = None
        options = ["bat", "ball"]
        while toss not in options:
            toss = input("bat or ball ? : ").lower()
        print("==================")

        if toss == "bat":
            player_play()
            computer_play()
            check_runs(sum_player, sum_computer)
            sum_player = 0
            sum_computer = 0

        elif toss == "ball":
            computer_play()
            player_play()
            check_runs(sum_player, sum_computer)
            sum_player = 0
            sum_computer = 0

        print()
        print("Wow, Good game!")
        play_again = input('wanna play again? (y/n):').lower()

        if play_again != 'y':
            print("Bye then,")
            break


if __name__ == '__main__':
    instruction = input("Do you want instructions on this game?(y/n) :")
    if instruction == "y":
        instructions()

    play()
