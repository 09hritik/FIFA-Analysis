import pandas as pd

def load_dataset():
    matches = pd.read_csv('FIFA_WC/Dataset/WorldCupMatches_cleaned.csv')
    players = pd.read_csv('FIFA_WC/Dataset/WorldCupPlayers.csv')
    cups = pd.read_csv('FIFA_WC/Dataset/WorldCups.csv')
    return matches, players, cups