import json

def save_game(data, filename="save_data.json"):
    """Saves the game data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)  # Save data with nice formatting
    print("Game saved successfully!")

def load_game(filename="save_data.json"):
    """Loads the game data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)  # Load and return game data as a dictionary
    except FileNotFoundError:
        print("Save file not found. Starting a new game.")
        return {}

