from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from training_environment.manager import save_manager
from training_environment.game_real_evaluation.real_evaluation_game import RealEvaluationGame
from training_environment.game_real_evaluation.real_evaluation_real_player import RealEvaluationRealPlayer
from training_environment.manager.player_manager import PlayerManager
from training_environment.config_files.training_setup import TrainingSetup


class EvaluationWrapper:
    def __init__(self, training_setup: TrainingSetup):
        self.directory = save_manager.determine_save_file_path(training_setup.name)

        self.training_config = training_setup.training_config
        self.training_setup = training_setup
        self.game_config = training_setup.game_config
        self.player_manager = PlayerManager(training_setup, self.directory)
        self.training_wrappers = self.player_manager.training_wrappers

        self.player = self.player_manager.player
        self.players = [self.player]

    def start_evaluation(self):

        self.setup_real_game(self.training_wrappers)
        for wrapper in self.training_wrappers:
            wrapper.total_rewards.append(wrapper.rewards)
            wrapper.save_return_of_episode()
            wrapper.reset_rewards()
        self.collect_data_from_evaluation_phase(self.training_wrappers)
        self.calculate_stats_per_round_for_players()

        save_manager.save_files_after_tournament(self.directory, self.players)

    def setup_real_game(self, wrapper_list):
        print("-------------------------")
        print(f"Test Spiel BSW")
        for wrapper in wrapper_list:
            wrapper.set_train_phase(False)
            wrapper.set_agent_policy()
        for i in range(self.game_config.num_players - 1):
            name = input(f"Enter the Name of Player Number {i+1}")
            print(name)
            self.players.append(RealEvaluationRealPlayer(name, self.directory))
        self.start_real_game(self.players)

    def collect_data_from_evaluation_phase(self, wrapper_list, step):
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

    def calculate_average_reward_and_return_for_wrappers(self, wrapper_list, step):
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

            print(f'{wrapper.name}:  step = {step}: Average Return = {avg_return}')
            if len(wrapper.total_avg_returns) > 1:
                last_avg_return = wrapper.total_avg_returns[-2]
                print(f'Change from last Evaluation Phase: {avg_return - last_avg_return}')

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

    def start_real_game(self, players):
        game = RealEvaluationGame(players,
                                  self.game_config)
        game.start_game()
