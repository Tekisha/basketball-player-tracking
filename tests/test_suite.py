import unittest

from utils.test_csv_parser import TestCsvParser
from repositories.test_player_repository import TestPlayerRepository
from services.test_player_stats_service import TestPlayerStatsService

csv_parser_test_case = unittest.TestLoader().loadTestsFromTestCase(TestCsvParser)
player_repository_test_case = unittest.TestLoader().loadTestsFromTestCase(TestPlayerRepository)
player_stats_service_test_case = unittest.TestLoader().loadTestsFromTestCase(TestPlayerStatsService)

test_suite = unittest.TestSuite([
    csv_parser_test_case,
    player_repository_test_case,
    player_stats_service_test_case,
])

unittest.TextTestRunner().run(test_suite)