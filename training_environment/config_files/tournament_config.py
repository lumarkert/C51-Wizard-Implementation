import os


class TournamentConfig:

    def __init__(self, path, name="", num_players="", path_player_1="", path_player_2="", path_player_3="",
                 path_player_4="", path_player_5="", path_player_6="", number_of_games=""):

        if path == "":
            self.name = name
            self.num_players = num_players
            self.path_player_1 = path_player_1
            self.path_player_2 = path_player_2
            self.path_player_3 = path_player_3
            self.path_player_4 = path_player_4
            self.path_player_5 = path_player_5
            self.path_player_6 = path_player_6
            self.number_of_games = number_of_games

        else:
            self.name = None
            self.num_players = None
            self.path_player_1 = None
            self.bid_name_player_1 = None
            self.play_name_player_1 = None
            self.setup_name_player_1 = None
            self.path_player_2 = None
            self.bid_name_player_2 = None
            self.play_name_player_2 = None
            self.setup_name_player_2 = None
            self.path_player_3 = None
            self.bid_name_player_3 = None
            self.play_name_player_3 = None
            self.setup_name_player_3 = None
            self.path_player_4 = None
            self.bid_name_player_4 = None
            self.play_name_player_4 = None
            self.setup_name_player_4 = None
            self.path_player_5 = None
            self.bid_name_player_5 = None
            self.play_name_player_5 = None
            self.setup_name_player_5 = None
            self.path_player_6 = None
            self.bid_name_player_6 = None
            self.play_name_player_6 = None
            self.setup_name_player_6 = None
            self.number_of_games = None
            self.load_config_from_file(path)

        self.list_of_setups = []
        self.list_of_setups.append(
            [self.path_player_1, self.bid_name_player_1, self.play_name_player_1, self.setup_name_player_1])
        self.list_of_setups.append(
            [self.path_player_2, self.bid_name_player_2, self.play_name_player_2, self.setup_name_player_2])
        self.list_of_setups.append(
            [self.path_player_3, self.bid_name_player_3, self.play_name_player_3, self.setup_name_player_3])
        if self.num_players > 3:
            self.list_of_setups.append(
                [self.path_player_4, self.bid_name_player_4, self.play_name_player_4, self.setup_name_player_4])
        if self.num_players > 4:
            self.list_of_setups.append(
                [self.path_player_5, self.bid_name_player_5, self.play_name_player_5, self.setup_name_player_5])
        if self.num_players > 5:
            self.list_of_setups.append(
                [self.path_player_6, self.bid_name_player_6, self.play_name_player_6, self.setup_name_player_6])

    def load_config_from_file(self, file_name):
        current_dir = os.getcwd()
        new_dir = os.path.join(current_dir, "pre_configs/tournament")
        path = os.path.join(new_dir, file_name)
        with open(path, 'r') as f:
            lines = f.read().splitlines()
            self.name = lines[1]
            self.num_players = int(lines[3])
            self.path_player_1 = lines[5]
            self.bid_name_player_1 = lines[7]
            self.play_name_player_1 = lines[9]
            self.setup_name_player_1 = lines[11]
            self.path_player_2 = lines[13]
            self.bid_name_player_2 = lines[15]
            self.play_name_player_2 = lines[17]
            self.setup_name_player_2 = lines[19]
            self.path_player_3 = lines[21]
            self.bid_name_player_3 = lines[23]
            self.play_name_player_3 = lines[25]
            self.setup_name_player_3 = lines[27]
            self.path_player_4 = lines[29]
            self.bid_name_player_4 = lines[31]
            self.play_name_player_4 = lines[33]
            self.setup_name_player_4 = lines[35]
            self.path_player_5 = lines[37]
            self.bid_name_player_5 = lines[39]
            self.play_name_player_5 = lines[41]
            self.setup_name_player_5 = lines[43]
            self.path_player_6 = lines[45]
            self.bid_name_player_6 = lines[47]
            self.play_name_player_6 = lines[49]
            self.setup_name_player_6 = lines[51]
            self.number_of_games = int(lines[53])

    def save_config_to_file(self, path):
        with open(os.path.join(path, f"{self.name}"), 'w') as f:
            f.write(f'Name:\n'
                    f'{self.name}\n'
                    f'Number of Players:\n'
                    f'{self.num_players}\n'
                    f'Path of Player 1:\n'
                    f'{self.path_player_1}\n'
                    f'Bid Config Path of Player 1:\n'
                    f'{self.bid_name_player_1}\n'
                    f'Play Config Path of Player 1:\n'
                    f'{self.play_name_player_1}\n'
                    f'Setup Name of Player 1:\n'
                    f'{self.setup_name_player_1}\n'
                    f'Path of Player 2:\n'
                    f'{self.path_player_2}\n'
                    f'Bid Config Path of Player 2:\n'
                    f'{self.bid_name_player_2}\n'
                    f'Play Config Path of Player 2:\n'
                    f'{self.play_name_player_2}\n'
                    f'Setup Name of Player 2:\n'
                    f'{self.setup_name_player_2}\n'
                    f'Path of Player 3:\n'
                    f'{self.path_player_3}\n'
                    f'Bid Config Path of Player 3:\n'
                    f'{self.bid_name_player_3}\n'
                    f'Play Config Path of Player 3:\n'
                    f'{self.play_name_player_3}\n'
                    f'Setup Name of Player 3:\n'
                    f'{self.setup_name_player_3}\n'
                    f'Path of Player 4:\n'
                    f'{self.path_player_4}\n'
                    f'Bid Config Path of Player 4:\n'
                    f'{self.bid_name_player_4}\n'
                    f'Play Config Path of Player 4:\n'
                    f'{self.play_name_player_4}\n'
                    f'Setup Name of Player 4:\n'
                    f'{self.setup_name_player_4}\n'
                    f'Path of Player 5:\n'
                    f'{self.path_player_5}\n'
                    f'Bid Config Path of Player 5:\n'
                    f'{self.bid_name_player_5}\n'
                    f'Play Config Path of Player 5:\n'
                    f'{self.play_name_player_5}\n'
                    f'Setup Name of Player 5:\n'
                    f'{self.setup_name_player_5}\n'
                    f'Path of Player 6:\n'
                    f'{self.path_player_6}\n'
                    f'Bid Config Path of Player 6:\n'
                    f'{self.bid_name_player_6}\n'
                    f'Play Config Path of Player 6:\n'
                    f'{self.play_name_player_6}\n'
                    f'Setup Name of Player 6:\n'
                    f'{self.setup_name_player_6}\n'
                    f'Number of Games:\n'
                    f'{self.number_of_games}\n'
                    )
        return
