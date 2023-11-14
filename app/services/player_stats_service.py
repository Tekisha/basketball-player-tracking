# app/services/player_stats_service.py
from app.api.core.models.Advanced import Advanced
from app.api.core.models.FreeThrows import FreeThrows
from app.api.core.models.PlayerStats import PlayerStats
from app.api.core.models.ThreePoints import ThreePoints
from app.api.core.models.Traditional import Traditional
from app.api.core.models.TwoPoints import TwoPoints


class PlayerStatsService:

    def __init__(self, player_repository):
        self.player_repository = player_repository

    def calculate_player_stats(self,player_full_name):
        player_stats_list = self.player_repository.get_player_stats_by_name(player_full_name)

        if not player_stats_list:
            return None

        total_ftm = 0
        total_fta = 0
        total_2pm = 0
        total_2pa = 0
        total_3pm = 0
        total_3pa = 0
        total_reb = 0
        total_blk = 0
        total_ast = 0
        total_stl = 0
        total_tov = 0

        for game_stats in player_stats_list:
            total_ftm += game_stats.ftm
            total_fta += game_stats.fta
            total_2pm += game_stats.two_pm
            total_2pa += game_stats.two_pa
            total_3pm += game_stats.three_pm
            total_3pa += game_stats.three_pa
            total_reb += game_stats.reb
            total_blk += game_stats.blk
            total_ast += game_stats.ast
            total_stl += game_stats.stl
            total_tov += game_stats.tov

        ft_percentage = (total_ftm / total_fta) * 100 if total_fta > 0 else 0
        two_points_percentage = (total_2pm / total_2pa) * 100 if total_2pa > 0 else 0
        three_points_percentage = (total_3pm / total_3pa) * 100 if total_3pa > 0 else 0
        points = total_ftm + 2 * total_2pm + 3 * total_3pm
        valorization = (total_ftm + 2 * total_2pm + 3 * total_3pm + total_reb + total_blk + total_ast + total_stl) - \
                       (total_fta - total_ftm + total_2pa - total_2pm + total_3pa - total_3pm + total_tov)
        effective_field_goal_percentage = ((total_2pm + total_3pm + 0.5 * total_3pm) / (total_2pa + total_3pa)) * 100 \
            if total_2pa + total_3pa > 0 else 0
        true_shooting_percentage = (points / (2 * (total_2pa + total_3pa + 0.475 * total_fta))) * 100 \
            if total_2pa + total_3pa + 0.475 * total_fta > 0 else 0
        hollinger_assist_ratio = (total_ast / (total_2pa + total_3pa + 0.475 * total_fta + total_ast + total_tov)) * 100 \
            if total_2pa + total_3pa + 0.475 * total_fta + total_ast + total_tov > 0 else 0

        games_played = len(player_stats_list)

        traditional_stats = Traditional(
            freeThrows=FreeThrows(attempts=round(total_fta/games_played, 1), made=round(total_ftm/games_played, 1), shootingPercentage=round(ft_percentage, 1)),
            twoPoints=TwoPoints(attempts=round(total_2pa/games_played, 1), made=round(total_2pm/games_played, 1), shootingPercentage=round(two_points_percentage, 1)),
            threePoints=ThreePoints(attempts=round(total_3pa/games_played, 1), made=round(total_3pm/games_played, 1), shootingPercentage=round(three_points_percentage, 1)),
            points=round(points/games_played, 1),
            rebounds=round(total_reb/games_played, 1),
            blocks=round(total_blk/games_played, 1),
            assists=round(total_ast/games_played, 1),
            steals=round(total_stl/games_played, 1),
            turnovers=round(total_tov/games_played, 1)
        )

        advanced_stats = Advanced(
            valorization=round(valorization, 1),
            effectiveFieldGoalPercentage=round(effective_field_goal_percentage, 1),
            trueShootingPercentage=round(true_shooting_percentage, 1),
            hollingerAssistRatio=round(hollinger_assist_ratio, 1)
        )

        return PlayerStats(
            playerName=player_full_name,
            gamesPlayed=games_played,
            traditional=traditional_stats,
            advanced=advanced_stats
        )
