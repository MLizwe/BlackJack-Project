import csv

FILE_NAME = "moneyyy.txt"

def read_player_money():
    """Reads the player's money amount from the CSV file."""
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                return float(row[0]) 
    except FileNotFoundError:
        return 100.0
    except ValueError:
        return 100.0

def write_player_money(money):
    """Writes the player's money amount to the CSV file."""
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([money])
