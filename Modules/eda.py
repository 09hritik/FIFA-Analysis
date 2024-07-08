import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(merged_data, metrics):
    # Example visualizations
    sns.histplot(merged_data['Home Team Goals'], bins=20, kde=True, color='blue', label='Home Team Goals')
    sns.histplot(merged_data['Away Team Goals'], bins=20, kde=True, color='red', label='Away Team Goals')
    plt.legend()
    plt.title('Distribution of Goals Scored by Home and Away Teams')
    plt.xlabel('Goals')
    plt.ylabel('Frequency')
    plt.show()
    
    # Plot correlation matrix
    correlation_matrix = merged_data[['Home Team Goals', 'Away Team Goals', 'Attendance']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()
