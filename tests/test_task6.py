from unittest import TestCase

from constants import Constants, PlayerPosition, PlayerStats, TeamStats
from ed_utils.decorators import number, visibility
from tests.test_task5 import Roster
from awards import Awards
from player import Player
from random_gen import RandomGen
from season import Season
from typing import Union


class TestTask6(TestCase):
    def __verify_results(self, expected_results: list[list[Union[str, int, list]]]) -> None:
        for row_no, row in enumerate(self.awards.get_leaderboard()):
            for cell_no, cell in enumerate(row):
                self.assertEqual(expected_results[row_no][cell_no], cell)

    def setUp(self) -> None:
        RandomGen.set_seed(123)

    @number("6.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_get_top_x_players_by_tackles(self):
        teams = Roster.generate_teams(6)
        season = Season(teams)
        season.simulate_season()

        expected_results: tuple = ((-3, 'Ben Iniesta'), (-3, 'Matthew Pearson'),
                                   (-3, 'Saksham Ronaldo'), (-2, 'Lisa Mbappé'))
        players: list[tuple[int, str, Player]] = teams[0].get_top_x_players(PlayerStats.TACKLES, 4)
        for i, player in enumerate(players):
            self.assertEqual(expected_results[i][0], player[0])
            self.assertEqual(expected_results[i][1], player[1])
            self.assertEqual(-1*expected_results[i][0], player[2][PlayerStats.TACKLES])

    @number("6.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_get_top_x_players_by_goals(self):
        teams = Roster.generate_teams(6)
        season = Season(teams)
        season.simulate_season()


        expected_results: tuple = ((-6, 'Lisa Roberto'), (-5, 'Matthew Pearson'), (-3, 'Laura Stacie'),
                                   (-2, 'Ann Caicedo'), (-2, 'Lisa Mbappé'), (-2, 'Matthew Sparks'))
        players: list[tuple[int, str, Player]] = teams[0].get_top_x_players(PlayerStats.GOALS, 6)
        for i, player in enumerate(players):
            self.assertEqual(expected_results[i][0], player[0])
            self.assertEqual(expected_results[i][1], player[1])
            self.assertEqual(-1*expected_results[i][0], player[2][PlayerStats.GOALS])

    @number("6.3")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_small_leaderboard(self):
        teams = Roster.generate_teams(4)
        season = Season(teams)
        season.simulate_season()
        self.awards: Awards = Awards(season, PlayerStats.GOALS, 3)

        expected_results: list[list[Union[str, int]]] = [
                   ['Ann Caicedo',   6,   5,   0,   2,   0,   2,   4,  76, 173],
              ['Christian Wright',   6,   3,   2,   1,   2,   5,   5,  89, 180],
               ['Saksham Iniesta',   6,   3,   1,   0,   2,   1,   4,  87, 157],
                 ['Alexey Zidane',   6,   2,   1,   0,   1,   5,   5,  89, 169],
                 ['Hui Fernandes',   6,   2,   0,   1,   2,   3,   5,  85, 154],
                  ['Laura Stacie',   6,   2,   2,   0,   1,   1,   1,  87, 174],
                   ['Lisa Mbappé',   6,   2,   1,   1,   1,   1,   4,  71, 151],
                   ['Lisa Zidane',   6,   2,   0,   1,   0,   0,   5,  86, 179],
                ['Matthew Wright',   6,   2,   3,   0,   1,   5,   2,  88, 152],
                  ['Patrick Kerr',   6,   2,   0,   3,   0,   1,   5,  78, 155],
               ['Patrick Roberto',   6,   2,   0,   0,   2,   0,   1,  83, 162],
            ['Saksham Bellingham',   6,   2,   0,   3,   0,   4,   3,  79, 158],
        ]

        self.__verify_results(expected_results)
