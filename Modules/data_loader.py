import pandas as pd

def load_dataset():
    matches = pd.read_csv('FIFA_WC/Dataset/WorldCupMatches.csv')
    players = pd.read_csv('FIFA_WC/Dataset/WorldCupPlayers.csv')
    cups = pd.read_csv('FIFA_WC/Dataset/WorldCups.csv')
    return matches, players, cups

#def main():
    matches, players, cups = load_dataset()
    print(matches.info(verbose=True))
    print(players.info(verbose=True))
    print(cups.info(verbose=True))
    duplicates_players = players[players.duplicated()]
    print('Duplicates in players:', duplicates_players)
    #duplicates_cups = cups[cups.duplicated()]
    #print('Duplicates in cups:', duplicates_cups)
    print(matches.isna().any(axis=1))

#if __name__ == '__main__':
    main()