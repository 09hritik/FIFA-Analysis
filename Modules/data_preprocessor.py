import pandas as pd
from Modules.data_loader import load_dataset

def clean_data(matches,players,cups):
    matches['Datetime'] = matches['Datetime'].str.replace('June', 'Jun')
    matches['Datetime'] = matches['Datetime'].str.replace('July', 'Jul')
    matches['Datetime'] = pd.to_datetime(matches['Datetime'])
    matches['Home Team Goals'] = pd.to_numeric(matches['Home Team Goals'])
    matches['Away Team Goals'] = pd.to_numeric(matches['Away Team Goals'])
    matches['Attendance'] = pd.to_numeric(matches['Attendance'], errors='coerce')

    #Droping null values
    matches = matches.dropna()

    #Renaming columns
    matches = matches.rename(columns={'Attendence':'Match Attendence'})
    cups = cups.rename(columns={'Attendance':'Total Attendence'})
    
    #dropping attendance column from cups because there is already a attendenc cloumn in matches
    #cups = cups.drop('Attendance', axis=1)
    return matches , players , cups


def main():
    matches, players, cups = load_dataset()
    matches, players , cups = clean_data(matches, players, cups)
    print(matches.info())
    print(cups.info())
    #print('players:',players.isna().any(axis=1))
    #print(cups.info(verbose=True))
    #print(players.head()) 

if __name__ == '__main__':
    main()