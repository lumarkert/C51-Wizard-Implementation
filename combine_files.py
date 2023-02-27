import csv
import os
import shutil


def combine_training(test_folder, target_path, step):
    #combine_avg_returns(test_folder, target_path, step)
    #combine_avg_rewards(test_folder, target_path, step)
    #move_train_loss(test_folder, target_path, step)
    combine_avg_score(test_folder, target_path, step)
    combine_avg_accuracy(test_folder, target_path, step)

def combine_avg_score(test_folder, target_path, step):
    current_dir = os.getcwd()

    target_dir = os.path.join(current_dir, target_path)

    test_dir = os.path.join(current_dir, test_folder)
    players_dir = os.path.join(test_dir, "players")

    avg_scores = []
    for x in range(21):
        avg_scores.append([])

    for player_idx in range(4):
        player_name = f"MultiAgent_BidPlay_{player_idx + 1}"
        player_data_path = os.path.join(player_name, "data")
        player_data_dir = os.path.join(players_dir, player_data_path)

        csv_file_name = f"avg_points_csv_{player_name}.csv"
        csv_file_path = os.path.join(player_data_dir, csv_file_name)

        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for idx, row in enumerate(reader):
                if idx != 0:
                    avg_scores[idx - 1].append(row[1])

    with open(os.path.join(target_dir, f'playerdata/avg_scores_over_training_{step}.csv'), 'w',
              newline='') as f:
        write = csv.writer(f)
        write.writerows(avg_scores)

def combine_avg_accuracy(test_folder, target_path, step):
    current_dir = os.getcwd()

    target_dir = os.path.join(current_dir, target_path)

    test_dir = os.path.join(current_dir, test_folder)
    players_dir = os.path.join(test_dir, "players")

    avg_accuracy = []
    for x in range(21):
        avg_accuracy.append([])

    for player_idx in range(4):
        player_name = f"MultiAgent_BidPlay_{player_idx + 1}"
        player_data_path = os.path.join(player_name, "data")
        player_data_dir = os.path.join(players_dir, player_data_path)

        csv_file_name = f"avg_accuracy_csv_{player_name}.csv"
        csv_file_path = os.path.join(player_data_dir, csv_file_name)

        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for idx, row in enumerate(reader):
                if idx != 0:
                    avg_accuracy[idx - 1].append(row[1])

    with open(os.path.join(target_dir, f'playerdata/avg_accuracies_over_training_{step}.csv'), 'w',
              newline='') as f:
        write = csv.writer(f)
        write.writerows(avg_accuracy)


def move_train_loss(test_folder, target_path, step):
    current_dir = os.getcwd()

    target_dir = os.path.join(current_dir, target_path)

    test_dir = os.path.join(current_dir, test_folder)
    wrappers_dir = os.path.join(test_dir, "wrappers")

    wrapper_name = f"MultiAgent_BidPlay_1_Bidding"
    wrapper_data_path = os.path.join(wrapper_name, "data")
    wrapper_data_dir = os.path.join(wrappers_dir, wrapper_data_path)

    current_file_name = "train_loss_csv_MultiAgent_BidPlay_1_Bidding.csv"
    current_file_path = os.path.join(wrapper_data_dir, current_file_name)
    moved_file_name = f"wrapperdata/train_loss_{step}_Bidding.csv"
    moved_file_path = os.path.join(target_dir, moved_file_name)

    shutil.copyfile(current_file_path, moved_file_path)

    wrapper_name = f"MultiAgent_BidPlay_1_Playing"
    wrapper_data_path = os.path.join(wrapper_name, "data")
    wrapper_data_dir = os.path.join(wrappers_dir, wrapper_data_path)

    current_file_name = "train_loss_csv_MultiAgent_BidPlay_1_Playing.csv"
    current_file_path = os.path.join(wrapper_data_dir, current_file_name)
    moved_file_name = f"wrapperdata/train_loss_{step}_Playing.csv"
    moved_file_path = os.path.join(target_dir, moved_file_name)

    shutil.copyfile(current_file_path, moved_file_path)



