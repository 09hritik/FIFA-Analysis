import pandas as pd
import pytest
from Modules.data_loader import load_dataset

# Fixture to load datasets for testing
@pytest.fixture
def load_test_data():
    matches = pd.read_csv('/Users/09hritik/ML/FIFA-Analysis/Dataset/WorldCupMatches.csv')
    players = pd.read_csv('/Users/09hritik/ML/FIFA-Analysis/Dataset/WorldCupPlayers.csv')
    cups = pd.read_csv('/Users/09hritik/ML/FIFA-Analysis/Dataset/WorldCups.csv')
    return matches, players, cups

# Test case for load_dataset function
def test_load_dataset(load_test_data):
    matches, players, cups = load_dataset()
    
    # Assertions to check if datasets are loaded correctly
    assert isinstance(matches, pd.DataFrame), "Matches data is not a DataFrame"
    assert isinstance(players, pd.DataFrame), "Players data is not a DataFrame"
    assert isinstance(cups, pd.DataFrame), "Cups data is not a DataFrame"
    assert not matches.empty, "Matches DataFrame is empty"
    assert not players.empty, "Players DataFrame is empty"
    assert not cups.empty, "Cups DataFrame is empty"

# Run the tests
if __name__ == "__main__":
    pytest.main()

