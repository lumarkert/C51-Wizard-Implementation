import csv
import os
import numpy as np

from matplotlib import pyplot as plt
from matplotlib.markers import TICKLEFT, TICKRIGHT


def plot_train_loss(path):
    current_dir = os.getcwd()
    csv_dir = os.path.join(current_dir, path)
    csv_steps = [20000, 40000, 60000, 80000]

    steps = []
    train_loss_bid = []
    offset = 0
    for step_idx, step in enumerate(csv_steps):
        if step_idx > 0:
            offset = csv_steps[step_idx - 1]
        csv_file_path = os.path.join(csv_dir, f"wrapperdata/train_loss_{step}_Bidding.csv")
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for idx, row in enumerate(reader):
                if idx != 0 and idx != 21:
                    train_loss_bid.append(float(row[1]))
                    steps.append(int(row[0]) + offset)

                if idx == 21 and step == csv_steps[-1]:
                    train_loss_bid.append(float(row[1]))
                    steps.append(int(row[0]) + offset)

    train_loss_play = []
    for step_idx, step in enumerate(csv_steps):
        csv_file_path = os.path.join(csv_dir, f"wrapperdata/train_loss_{step}_Playing.csv")
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for idx, row in enumerate(reader):
                if idx != 0 and idx != 21:
                    train_loss_play.append(float(row[1]))

                if idx == 21 and step == csv_steps[-1]:
                    train_loss_play.append(float(row[1]))

    plt.plot(steps, train_loss_play, color="r", label="Ausspiel-Agent")
    plt.plot(steps, train_loss_bid, color="b", label="Ansagen-Agent")
    plt.grid()
    plt.xlabel('Trainingsiteration')
    plt.ylim(top=4.0, bottom=1.0)
    plt.xticks(range(0, 100000, 20000))
    plt.legend()
    plt.ylabel('Verlust')
    file_name = f'train_loss.png'
    plt.savefig(os.path.join(csv_dir, file_name))
    plt.clf()


def plot_returns(path):
    current_dir = os.getcwd()
    csv_dir = os.path.join(current_dir, path)
    csv_steps = [20000, 40000, 60000, 80000]

    avg_returns = []
    for step_idx, step in enumerate(csv_steps):
        csv_file_path = os.path.join(csv_dir, f"wrapperdata/avg_returns_{step}.csv")
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for idx, row in enumerate(reader):
                if idx != 20:
                    avg_return_combined = 0.0
                    for column in row:
                        avg_return_combined += float(column)
                    avg_return_combined = avg_return_combined / len(row)
                    avg_returns.append(avg_return_combined)

                if idx == 20 and step_idx == len(csv_steps) - 1:
                    avg_return_combined = 0.0
                    for column in row:
                        avg_return_combined += float(column)
                    avg_return_combined = avg_return_combined / len(row)
                    avg_returns.append(avg_return_combined)

    steps = range(0, 81000, 1000)
    plt.plot(steps, avg_returns)
    plt.grid()
    plt.xlabel('Trainingsiteration')
    plt.xticks(range(0, 100000, 20000))

    plt.ylabel('Durchschnittlicher Gewinn über 100 Spiele')
    plt.ylim(bottom=-100)
    file_name = f'average_returns_over_training_part_view.png'
    plt.savefig(os.path.join(csv_dir, file_name))
    plt.clf()

    plt.plot(steps, avg_returns)
    plt.grid()
    plt.xlabel('Trainingsiteration')
    plt.xticks(range(0, 100000, 20000))

    plt.ylabel('Durchschnittlicher Gewinn über 100 Spiele')
    file_name = f'average_returns_over_training_full_view.png'
    plt.savefig(os.path.join(csv_dir, file_name))
    plt.clf()

