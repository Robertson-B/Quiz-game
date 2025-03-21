import os
import csv
import type

def update_leaderboard(player_name, score, category, max_score):
    leaderboard_file = "leaderboard.csv"
    new_entry = [player_name, f"{score}/{max_score}", category]

    # Check if the leaderboard file exists
    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_entry)
    else:
        with open(leaderboard_file, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Player Name", "Score", "Category"])
            writer.writerow(new_entry)

    # Display the highest score for the category
    highest_score = 0
    highest_score_entry = None
    tied_high_score = False
    new_high_score = False

    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, "r", newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for line in reader:
                if len(line) < 3:
                    continue  # Skip rows with fewer than 3 columns
                if line[2] == category:
                    current_score = int(line[1].split("/")[0])
                    if current_score > highest_score:
                        highest_score = current_score
                        highest_score_entry = line
                        tied_high_score = False
                    elif current_score == highest_score:
                        tied_high_score = True

    if score > highest_score:
        new_high_score = True

    if highest_score_entry:
        if new_high_score:
            type.type(f"Congratulations {player_name}! You achieved a new high score in {category} with {score}/{max_score}!\n")
        elif tied_high_score:
            type.type(f"Great job {player_name}! You tied the high score in {category} with {score}/{max_score}!\n")
        else:
            type.type(f"Highest Score in {category}: {highest_score_entry[0]} with {highest_score_entry[1]}\n")
    else:
        type.type(f"No scores yet in {category}.\n")
