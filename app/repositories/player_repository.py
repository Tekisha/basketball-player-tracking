
class PlayerRepository:
    def __init__(self, game_state_list):
        self.game_stats_list = game_state_list

    def get_player_by_name(self, playerFullName: str):
        player_stats = [game_stats for game_stats in self.game_stats_list if game_stats.player.lower() == playerFullName.lower()]

        return player_stats
