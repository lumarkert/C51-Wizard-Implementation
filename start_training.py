from training_environment.evaluation_wrapper import EvaluationWrapper
from training_environment.config_files.tournament_config import TournamentConfig
from training_environment.tournament_wrapper import TournamentWrapper
from training_environment.config_files.training_setup import TrainingSetup
from training_environment.training_wrapper import TrainingWrapper


def start_training_wrapper(training_setup_name):
    tw = TrainingWrapper(TrainingSetup(training_setup_name))
    tw.start_training()

def start_tournament_wrapper(tournament_config_name, game_config_name):
    tw = TournamentWrapper(TournamentConfig(tournament_config_name), game_config_name)
    tw.start_tournament()

def start_evaluation_wrapper(training_setup_name):
    ew = EvaluationWrapper(TrainingSetup(training_setup_name))
    ew.start_evaluation()





