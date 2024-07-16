import pandas as pd
import pytest
from Modules.data_preprocessor import clean_data  # Replace with the correct import path

# Fixture to load datasets for testing
@pytest.fixture
def clean_test_data():
    matches = pd.read_csv('/Users/09hritik/ML/FIFA-Analysis/Dataset/WorldCupMatches.csv')
    players = pd.read_csv('/Users/09hritik/ML/FIFA-Analysis/Dataset/WorldCupPlayers.csv')
    cups = pd.read_csv('/Users/09hritik/ML/FIFA-Analysis/Dataset/WorldCups.csv')
    return matches, players, cups

# Test case for clean_data function
def test_clean_data(clean_test_data):
    matches, players, cups = clean_test_data
    cleaned_matches, cleaned_players, cleaned_cups = clean_data(matches, players, cups)
    
    # Assertions to check if data cleaning is performed correctly
    assert isinstance(cleaned_matches, pd.DataFrame), "Cleaned matches data is not a DataFrame"
    assert isinstance(cleaned_players, pd.DataFrame), "Cleaned players data is not a DataFrame"
    assert isinstance(cleaned_cups, pd.DataFrame), "Cleaned cups data is not a DataFrame"
    assert not cleaned_matches.empty, "Cleaned matches DataFrame is empty"
    assert not cleaned_players.empty, "Cleaned players DataFrame is empty"
    assert not cleaned_cups.empty, "Cleaned cups DataFrame is empty"
    assert 'Datetime' in cleaned_matches.columns, "Datetime column is missing in cleaned matches"
    assert 'Attendance' in cleaned_matches.columns, "Attendance column is missing in cleaned matches"
    assert 'Match Attendence' in cleaned_matches.columns, "Renamed column 'Match Attendence' is missing in cleaned matches"
    assert 'Total Attendence' in cleaned_cups.columns, "Renamed column 'Total Attendence' is missing in cleaned cups"

# Run the tests
if __name__ == "__main__":
    pytest.main()