def plot_accuracy_over_training(path):
    current_dir = os.getcwd()
    csv_dir = os.path.join(current_dir, path)
    csv_steps = [20000, 40000, 60000, 80000]

    total_accuracy = []
    for step_idx, step in enumerate(csv_steps):
        csv_file_path = os.path.join(csv_dir, f"playerdata/avg_accuracies_over_training_{step}.csv")
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for idx, row in enumerate(reader):

                if idx != 20:
                    accuracy = 0.0
                    for column in row:
                        accuracy += float(column)
                    accuracy = accuracy / len(row)
                    total_accuracy.append(accuracy)

                if idx == 20 and step_idx == len(csv_steps) - 1:
                    accuracy = 0.0
                    for column in row:
                        accuracy += float(column)
                    accuracy = accuracy / len(row)
                    total_accuracy.append(accuracy)

    steps = range(0, 81000, 1000)
    plt.plot(steps, total_accuracy)
    plt.grid()
    plt.xlabel('Trainingsiteration')
    plt.xticks(range(0, 100000, 20000))
    plt.ylim(top=40, bottom=30)

    plt.ylabel('Durchschnittlicher Genauigkeit über 100 Spiele')
    file_name = f'accuracy_over_training_part_view.png'
    plt.savefig(os.path.join(csv_dir, file_name))
    plt.clf()

    plt.plot(steps, total_accuracy)
    plt.grid()
    plt.xlabel('Trainingsiteration')
    plt.xticks(range(0, 100000, 20000))
    plt.ylim(top=40, bottom=15)
    plt.ylabel('Durchschnittlicher Genauigkeit über 100 Spiele')
    file_name = f'accuracy_over_training_full_view.png'
    plt.savefig(os.path.join(csv_dir, file_name))
    plt.clf()

def plot_points_over_training(path):
    current_dir = os.getcwd()
    csv_dir = os.path.join(current_dir, path)
    csv_steps = [20000, 40000, 60000, 80000]

    total_points = []
    for step_idx, step in enumerate(csv_steps):
        csv_file_path = os.path.join(csv_dir, f"playerdata/avg_scores_over_training_{step}.csv")
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for idx, row in enumerate(reader):
                if idx != 20:
                    score = 0.0
                    for column in row:
                        score += float(column)
                    score = score / len(row)
                    total_points.append(score)

                if idx == 20 and step_idx == len(csv_steps) - 1:
                    score = 0.0
                    for column in row:
                        score += float(column)
                    score = score / len(row)
                    total_points.append(score)

    steps = range(0, 81000, 1000)
    plt.plot(steps, total_points)
    plt.grid()
    plt.xlabel('Trainingsiteration')
    plt.xticks(range(0, 100000, 20000))

    plt.ylabel('Durchschnittlicher Gesamtpunktestand über 100 Spiele')
    plt.yticks(range(-400, 150, 50))
    plt.ylim(bottom=-400, top=75)
    file_name = f'score_over_training_full_view.png'
    plt.savefig(os.path.join(csv_dir, file_name))
    plt.clf()

    steps = range(0, 81000, 1000)
    plt.plot(steps, total_points)
    plt.grid()
    plt.xlabel('Trainingsiteration')
    plt.xticks(range(0, 100000, 20000))

    plt.ylabel('Durchschnittlicher Gesamtpunktestand über 100 Spiele')
    plt.yticks(range(-50, 150, 25))
    plt.ylim(bottom=-50, top=75)
    file_name = f'score_over_training_part_view.png'
    plt.savefig(os.path.join(csv_dir, file_name))
    plt.clf()


