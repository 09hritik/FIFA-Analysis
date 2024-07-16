from Modules.data_loader import load_dataset
from Modules.data_merger import merge_datasets
from Modules.data_preprocessor import clean_data
from Modules.metrics_calculator import calculate_metrics
from Modules.eda import eda

def main():

    matches, players, cups = load_dataset()
    matches, players, cups = clean_data(matches, players, cups)
    merged_data = merge_datasets(matches, players, cups)
    metrics = calculate_metrics(matches)
    print(metrics)
    eda(merged_data)


if __name__ == '__main__':
    main()