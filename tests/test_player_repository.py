import unittest

from app.models.game_stats import GameStats
from app.repositories.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        self.game_stats_list = [
            GameStats("John Doe", "PG", 6, 6, 0, 4, 4, 4, 1, 1, 4, 2, 2),
            GameStats("John Doe", "PG", 5, 5, 1, 3, 2, 2, 0, 0, 3, 1, 0),
            GameStats("John Doe", "PG", 4, 4, 2, 5, 1, 3, 2, 1, 2, 0, 1),
            GameStats("Alice Smith", "C", 4, 5, 2, 6, 1, 3, 10, 2, 3, 1, 0),
            GameStats("Alice Smith", "C", 3, 3, 0, 2, 1, 1, 7, 0, 2, 2, 1),
            GameStats("Alice Smith", "C", 2, 2, 1, 4, 0, 2, 8, 1, 1, 0, 2),
        ]

        self.player_repository = PlayerRepository(self.game_stats_list)

    def test_get_player_stats_by_name_valid(self):
        result = self.player_repository.get_player_stats_by_name("John Doe")
        expected_result = [
            GameStats("John Doe", "PG", 6, 6, 0, 4, 4, 4, 1, 1, 4, 2, 2),
            GameStats("John Doe", "PG", 5, 5, 1, 3, 2, 2, 0, 0, 3, 1, 0),
            GameStats("John Doe", "PG", 4, 4, 2, 5, 1, 3, 2, 1, 2, 0, 1),
        ]

        for result_game_stats, expected_game_stats in zip(result, expected_result):
            self.assertEqual(result_game_stats.player, expected_game_stats.player)
            self.assertEqual(result_game_stats.position, expected_game_stats.position)
            self.assertEqual(result_game_stats.ftm, expected_game_stats.ftm)
            self.assertEqual(result_game_stats.fta, expected_game_stats.fta)
            self.assertEqual(result_game_stats.two_pm, expected_game_stats.two_pm)
            self.assertEqual(result_game_stats.two_pa, expected_game_stats.two_pa)
            self.assertEqual(result_game_stats.three_pm, expected_game_stats.three_pm)
            self.assertEqual(result_game_stats.three_pa, expected_game_stats.three_pa)
            self.assertEqual(result_game_stats.reb, expected_game_stats.reb)
            self.assertEqual(result_game_stats.blk, expected_game_stats.blk)
            self.assertEqual(result_game_stats.ast, expected_game_stats.ast)
            self.assertEqual(result_game_stats.stl, expected_game_stats.stl)
            self.assertEqual(result_game_stats.tov, expected_game_stats.tov)


    def test_get_player_stats_by_name_invalid(self):
        result = self.player_repository.get_player_stats_by_name("Nonexistent Player")
        expected_result = []
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
