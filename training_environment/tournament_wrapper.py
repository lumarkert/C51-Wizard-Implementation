from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys

import numpy as np
import time as t

from training_environment.manager import save_manager
from training_environment.config_files.game_config import GameConfig
from training_environment.config_files.tournament_config import TournamentConfig
from training_environment.game_environment.game import Game
from training_environment.manager.tournament_manager import TournamentManager


class TournamentWrapper:
    def __init__(self, tournament_config: TournamentConfig, game_config_path):

        self.tournament_config = tournament_config
        self.game_config = GameConfig(game_config_path)
        self.directory = save_manager.determine_save_file_path(self.tournament_config.name)

        self.tournament_manager = TournamentManager(self.game_config, self.tournament_config, self.directory)
        self.wrapper_list = self.tournament_manager.wrapper_list
        self.players = self.tournament_manager.players

    def start_tournament(self):
        self.collect_steps_for_evaluation(self.wrapper_list, self.tournament_config.number_of_games)
        self.collect_data_from_evaluation_phase(self.wrapper_list)
        self.calculate_stats_per_round_for_players()

        save_manager.save_files_after_tournament(self.directory, self.players)


    def collect_data_from_evaluation_phase(self, wrapper_list):
        self.calculate_average_points_for_players()
        self.calculate_avg_accuracy_for_players()
        self.calculate_winrate_for_players()

    def calculate_average_points_for_players(self):
        for player in self.players:
            player.avg_points.append(sum(player.history_scores) / len(player.history_scores))

    def calculate_avg_accuracy_for_players(self):
        for player in self.players:
            player.calculate_average_accuracies()

    def calculate_winrate_for_players(self):
        total_games = 0
        for player in self.players:
            total_games += player.games_won

        for player in self.players:
            player.winrates.append(player.calculate_win_rate(total_games))

    def calculate_average_reward_and_return_for_wrappers(self, wrapper_list):
        for wrapper in wrapper_list:
            avg_reward_list = []
            for reward_list in wrapper.total_rewards:
                avg_reward_list.append(self.calculate_average_reward(reward_list))
            avg_reward = self.calculate_average_reward(avg_reward_list)
            wrapper.total_avg_rewards.append(avg_reward)
            wrapper.total_rewards = []

            avg_return = sum(wrapper.total_returns)/len(wrapper.total_returns)
            wrapper.total_avg_returns.append(avg_return)
            wrapper.total_returns = []

    def calculate_stats_per_round_for_players(self):
        for player in self.players:
            player.calculate_stats_per_round(self.game_config.number_of_total_rounds)

    def reset_win_stats(self):
        for player in self.players:
            player.reset_evaluation_stats()

    @staticmethod
    def calculate_average_reward(reward_array):
        avg_reward = 0
        for reward in reward_array:
            avg_reward += np.average(reward)
        avg_reward = avg_reward / len(reward_array)
        return avg_reward

    def collect_steps_for_evaluation(self, wrapper_list, number_of_games):
        print("-------------------------")
        print(f"Starting Tournament")
        for wrapper in wrapper_list:
            wrapper.set_train_phase(False)
            wrapper.set_agent_policy()

        self.reset_win_stats()
        for x in range(number_of_games):
            lap_start_time = t.time()
            sys.stdout = open(os.devnull, 'w')
            winner = self.start_game()
            sys.stdout = sys.__stdout__
            lap_end_time = t.time()
            remaining_games = number_of_games-(x+1)
            time_for_lap = lap_end_time-lap_start_time
            remaining_time = time_for_lap * remaining_games
            print(f"Game {x+1} finished.")
            print(f"Winner is {winner.name}")

            won_games_string = "Total Won Games:"
            for player in self.players:
                won_games_string += f" {player.name}: {player.games_won} |"
            print(won_games_string)
            print(f"Remaining Time: {save_manager.convert_seconds(remaining_time)}")
            for wrapper in wrapper_list:
                wrapper.total_rewards.append(wrapper.rewards)
                wrapper.save_return_of_episode()
                wrapper.reset_rewards()
        sys.stdout = sys.__stdout__
        print("Finished collecting Steps for Evaluation")

    def start_game(self):
        game = Game(self.players,
                    self.game_config)
        return game.start_game()

    def start_bsw_game(self, players):
        game = BrettspielweltGame(players,
                                  self.game_config)
        game.start_game()
