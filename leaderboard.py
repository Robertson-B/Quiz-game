import os
import csv
import type

def update_leaderboard(player_name, score, category, max_score):

    if not player_name:
        print("Error: Player name is missing.")
        return

    leaderboard_file = "leaderboard.csv"
    highest_score = -1
    highest_score_entry = None

    # Ensure the leaderboard file exists
    if not os.path.exists(leaderboard_file):
        # Create the file if it doesn't exist
        with open(leaderboard_file, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Player Name", "Score", "Category"])  # Add a header row

    # Read the leaderboard and find the highest score for the category
    with open(leaderboard_file, "r", newline='') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip the header row if it exists
        for line in reader:
            if len(line) < 3:
                continue  # Skip invalid rows
            existing_name, existing_score, existing_category = line # Existing name need to be there for the other two to work
            if existing_category.strip().lower() == category.strip().lower():
                try:
                    current_score = int(existing_score.split("/")[0])  # Extract the numeric score
                    if current_score > highest_score:
                        highest_score = current_score
                        highest_score_entry = line
                except ValueError:
                    continue  # Skip rows with invalid score formats

    # Display the appropriate message based on the score
    if highest_score_entry:
        if score > highest_score:
            type.type(f"Congratulations {player_name}! You achieved a new high score in {category} with {score}/{max_score}!")
        elif score == highest_score:
            type.type(f"Great job {player_name}! You tied the high score in {category} with {score}/{max_score}!")
        else:
            type.type("Good effort but not quite enough to beat the high score.")
            type.type(f"Highest Score in {category}: {highest_score_entry[0]} with {highest_score_entry[1]}")
    else:
        type.type(f"No previous high score in {category}. You set the first high score with {score}/{max_score}!")

    # Add the player's score to the leaderboard
    new_entry = [player_name, f"{score}/{max_score}", category]
    with open(leaderboard_file, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_entry)