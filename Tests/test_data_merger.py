import pandas as pd
import pytest
from Modules.data_loader import load_dataset
from Modules.data_merger import merge_datasets  

# Fixture to load datasets for testing
@pytest.fixture
def load_test_data():
    matches = pd.read_csv('path/to/test/WorldCupMatches_test.csv')  # Replace with actual test file path
    players = pd.read_csv('path/to/test/WorldCupPlayers_test.csv')  # Replace with actual test file path
    cups = pd.read_csv('path/to/test/WorldCups_test.csv')  # Replace with actual test file path
    return matches, players, cups

# Test case for merge_datasets function
def test_merge_datasets(load_test_data):
    matches, players, cups = load_test_data
    merged_data = merge_datasets(matches, players, cups)
    
    # Assertions to check merging operations
    assert 'Home Team Goals' in merged_data.columns, "Home Team Goals column missing in merged data"
    assert 'Away Team Goals' in merged_data.columns, "Away Team Goals column missing in merged data"
    # Add more assertions as needed for merging operations

# Run the tests
if __name__ == "__main__":
    pytest.main()

