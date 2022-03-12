#tty game code
#need to come up with lives
#rock paper scissors 
import random


def play():
  computer_lives = 5
  player_lives = 5
  user = input("'r' for rock, 'p' for paper, 's' for scissors\n")
  computer = random.choice(['r', 'p', 's'])
  if user == computer:
    return 'It\'s a tie'

  if is_win(user, computer):
    computer_lives -= 1
    return 'You win'

  else:
    player_lives -= 1
    return 'You lost'

def is_win(player,opponent):
  if (player == 'r' and opponent == 's') or (player =='s' and opponent == 'p') or (player =='p' and opponent == 'r'):
    return True

print(play())


