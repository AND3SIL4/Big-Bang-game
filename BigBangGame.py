class BigBangTheoryGame:
  def __init__(self, player_one, player_two):
    self.player_one = player_one
    self.player_two = player_two

  def verify_win_game(self):
      valid_data = ["rock", "paper", "scissors", "lizard", "spock"]

      if self.player_one not in valid_data or self.player_two not in valid_data:
        print("Ingresa una opcion valida (rock, paper, scissors, lizard,spock)")

      elif self.player_one == self.player_two:
          print("It's a tie")
      elif (
          (self.player_one == "rock" and (self.player_two == "scissors" or self.player_two == "lizard")) or
          (self.player_one == "paper" and (self.player_two == "rock" or self.player_two == "spock")) or
          (self.player_one == "scissors" and (self.player_two == "paper" or self.player_two == "lizard")) or
          (self.player_one == "lizard" and (self.player_two == "paper" or self.player_two == "spock")) or
          (self.player_one == "spock" and (self.player_two == "rock" or self.player_two == "scissors"))
      ):
          print("player 1 wins with", self.player_one)
      else:
        print("player 2 wins with", player_two)

player_one = input("Player 1, choose an option (rock, paper, scissors, lizard, spock): ").lower()
player_two = input("Player 2, choose an option (rock, paper, scissors, lizard, spock): ").lower()

game_one = BigBangTheoryGame(player_one, player_two)
game_one.verify_win_game()

# verify_win_game(player_one, player_two)