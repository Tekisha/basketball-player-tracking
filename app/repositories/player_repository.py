
class PlayerRepository:
    def __init__(self, game_state_list):
        self.game_stats_list = game_state_list

    def get_player_stats_by_name(self, player_full_name: str):
        player_stats = [game_stats for game_stats in self.game_stats_list if game_stats.player.lower() == player_full_name.lower()]

        return player_stats
