import csv
import unittest
from app.models.game_stats import GameStats
from app.utils.csv_parser import CsvParser

class TestCsvParser(unittest.TestCase):
    def setUp(self):
        self.csv_file_path = 'test_data.csv'
        with open(self.csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['PLAYER', 'POSITION', 'FTM', 'FTA', '2PM', '2PA', '3PM', '3PA', 'REB', 'BLK', 'AST', 'STL', 'TOV'])
            csv_writer.writerow(['John Doe', 'PG', '6', '6', '0', '4', '4', '4', '1', '1', '4', '2', '2'])
            csv_writer.writerow(['Jane Doe', 'SG', '2', '3', '1', '5', '0', '2', '7', '1', '1', '0', '1'])

    def tearDown(self):
        # Remove the sample CSV file after testing
        import os
        os.remove(self.csv_file_path)

    def test_parse_csv(self):
        game_stats_list = CsvParser.parse_csv(self.csv_file_path)

        expected_result = [
            GameStats('John Doe', 'PG', 6, 6, 0, 4, 4, 4, 1, 1, 4, 2, 2),
            GameStats('Jane Doe', 'SG', 2, 3, 1, 5, 0, 2, 7, 1, 1, 0, 1),
        ]

        for result_game_stats, expected_game_stats in zip(game_stats_list, expected_result):
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

if __name__ == '__main__':
    unittest.main()