def plot_avg_accuracy_per_round(path):
    current_dir = os.getcwd()
    csv_dir = os.path.join(current_dir, path)
    csv_steps = [20000, 40000, 60000, 80000]

    colors = ["r", "g", "y", "k"]
    for step_idx, step in enumerate(csv_steps):
        avg_accuracy_per_round = []
        csv_file_path = os.path.join(csv_dir,
                                     f"playerdata/avg_accuracy_per_round_{step}.csv")
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for idx, row in enumerate(reader):
                accuracy = 0.0
                for column in row:
                    accuracy += float(column)
                accuracy = accuracy / len(row)
                avg_accuracy_per_round.append(accuracy)

        game_steps = range(1, 16, 1)
        plt.plot(game_steps, avg_accuracy_per_round, color=colors[step_idx], marker='*', label=f"Step {step}")

    plt.xticks(game_steps)
    plt.ylabel('Durchschnittliche Genauigkeit über 1000 Spiele')
    plt.xlabel('Nummer der Runde')
    plt.ylim(top=80, bottom=18)
    plt.grid()
    plt.legend()
    plt.savefig(os.path.join(csv_dir, "avg_accuray_per_round_all.png"))
    plt.clf()

    avg_accuracy_per_round = []
    csv_file_path = os.path.join(csv_dir,
                                 f"playerdata/avg_accuracy_per_round_80000.csv")
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for idx, row in enumerate(reader):
            accuracy = 0.0
            for column in row:
                accuracy += float(column)
            accuracy = accuracy / len(row)
            avg_accuracy_per_round.append(accuracy)

    game_steps = range(1, 16, 1)
    plt.plot(game_steps, avg_accuracy_per_round, color="k", marker='*', label=f"Step {step}")
    plt.xticks(game_steps)
    plt.ylabel('Durchschnittliche Genauigkeit über 1000 Spiele')
    plt.xlabel('Nummer der Runde')
    plt.ylim(top=80, bottom=18)
    plt.grid()
    plt.legend()
    plt.savefig(os.path.join(csv_dir, "avg_accuray_per_round_final.png"))
    plt.clf()


def plot_avg_points_per_round(path):
    current_dir = os.getcwd()
    csv_dir = os.path.join(current_dir, path)
    csv_steps = [20000, 40000, 60000, 80000]

    colors = ["r", "g", "y", "k"]
    for step_idx, step in enumerate(csv_steps):
        avg_points_per_round = []
        csv_file_path = os.path.join(csv_dir,
                                     f"playerdata/avg_points_per_round_{step}.csv")
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for idx, row in enumerate(reader):
                points = 0.0
                for column in row:
                    points += float(column)
                points = points / len(row)
                avg_points_per_round.append(points)

        game_steps = range(1, 16, 1)
        plt.plot(game_steps, avg_points_per_round, color=colors[step_idx], marker='*', label=f"Step {step}")

    plt.xticks(game_steps)
    plt.ylabel('Durchschnittliche erreichte Punkte über 1000 Spiele')
    plt.xlabel('Nummer der Runde')
    plt.ylim(bottom=-7.5, top=15)
    plt.grid()
    plt.legend()
    plt.savefig(os.path.join(csv_dir, "avg_points_per_round_all.png"))
    plt.clf()

    avg_points_per_round = []
    csv_file_path = os.path.join(csv_dir,
                                 f"playerdata/avg_points_per_round_80000.csv")
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for idx, row in enumerate(reader):
            points = 0.0
            for column in row:
                points += float(column)
            points = points / len(row)
            avg_points_per_round.append(points)

    plt.plot(game_steps, avg_points_per_round, color="k", marker='*', label=f"Step {step}")

    plt.xticks(game_steps)
    plt.ylabel('Durchschnittliche erreichte Punkte über 1000 Spiele')
    plt.xlabel('Nummer der Runde')
    plt.ylim(bottom=-7.5, top=15)
    plt.grid()
    plt.legend()
    plt.savefig(os.path.join(csv_dir, "avg_points_per_round_final.png"))
    plt.clf()


def plot_avg_points_bars_tournament_against(path):
    current_dir = os.getcwd()
    csv_dir = os.path.join(current_dir, path)

    avg_points = []
    csv_file_path = os.path.join(csv_dir, f"playerdata/avg_points_tournament_all.csv")
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row_idx, row in enumerate(reader):
            if row_idx != 0:
                avg_points.append(float(row[1]))

    csv_steps_str = [str(20000), str(40000), str(60000), str(80000)]
    plt.bar(csv_steps_str, avg_points, width=0.5)
    plt.grid()
    plt.ylim(top=50, bottom=10)
    plt.ylabel('Durchschnittliche erreichte Punkte\nüber 5000 Spiele gegen einander')
    plt.xlabel('Trainingsiteration')
    plt.savefig(os.path.join(csv_dir, "avg_points_tournament_against.png"))
    plt.clf()


