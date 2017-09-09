from discrete_pmf import DiscretePMF

class GamblersRuin:

  def __init__(self, pmf={-1:.5, 1:.5}, threshold_gain=5, threshold_lose=-5):
    """
    Constructor for Gamblers Ruin model.

    Input is probability mass function of game and thresholds for showing gain
    and loss streaks
    """

    self.pmf = DiscretePMF(pmf)
    self.money = 0
    self.iterations = 0

    self.streak = 0
    self.streak_threshold_gain = 0
    self.streak_threshold_loss = 0

    self.gain_streak = 0
    self.lose_streak = 0

    self.gain = set()
    self.lose = set()
    self.money_set = set()

    self.threshold_gain = threshold_gain
    self.threshold_lose = threshold_lose

    print(str(self.pmf))


  def play_game(self, money, iterations):
    """
    Method to simulate a player playing the game.

    Input amount of money the player comes to play with and number of times
    the player wants to play
    """

    print("Playing Game...")
    self.money = money
    self.iterations = iterations

    for i in range(iterations):

      result = self.pmf.get_value()

      self.money += result
      self.streak += result

      if (result > 0):
        self.gain_streak += result
        self.lose_streak = 0
        self.gain.add(self.gain_streak)
      else:
        self.gain_streak = 0
        self.lose_streak += result
        self.lose.add(self.lose_streak)

      self.money_set.add(self.money)

      self.play_game_print(i, self.streak, self.money)

    self.game_final_print(money)



  def play_game_print(self, game_num, streak, money):
    """
    Print method after every individual game to check for gain/loss streak
    """

    if (streak == self.threshold_gain):
      print("GAINED  {}\tGAME {}  \tMONEY {}".format(streak, game_num + 1, money))
      self.streak = 0

    if (streak == self.threshold_lose):
      print("LOST   {}\tGAME {}  \tMONEY {}".format(streak, game_num + 1, money))
      self.streak = 0


  def game_final_print(self, money):
    """
    Print method when player finally stops playing.
    Prints stats of players win/loss
    """

    print("\nStarted with ${}".format(money))
    print("Final net worth after {} games played: ${}\n".format(self.iterations,
                                                                self.money))
    print("Biggest win streak:   ${}".format(max(self.gain)))
    print("Biggest lose streak: -${}".format(-1*min(self.lose)))
    print("Most amount of money had:  {}".format(max(self.money_set)))
    print("Least amount of money had: {}\n".format(min(self.money_set))) 

