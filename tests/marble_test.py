from hamcrest import *
import unittest
from tests.src.marble__mania import marble_game
from tests.src.test_input import TEST_INPUT


class TestMarble(unittest.TestCase):

    def test_10_players(self):
        num_of_players = 10
        expected_dict = TEST_INPUT[str(num_of_players)]
        assert_that(marble_game(num_of_players, expected_dict["last_marble"]), has_entries(expected_dict))

    def test_13_players(self):
        num_of_players = 13
        expected_dict = TEST_INPUT[str(num_of_players)]
        assert_that(marble_game(num_of_players, expected_dict["last_marble"]), has_entries(expected_dict))

    def test_17_players(self):
        num_of_players = 17
        expected_dict = TEST_INPUT[str(num_of_players)]
        assert_that(marble_game(num_of_players, expected_dict["last_marble"]), has_entries(expected_dict))

    def test_21_players(self):
        num_of_players = 21
        expected_dict = TEST_INPUT[str(num_of_players)]
        assert_that(marble_game(num_of_players, expected_dict["last_marble"]), has_entries(expected_dict))

    def test_30_players(self):
        num_of_players = 30
        expected_dict = TEST_INPUT[str(num_of_players)]
        assert_that(marble_game(num_of_players, expected_dict["last_marble"]), has_entries(expected_dict))


if __name__ == "__main__":
    unittest.main()
