from training_environment.evaluation_wrapper import EvaluationWrapper
from training_environment.config_files.tournament_config import TournamentConfig
from training_environment.tournament_wrapper import TournamentWrapper
from training_environment.config_files.training_setup import TrainingSetup
from training_environment.training_wrapper import TrainingWrapper
import sys

def start_training_wrapper(training_setup_name):
    tw = TrainingWrapper(TrainingSetup(training_setup_name))
    tw.start_training()

def start_tournament_wrapper(tournament_config_name, game_config_name):
    tw = TournamentWrapper(TournamentConfig(tournament_config_name), game_config_name)
    tw.start_tournament()


if len(sys.argv) == 1:
    print("Please specify which mode should be started.")

elif sys.argv[1] == "training":
    if sys.argv == 2:
        print("Training mode was select but no training_setup was given. Please specify the name of the training_setup file.")
    else:
        start_training_wrapper(sys.argv[2])

elif sys.argv[1] == "tournament":
    if sys.argv == 2:
        print("Tournament mode was select but no tournament_config was given. Please specify the name of the tournament_config file.")
    elif sys.argv == 3:
        print("Tournament mode was select but no game_config was given. Please specify the name of the game_config file.")
    else:
        start_training_wrapper(sys.argv[2], sys.argv[3])