def plot_avg_points_bars_tournament_same(path):
    current_dir = os.getcwd()
    csv_dir = os.path.join(current_dir, path)
    csv_steps = [20000, 40000, 60000, 80000]

    avg_points = []
    for step_idx, step in enumerate(csv_steps):
        csv_file_path = os.path.join(csv_dir,
                                     f"playerdata/avg_points_tournament_{step}.csv")
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            points = 0.0
            number_of_rows = 0
            for row_idx, row in enumerate(reader):
                if row_idx != 0:
                    number_of_rows += 1
                    points += float(row[1])
            points = points / number_of_rows
            avg_points.append(points)

    csv_steps_str = [str(20000), str(40000), str(60000), str(80000)]
    plt.bar(csv_steps_str, avg_points, width=0.5)
    plt.grid()
    plt.ylim(top=50, bottom=10)
    plt.ylabel('Durchschnittliche erreichte Punkte\nüber 1000 Spiele gegen sich selbst')
    plt.xlabel('Trainingsiteration')
    plt.savefig(os.path.join(csv_dir, "avg_points_tournament_same.png"))
    plt.clf()


def plot_avg_accuracy_bars_tournament_against(path):
    current_dir = os.getcwd()
    csv_dir = os.path.join(current_dir, path)

    avg_accuracy = []

    csv_file_path = os.path.join(csv_dir, f"playerdata/avg_accuracy_tournament_all.csv")
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row_idx, row in enumerate(reader):
            if row_idx != 0:
                avg_accuracy.append(float(row[1]))

    csv_steps_str = [str(20000), str(40000), str(60000), str(80000)]
    plt.bar(csv_steps_str, avg_accuracy, width=0.5)
    plt.grid()
    plt.ylim(top=38, bottom=32)
    plt.ylabel('Durchschnittliche Genauigkeit\nüber 5000 Spiele gegen einander')
    plt.xlabel('Trainingsiteration')
    plt.savefig(os.path.join(csv_dir, "avg_accuracy_tournament_against.png"))
    plt.clf()


def plot_avg_accuracy_bars_tournament_same(path):
    current_dir = os.getcwd()
    csv_dir = os.path.join(current_dir, path)
    csv_steps = [20000, 40000, 60000, 80000]

    avg_accuracy = []
    for step_idx, step in enumerate(csv_steps):
        csv_file_path = os.path.join(csv_dir,
                                     f"playerdata/avg_accuracy_tournament_{step}.csv")
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            accuracy = 0.0
            number_of_rows = 0
            for row_idx, row in enumerate(reader):
                if row_idx != 0:
                    number_of_rows += 1
                    accuracy += float(row[1])
            accuracy = accuracy / number_of_rows
            avg_accuracy.append(accuracy)

    csv_steps_str = [str(20000), str(40000), str(60000), str(80000)]
    plt.bar(csv_steps_str, avg_accuracy, width=0.5)
    plt.grid()
    plt.ylim(top=38, bottom=32)
    plt.ylabel('Durchschnittliche Genauigkeit\nüber 1000 Spiele gegen sich selbst')
    plt.xlabel('Trainingsiteration')
    plt.savefig(os.path.join(csv_dir, "avg_accuracy_tournament_same.png"))
    plt.clf()

