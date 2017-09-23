import sys
sys.path.append('../../src')

from models.discrete_random_walk import RandomWalk
from stats.discrete_pmf import DiscretePMF


def test_discrete_pmf():
  """
  Test method to test DiscretePMF module
  """
  pmf = DiscretePMF({-1:.5, 1:.3, 10:.2})
  print(pmf.get_value(), "\n")
  print(pmf.get_value(), "\n")
  print(pmf.get_value(), "\n")
  print(pmf.get_value(), "\n")
  print(pmf.get_value(), "\n")
  print(pmf.get_expected_value())

  print(str(pmf))

def test_random_walk():
  """
  Test method to test the RandomWalk module
  """
  random_walk = RandomWalk({-2:.25, -1:.25, 1:.25, 2:.25})

  random_walk.play_game(200, 50)


if __name__ == '__main__':
  """
  Main method to call test functions
  """
  test_random_walk()
  # test_discrete_pmf()
  
