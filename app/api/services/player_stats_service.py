# app/services/player_stats_service.py

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

        for player_stats in player_stats_list:
            total_ftm += player_stats[2]
            total_fta += player_stats[3]
            total_2pm += player_stats[4]
            total_2pa += player_stats[5]
            total_3pm += player_stats[6]
            total_3pa += player_stats[7]
            total_reb += player_stats[8]
            total_blk += player_stats[9]
            total_ast += player_stats[10]
            total_stl += player_stats[11]
            total_tov += player_stats[12]