def combine_avg_returns(test_folder, target_path, step):
    current_dir = os.getcwd()

    target_dir = os.path.join(current_dir, target_path)

    test_dir = os.path.join(current_dir, test_folder)
    wrappers_dir = os.path.join(test_dir, "wrappers")

    avg_returns = []
    for x in range(21):
        avg_returns.append([])

    for wrapper_idx in range(4):
        wrapper_name = f"MultiAgent_BidPlay_{wrapper_idx+1}_Bidding"
        wrapper_data_path = os.path.join(wrapper_name, "data")
        wrapper_data_dir = os.path.join(wrappers_dir, wrapper_data_path)

        csv_file_name = f"avg_returns_csv_{wrapper_name}.csv"
        csv_file_path = os.path.join(wrapper_data_dir, csv_file_name)


        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for idx, row in enumerate(reader):
                if idx != 0:
                    avg_returns[idx-1].append(row[1])

    with open(os.path.join(target_dir, f'wrapperdata/avg_returns_{step}.csv'), 'w',
              newline='') as f:
        write = csv.writer(f)
        write.writerows(avg_returns)

def combine_avg_rewards(test_folder, target_path, step):
    current_dir = os.getcwd()

    target_dir = os.path.join(current_dir, target_path)

    test_dir = os.path.join(current_dir, test_folder)
    wrappers_dir = os.path.join(test_dir, "wrappers")

    avg_returns = []
    for x in range(21):
        avg_returns.append([])

    for wrapper_idx in range(4):
        wrapper_name = f"MultiAgent_BidPlay_{wrapper_idx+1}_Bidding"
        wrapper_data_path = os.path.join(wrapper_name, "data")
        wrapper_data_dir = os.path.join(wrappers_dir, wrapper_data_path)

        csv_file_name = f"avg_rewards_csv_{wrapper_name}.csv"
        csv_file_path = os.path.join(wrapper_data_dir, csv_file_name)


        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for idx, row in enumerate(reader):
                if idx != 0:
                    avg_returns[idx-1].append(row[1])

    with open(os.path.join(target_dir, f'wrapperdata/avg_rewards_{step}.csv'), 'w',
              newline='') as f:
        write = csv.writer(f)
        write.writerows(avg_returns)

def combine_tournament_against_each_other(tournament_path, target_path, step):
    move_avg_points(tournament_path, target_path, step)
    move_avg_accuracy(tournament_path, target_path, step)

def combine_tournament_all_same(tournament_path, target_path, step):
    combine_guessed_tricks(tournament_path, target_path, step)
    combine_won_tricks(tournament_path, target_path, step)
    move_avg_accuracy(tournament_path, target_path, step)
    combine_avg_accuracy_per_round(tournament_path, target_path, step)
    move_avg_points(tournament_path, target_path, step)
    combine_avg_points_per_round(tournament_path, target_path, step)
    combine_box_plot_points(tournament_path, target_path, step)

def move_avg_points(tournament_path, target_path, step):
    current_dir = os.getcwd()

    target_dir = os.path.join(current_dir, target_path)

    tournament_dir = os.path.join(current_dir, tournament_path)

    avg_accuracy = None
    for file in os.listdir(tournament_dir):
        if file.startswith("avg_points_csv"):
            avg_accuracy = file

    current_file_path = os.path.join(tournament_dir, avg_accuracy)
    moved_file_name = f"playerdata/avg_points_tournament_{step}.csv"
    moved_file_path = os.path.join(target_dir, moved_file_name)

    shutil.copyfile(current_file_path, moved_file_path)

def move_avg_accuracy(tournament_path, target_path, step):
    current_dir = os.getcwd()

    target_dir = os.path.join(current_dir, target_path)

    tournament_dir = os.path.join(current_dir, tournament_path)

    avg_accuracy = None
    for file in os.listdir(tournament_dir):
        if file.startswith("avg_accuracy_csv"):
            avg_accuracy = file

    current_file_path = os.path.join(tournament_dir, avg_accuracy)
    moved_file_name = f"playerdata/avg_accuracy_tournament_{step}.csv"
    moved_file_path = os.path.join(target_dir, moved_file_name)

    shutil.copyfile(current_file_path, moved_file_path)

