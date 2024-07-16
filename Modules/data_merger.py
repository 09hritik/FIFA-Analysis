import pandas as pd
from Modules.data_loader import load_dataset


def merge_datasets(matches, players, cups):
    # Merge matches and players
    merged_data = pd.merge(matches, players , how = 'left', on=[ 'RoundID', 'MatchID'])
    # Merge matches and cups
    merged_data = pd.merge(merged_data, cups, how='left', left_on='Year', right_on='Year')
    return merged_data


