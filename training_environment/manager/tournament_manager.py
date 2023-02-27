import os.path

from training_environment.agent_wrappers.c51_bidding_wrapper import C51BiddingWrapper
from training_environment.agent_wrappers.c51_playing_wrapper import C51PlayingWrapper
from training_environment.config_files.c51_config import C51Config
from training_environment.config_files.game_config import GameConfig
from training_environment.config_files.tournament_config import TournamentConfig
from training_environment.players.rl_player_bidding_playing import RLPlayerBiddingPlaying
from training_environment.tf_environments.tf_wizard_bidding_env import TFWizardBiddingEnv
from training_environment.tf_environments.tf_wizard_play_env import TFWizardPlayEnv


class TournamentManager:
    def __init__(self, game_config: GameConfig, tournament_config: TournamentConfig, directory):
        self.tournament_config = tournament_config
        self.directory = directory

        self.game_config = game_config

        self.players = []
        self.wrapper_list = []

        self.setup_tournament_agents()

    def setup_tournament_agents(self):
        for player_setup in self.tournament_config.list_of_setups:
            player = self.setup_tournament_player(player_setup[3])
            self.setup_c51_bidding(player, player_setup)
            self.setup_c51_playing(player, player_setup)

    def setup_tournament_player(self, player_name):
        player = RLPlayerBiddingPlaying(player_name, self.directory)
        self.players.append(player)
        return player

    def setup_c51_bidding(self, player, player_setup):
        bid_path = os.path.join(os.getcwd(), player_setup[0], player_setup[1])
        bid_config = C51Config(bid_path)
        #bid_model_path = os.path.join(player_setup[0], "wrappers/MultiAgent_BidPlay_1_Bidding/checkpoint")
        bid_model_path = os.path.join(player_setup[0], "bid/checkpoint")
        train_bidding_py_env = TFWizardBiddingEnv(self.game_config, bid_config, player)
        eval_bidding_py_env = TFWizardBiddingEnv(self.game_config, bid_config, player)

        c51_bidding_wrapper = C51BiddingWrapper(player.name, train_bidding_py_env, eval_bidding_py_env, bid_config,
                                                self.game_config, "SingleAgent", self.directory, "True", bid_model_path)

        player.set_bidding_wrapper(c51_bidding_wrapper)
        self.wrapper_list.append(player.bidding_wrapper)

    def setup_c51_playing(self, player, player_setup):
        play_path = os.path.join(os.getcwd(), player_setup[0], player_setup[2])
        play_config = C51Config(play_path)
        #play_model_path = os.path.join(player_setup[0], "wrappers/MultiAgent_BidPlay_1_Bidding/checkpoint")
        play_model_path = os.path.join(player_setup[0], "play/checkpoint")
        train_playing_py_env = TFWizardPlayEnv(self.game_config, play_config, player)
        eval_playing_py_env = TFWizardPlayEnv(self.game_config, play_config, player)

        c51_playing_wrapper = C51PlayingWrapper(player.name, train_playing_py_env, eval_playing_py_env,
                                                play_config, self.game_config, "SingleAgent", self.directory, "True",
                                                play_model_path)

        player.set_playing_wrapper(c51_playing_wrapper)
        self.wrapper_list.append(player.playing_wrapper)