def combine_avg_accuracy_per_round(path, target_path, step):
    current_dir = os.getcwd()
    csv_dir = os.path.join(current_dir, path)
    target_dir = os.path.join(current_dir, target_path)

    avg_accuracy_files = []
    for file in os.listdir(csv_dir):
        if file.startswith("avg_accuracy_per_round_csv"):
            avg_accuracy_files.append(str(file))

    avg_accuracies = []
    for x in range(15):
        avg_accuracies.append([])

    for file in avg_accuracy_files:
        csv_file_path = os.path.join(csv_dir, file)
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for idx, row in enumerate(reader):
                avg_accuracies[idx].append(row[0])

    with open(os.path.join(target_dir, f'playerdata/avg_accuracy_per_round_{step}.csv'), 'w',
              newline='') as f:
        write = csv.writer(f)
        write.writerows(avg_accuracies)

def combine_avg_points_per_round(path, target_path, step):
    current_dir = os.getcwd()
    csv_dir = os.path.join(current_dir, path)
    target_dir = os.path.join(current_dir, target_path)

    avg_points_files = []
    for file in os.listdir(csv_dir):
        if file.startswith("avg_points_per_round_csv"):
            avg_points_files.append(str(file))

    avg_points = []
    for x in range(15):
        avg_points.append([])

    for file in avg_points_files:
        csv_file_path = os.path.join(csv_dir, file)
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for idx, row in enumerate(reader):
                avg_points[idx].append(row[0])

    with open(os.path.join(target_dir, f'playerdata/avg_points_per_round_{step}.csv'), 'w',
              newline='') as f:
        write = csv.writer(f)
        write.writerows(avg_points)

def combine_guessed_tricks(path, target_path, step):
    current_dir = os.getcwd()
    csv_dir = os.path.join(current_dir, path)
    target_dir = os.path.join(current_dir, target_path)

    guessed_tricks_files = []
    for file in os.listdir(csv_dir):
        if file.startswith("guessed_tricks_csv"):
            guessed_tricks_files.append(str(file))

    guessed_tricks = []
    for x in range(15):
        guessed_tricks.append([])

    for file in guessed_tricks_files:
        csv_file_path = os.path.join(csv_dir, file)
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for idx, row in enumerate(reader):
                for column in row:
                    guessed_tricks[idx].append(column)

    with open(os.path.join(target_dir, f'playerdata/guessed_tricks_{step}.csv'), 'w',
              newline='') as f:
        write = csv.writer(f)
        write.writerows(guessed_tricks)

def combine_won_tricks(path, target_path, step):
    current_dir = os.getcwd()
    csv_dir = os.path.join(current_dir, path)
    target_dir = os.path.join(current_dir, target_path)

    won_tricks_files = []
    for file in os.listdir(csv_dir):
        if file.startswith("won_tricks_per_round"):
            won_tricks_files.append(str(file))

    won_tricks = []
    for x in range(15):
        won_tricks.append([])

    for file in won_tricks_files:
        csv_file_path = os.path.join(csv_dir, file)
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for idx, row in enumerate(reader):
                for column in row:
                    won_tricks[idx].append(column)

    with open(os.path.join(target_dir, f'playerdata/won_tricks_{step}.csv'), 'w',
              newline='') as f:
        write = csv.writer(f)
        write.writerows(won_tricks)

def combine_box_plot_points(path, target_path, step):
    current_dir = os.getcwd()
    csv_dir = os.path.join(current_dir, path)
    target_dir = os.path.join(current_dir, target_path)

    boxplot_points_files = []
    for file in os.listdir(csv_dir):
        if file.startswith("boxplot_points_csv"):
            boxplot_points_files.append(str(file))

    boxplot_points = []
    for x in range(15):
        boxplot_points.append([])

    for file in boxplot_points_files:
        csv_file_path = os.path.join(csv_dir, file)
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for idx, row in enumerate(reader):
                for column in row:
                    boxplot_points[idx].append(column)

    with open(os.path.join(target_dir, f'playerdata/boxplot_points_{step}.csv'), 'w',
              newline='') as f:
        write = csv.writer(f)
        write.writerows(boxplot_points)


combine_tournament_against_each_other("tests/Evaluierung/Against Each Other/tournament", "tests/Auswahl/A Final Run", "all")
#combine_tournament_all_same("Tests/Auswahl/A Final Run/Tournament/All 40k/tournament", "Tests/Auswahl/A Final Run", 40000)
#combine_training("Tests/Auswahl/A Final Run/Training/Final 4 Players 0-20", "Tests/Auswahl/A Final Run", 20000)
