import csv
from app.models.game_stats import GameStats

class CsvParser:
    @staticmethod
    def parse_csv(csv_file_path):
        game_stats_list = []

        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                game_stats = GameStats(
                    row['PLAYER'],
                    row['POSITION'],
                    row['FTM'],
                    row['FTA'],
                    row['2PM'],
                    row['2PA'],
                    row['3PM'],
                    row['3PA'],
                    row['REB'],
                    row['BLK'],
                    row['AST'],
                    row['STL'],
                    row['TOV']
                )
                game_stats_list.append(game_stats)

        return game_stats_list
