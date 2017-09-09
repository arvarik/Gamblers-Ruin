# from scipy.stats import randint as ri
from random import randint
import numpy as np

class DiscretePMF:

  def __init__(self, pmf={}):
    ''' 
    Constructor given  dictionary that maps outcomes to their
    probabilities. Probabilities must sum to 1.

    Creates two numpy arrays for lower and upper bounds, and list of outcomes
    '''
    self.pmf = pmf

    if (sum(pmf.values()) != 1):
      raise ValueError("PMF is invalid.\nProbabilities do not sum to one.")

    self.keys = []
    self.lows = np.array([])
    self.highs = np.array([])

    for key, value in self.pmf.items():
      self.keys.append(key)
      value *= 100
      if len(self.keys) == 1:
        self.lows = np.append(self.lows, 0)
        self.highs = np.append(self.highs, value - 1)
      else:
        self.lows = np.append(self.lows, self.highs[-1] + 1)
        self.highs = np.append(self.highs, self.lows[-1] + value - 1)


  def __str__(self):
    """
    Changing objects to_string
    """
    rep = "-------------------\nDistribution\n-------------------\n"
    for key, value in self.pmf.items():
      rep += str(round(100*value, 3)) + "% chance of " + str(key) + "\n"

    return rep + "===================\n"


  def get_value(self):
    """
    Function to get a random variable from the given probabilty mass function
    """
    x = randint(0, 99)
    return self.keys[np.where((self.lows <= x) & (x <= self.highs))[0][0]]


  def get_expected_value(self):
    """
    Function to get the expected value of the probabilty distribution
    """
    ev = 0

    for key, value in self.pmf.items():
      ev += key*value

    return round(ev, 3)
