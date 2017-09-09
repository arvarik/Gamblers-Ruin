from gamblers_ruin import GamblersRuin
from discrete_pmf import DiscretePMF


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

def test_gamblers_ruin():
  """
  Test method to test the GamblersRuin module
  """
  gamblers_ruin = GamblersRuin({-2:.25, -1:.25, 1:.25, 2:.25})

  gamblers_ruin.play_game(200, 50)


if __name__ == '__main__':
  """
  Main method to call test functions
  """
  test_gamblers_ruin()
  # test_discrete_pmf()
  