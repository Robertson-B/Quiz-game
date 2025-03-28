import os
import csv
import type

def update_leaderboard(player_name, score, category, max_score):  # Update the CSV file with scores
    leaderboard_file = "leaderboard.csv"
    highest_score = -1  # Initialize with a value lower than any possible score
    highest_score_entry = None

    # Check if the leaderboard file exists
    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, "r", newline='') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header if it exists
            for line in reader:
                if len(line) < 3:
                    continue  # Skip rows with fewer than 3 columns
                # Case-insensitive and whitespace-tolerant category matching
                if line[2].strip().lower() == category.strip().lower():
                    try:
                        current_score = int(line[1].split("/")[0])  # Extract the score as an integer
                        if current_score > highest_score:
                            highest_score = current_score
                            highest_score_entry = line
                    except ValueError:
                        # Skip invalid score entries
                        continue

    # Display the appropriate message based on the score
    if highest_score_entry:
        if score > highest_score:
            type.type(f"Congratulations {player_name}! You achieved a new high score in {category} with {score}/{max_score}!\n")
        elif score == highest_score:
            type.type(f"Great job {player_name}! You tied the high score in {category} with {score}/{max_score}!\n")
        else:
            type.type(f"Highest Score in {category}: {highest_score_entry[0]} with {highest_score_entry[1]}\n")
    else:
        type.type(f"No previous high score in {category}. You set the first high score with {score}/{max_score}!\n")

    # Create a new entry for the leaderboard
    new_entry = [player_name, f"{score}/{max_score}", category]

    # Append the new entry to the leaderboard file
    with open(leaderboard_file, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_entry)