import unittest
from unittest.mock import MagicMock

from app.models.game_stats import GameStats
from app.services.player_stats_service import PlayerStatsService
from app.api.core.models.Advanced import Advanced
from app.api.core.models.FreeThrows import FreeThrows
from app.api.core.models.PlayerStats import PlayerStats
from app.api.core.models.ThreePoints import ThreePoints
from app.api.core.models.Traditional import Traditional
from app.api.core.models.TwoPoints import TwoPoints

class TestPlayerStatsService(unittest.TestCase):
    def setUp(self):
        self.player_repository = MagicMock()

        self.sample_game_stats = [
            GameStats("John Doe", "PG", 6, 6, 0, 4, 4, 4, 1, 1, 4, 2, 2),
            GameStats("John Doe", "PG", 5, 5, 1, 3, 2, 2, 0, 0, 3, 1, 0),
        ]

        # Configure the mock to return the sample game stats
        self.player_repository.get_player_stats_by_name.return_value = self.sample_game_stats

        # Create PlayerStatsService instance with the mocked repository
        self.player_stats_service = PlayerStatsService(self.player_repository)

    def test_calculate_player_stats(self):
        result = self.player_stats_service.calculate_player_stats("John Doe")

        expected_result = PlayerStats(
            playerName="John Doe",
            gamesPlayed=len(self.sample_game_stats),
            traditional=Traditional(
                freeThrows=FreeThrows(attempts=5.5, made=5.5, shootingPercentage=100.0),
                twoPoints=TwoPoints(attempts=3.5, made=0.5, shootingPercentage=14.3),
                threePoints=ThreePoints(attempts=3.0, made=3.0, shootingPercentage=100.0),
                points=15.5,
                rebounds=0.5,
                blocks=0.5,
                assists=3.5,
                steals=1.5,
                turnovers=1.0
            ),
            advanced=Advanced(
                valorization=35.0,
                effectiveFieldGoalPercentage=76.9,
                trueShootingPercentage=85.0,
                hollingerAssistRatio=25.7
            )
        )

        # Assert that the result matches the expected result
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()