def plot_eval(path):
    current_dir = os.getcwd()
    csv_dir = os.path.join(current_dir, path)

    avg_points = []
    csv_file_path = os.path.join(csv_dir, f"playerdata/real_eval.csv")
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row_idx, row in enumerate(reader):
            number_of_columns = 0
            points = 0.0
            for column in row:
                number_of_columns += 1
                points += float(column)
            points = points / number_of_columns
            avg_points.append(points)

    csv_steps_str = ["C51 Wizard Agent", "Reale Spieler"]
    plt.bar(csv_steps_str, avg_points, width=0.5)
    plt.grid()
    plt.ylim(top=200, bottom=0)
    plt.ylabel('Durchschnittlicher Endpunktestand\nüber 20 Spiele')
    plt.savefig(os.path.join(csv_dir, "real_eval.png"))
    plt.clf()

def plot_final(path, step):
    plot_boxplot_guesses(path, step)
    plot_accuracy_over_training(path)
    plot_points_over_training(path)
    plot_avg_accuracy_per_round(path)
    plot_avg_points_per_round(path)
    plot_avg_points_bars_tournament_same(path)
    plot_avg_accuracy_bars_tournament_same(path)
    plot_avg_points_bars_tournament_against(path)
    plot_avg_accuracy_bars_tournament_against(path)
    plot_eval(path)

    plot_train_loss(path)
    plot_returns(path)


