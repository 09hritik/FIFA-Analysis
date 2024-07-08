import pandas as pd
from Modules.data_loader import load_dataset


def merge_datasets(matches, players, cups):
    # Merge matches and players
    merged_data = pd.merge(matches, players , how = 'left', on=[ 'RoundID', 'MatchID'])
    # Merge matches and cups
    merged_data = pd.merge(merged_data, cups, how='left', left_on='Year', right_on='Year')
    return merged_data

#def main():
    matches, players, cups = load_dataset()
    merged_data = merge_datasets(matches, players, cups)
    print(merged_data.info(verbose=True))
    print(merged_data.head())
    #print(merged_data.isna().any(axis=1))
    attendence_columns = merged_data.filter(like='Attendance', axis=1)
    print(attendence_columns.head())
    # saving file
    merged_data.to_csv('FIFA_WC/Dataset/WorldCupData_merged.csv', index=False)

#if __name__ == '__main__':
    main()
