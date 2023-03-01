# C51-Wizard-Implementation

Bei diesem Projekt handelt es sich um die Implementierung der Trainingsumgebung, die verwendet wurde, um einem Deep Reinforcement Learning Agenten das Spiel Wizard beizubringen. Um den Agenten zu trainieren wurde der C51-Algorithmus verwendet.

## Struktur der Trainingsumgebung
Die Implementierung der Trainingsumgebung befindet sich im Ordner "/training_environment".
Der Ordner "/training_environment/agent_wrappers" enthält die Implementierung der C51-Wrapper.
Der Ordner "/training_environment/config_files" enthält die Klassen der Konfigurationsdateien.
Der Ordner "/training_environment/game_environment" enthält die Spielumgebung, die für das normale Spielen verwendet wurde.
Der Ordner "/training_environment/game_real_evaluation" enthält die Spielumgebung, die für das Spiel gegen echte Menschen verwendet wurde.
Der Ordner "/training_environment/manager" enthält die unterstützenden Manager-Klassen.
Der Ordner "/training_environment/players" enthält diverse Spieler-Klassen, die am Spiel teilnehmen können. Darunter befindet sich auch die RLPlayerBiddingPlaying-Klasse, die einen Agenten darstellt.
Der Ordner "/training_environment/pre_configs" enthält Voreinstellungen zu diversen Konfigurationen.
Der Ordner "/training_environment/tf_environments" enthält die TensorFlow-Umgebungen.

## Installation

Für die Installation der benötigten Software wurde folgender Guide verwendet: https://www.tensorflow.org/install/pip

## Verwendung

### Training
Um einen Agenten zu trainieren, wird zuerst eine "TrainingsSetup"-Datei benötigt. Diese sollte im Ordner "/training_environment/pre_configs/setup" abgelegt sein. 

Der Befehl "python start_training.py training training_setup_name" führt die Trainingsumgebung aus und verwendet die angegebene TrainingsSetup Datei.
Um das Training des Agenten aus der Untersuchung auszuführen, wird folgender Befehl ausgeführt: python start_training.py training "Final 4 Player"

### Tournament
Um verschiedene trainierte Agenten gegeneinander antreten zu lassen, muss ein Tournament ausgeführt werden. Hierzu muss zuvor eine "TournamentConfig"-Datei im Ordner "/training_environment/pre_configs/tournament" angelegt werden.  Ebenfalls sollte eine "GameConfig"-Datei im Ordner "/training_environment/pre_configs/game" angelegt werden.

Der Befehl "python start_training.py tournament tournament_config_name game_config_name" führt ein Tournament aus, welches zur Initialisierung die angegeben TournamentConfig und die angegebene GameConfig verwedet. 

## Ergebnisse
Die Ergebnisse der Untersuchung sind im Ordner "tests" dargestellt. Ergebnisse aus neuen Ausführungen der Umgebung werden unter diese Ordner gespeichert.
Der Ordner "/tests/Checkpointers, Data & Plots" enthält die verschiedenen Versionnen des Agenten, die kummulierten Daten die während der Untersuchung gesammelt wurden und verschiedene Diagramme die erstellt wurden.
Der Ordner "/tests/Evaluierung" enthält die gesammelte Daten der finalen Evaluierung.
Der Ordner "/tests/Training" die Daten enthält, die während des Trainings gesammelt wurden.