def plot_boxplot_guesses(path, step):
    current_dir = os.getcwd()
    csv_dir = os.path.join(current_dir, path)

    guessed_tricks = []
    csv_file_path = os.path.join(csv_dir, f"playerdata/guessed_tricks_{step}.csv")
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for idx, row in enumerate(reader):
            guessed_tricks.append([])
            for column in row:
                guessed_tricks[idx].append(int(column))

    won_tricks = []
    csv_file_path = os.path.join(csv_dir, f"playerdata/won_tricks_{step}.csv")
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for idx, row in enumerate(reader):
            won_tricks.append([])
            for column in row:
                won_tricks[idx].append(int(column))

    difference_tricks = []

    for round_idx in range(len(guessed_tricks)):
        difference_tricks.append([])
        for trick_idx in range(len(guessed_tricks[round_idx])):
            difference_tricks[round_idx].append(
                abs(guessed_tricks[round_idx][trick_idx] - won_tricks[round_idx][trick_idx]))

    game_steps = range(1, 16, 1)
    avg_difference_tricks = []
    std_difference_tricks = []
    min_difference_tricks = []
    max_difference_tricks = []

    for idx in range(len(difference_tricks)):
        avg_difference_tricks.append(sum(difference_tricks[idx]) / len(difference_tricks[idx]))
        std_difference_tricks.append(np.std(difference_tricks[idx]))
        min_difference_tricks.append(min(difference_tricks[idx]))
        max_difference_tricks.append(max(difference_tricks[idx]))

    plt.errorbar(game_steps, avg_difference_tricks, fmt="o", capsize=5,
                 label="Durchschnittliche Differenz")
    plt.scatter(game_steps, max_difference_tricks, marker="_", c="k", label="Maximale Differenz")
    plt.ylabel('Durchschnittliche Differenz zwischen getippten \nund gewonnenen Stichen über 1000 Spiele')
    plt.xlabel('Nummer der Runde')
    file_name = f'delta_tricks_with_max{step}.png'
    plt.legend()
    plt.savefig(os.path.join(csv_dir, file_name))
    plt.clf()

    plt.errorbar(game_steps, avg_difference_tricks, fmt="o", capsize=5,
                 label="Durchschnittliche Differenz")
    plt.ylabel('Durchschnittliche Differenz zwischen getippten \nund gewonnenen Stichen über 1000 Spiele')
    plt.xlabel('Nummer der Runde')
    plt.xticks(game_steps)
    file_name = f'delta_tricks_{step}.png'
    plt.grid()
    plt.legend()
    plt.savefig(os.path.join(csv_dir, file_name))
    plt.clf()

    plt.boxplot(difference_tricks)
    plt.ylabel('Differenz zwischen getippten und \ngewonnenen Stichen über 1000 Spiele')
    plt.xlabel('Nummer der Runde')
    file_name = f'delta_tricks_boxplot_{step}.png'
    plt.savefig(os.path.join(csv_dir, file_name))
    plt.clf()

    avg_won_tricks = []
    avg_guessed_tricks = []
    for idx in range(len(guessed_tricks)):
        avg_won_tricks.append(sum(won_tricks[idx]) / len(won_tricks[idx]))
        avg_guessed_tricks.append(sum(guessed_tricks[idx]) / len(guessed_tricks[idx]))

    plt.boxplot(guessed_tricks)
    plt.ylabel('Getippte Stiche über 1000 Spiele')
    plt.xlabel('Nummer der Runde')
    plt.ylim(top=15, bottom=-1)
    file_name = f'guessed_tricks_clean_{step}.png'
    plt.savefig(os.path.join(csv_dir, file_name))
    plt.clf()

    plt.boxplot(won_tricks)
    plt.ylabel('Gewonnen Stiche über 1000 Spiele')
    plt.xlabel('Nummer der Runde')
    plt.ylim(top=15, bottom=-1)
    file_name = f'won_tricks_clean_{step}.png'
    plt.savefig(os.path.join(csv_dir, file_name))
    plt.clf()

    plt.boxplot(won_tricks)
    plt.plot(game_steps, avg_won_tricks, "x", color="g", label=f"Durchschnittliche gewonnene Stiche")
    plt.ylabel('Gewonnen Stiche über 1000 Spiele')
    plt.xlabel('Nummer der Runde')
    plt.ylim(top=15, bottom=-1)
    plt.legend()
    file_name = f'won_tricks_with_average_{step}.png'
    plt.savefig(os.path.join(csv_dir, file_name))
    plt.clf()

    plt.boxplot(guessed_tricks)
    plt.ylabel('Getippte Stiche über 1000 Spiele')
    plt.xlabel('Nummer der Runde')
    plt.ylim(top=15, bottom=-1)
    plt.plot(game_steps, avg_won_tricks, "x", color="g", label=f"Durchschnittliche gewonnene Stiche")
    plt.plot(game_steps, avg_guessed_tricks, "^", color="r", label=f"Durchschnittliche getippte Stiche",
             markerfacecolor='none')
    file_name = f'guessed_tricks_with_averages_{step}.png'
    plt.legend()
    plt.savefig(os.path.join(csv_dir, file_name))
    plt.clf()

    plt.boxplot(guessed_tricks)
    plt.ylabel('Getippte Stiche über 1000 Spiele')
    plt.xlabel('Nummer der Runde')
    plt.ylim(top=15, bottom=-1)
    plt.plot(game_steps, avg_won_tricks, "x", color="g", label=f"Durchschnittliche gewonnene Stiche")
    file_name = f'guessed_tricks_with_won_averages_{step}.png'
    plt.legend()
    plt.savefig(os.path.join(csv_dir, file_name))
    plt.clf()

    plt.boxplot(guessed_tricks)
    plt.ylabel('Getippte Stiche über 1000 Spiele')
    plt.xlabel('Nummer der Runde')
    plt.ylim(top=15, bottom=-1)
    plt.plot(game_steps, avg_guessed_tricks, "^", color="r", label=f"Durchschnittliche getippte Stiche",
             markerfacecolor='none')
    file_name = f'guessed_tricks_with_guessed_averages_{step}.png'
    plt.legend()
    plt.savefig(os.path.join(csv_dir, file_name))
    plt.clf()


def plot_categorical(path):
    current_dir = os.getcwd()
    csv_dir = os.path.join(current_dir, path)

    xaxis = [str(-20), str(-10), str(0), str(10), str(20)]

    yaxis = [0.2, 0.1, 0.25, 0.4, 0.05]

    plt.bar(xaxis, yaxis)

    plt.xticks(xaxis)
    plt.ylabel('Wahrscheinlichkeit')
    plt.xlabel('Gewinn')
    plt.savefig(os.path.join(csv_dir, "categorical_plot.png"))
    plt.clf()


plot_final("tests/Auswahl/A Final Run", 80000)
