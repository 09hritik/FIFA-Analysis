import matplotlib.pyplot as plt
import seaborn as sns

def summary_statistics(data):
    summary = data.describe(include='all')
    return summary


def detailed_visualizations(data):
    # Distribution of Goals over Time
    plt.figure(figsize=(14, 6))
    sns.lineplot(data=data, x='Year', y='Home Team Goals', label='Home Team Goals')
    sns.lineplot(data=data, x='Year', y='Away Team Goals', label='Away Team Goals', color='red')
    plt.title('Goals Scored Over Time')
    plt.xlabel('Year')
    plt.ylabel('Goals')
    plt.legend()
    plt.show()

    # Top Goal Scoring Teams
    top_home_teams = data.groupby('Home Team Name')['Home Team Goals'].sum().sort_values(ascending=False).head(10)
    top_away_teams = data.groupby('Away Team Name')['Away Team Goals'].sum().sort_values(ascending=False).head(10)
    
    plt.figure(figsize=(14, 6))
    sns.barplot(x=top_home_teams.values, y=top_home_teams.index, color='blue', label='Home Team Goals')
    sns.barplot(x=top_away_teams.values, y=top_away_teams.index, color='red', label='Away Team Goals')
    plt.title('Top 10 Goal Scoring Teams')
    plt.xlabel('Total Goals')
    plt.legend()
    plt.show()

    # Attendance Trends Over Time
    plt.figure(figsize=(14, 6))
    sns.lineplot(data=data, x='Year', y='Attendance', marker='o')
    plt.title('Attendance Trends Over Time')
    plt.xlabel('Year')
    plt.ylabel('Attendance')
    plt.show()

    # Correlation Heatmap with More Features
    features = ['Home Team Goals', 'Away Team Goals', 'Attendance', 'Year']
    correlation_matrix = data[features].corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

def match_outcomes(data):
    data['Match Outcome'] = data.apply(lambda row: 'Home Win' if row['Home Team Goals'] > row['Away Team Goals'] else ('Away Win' if row['Home Team Goals'] < row['Away Team Goals'] else 'Draw'), axis=1)
    
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='Match Outcome', palette='viridis')
    plt.title('Distribution of Match Outcomes')
    plt.xlabel('Outcome')
    plt.ylabel('Count')
    plt.show()


def goal_difference_analysis(data):
    data['Goal Difference'] = abs(data['Home Team Goals'] - data['Away Team Goals'])
    
    plt.figure(figsize=(10, 6))
    sns.histplot(data=data, x='Goal Difference', bins=20, kde=True, color='purple')
    plt.title('Goal Difference Distribution')
    plt.xlabel('Goal Difference')
    plt.ylabel('Frequency')
    plt.show()


def attendance_insights(data):
    plt.figure(figsize=(14, 6))
    sns.boxplot(data=data, x='Year', y='Attendance', palette='coolwarm')
    plt.title('Box Plot of Attendance Over Years')
    plt.xlabel('Year')
    plt.ylabel('Attendance')
    plt.show()

def home_vs_away_performance(data):
    team_performance = data.groupby('Home Team Name').agg({
        'Home Team Goals': 'sum',
        'Away Team Goals': 'sum'
    }).rename(columns={'Home Team Goals': 'Home Goals', 'Away Team Goals': 'Away Goals'})

    team_performance['Total Goals'] = team_performance['Home Goals'] + team_performance['Away Goals']
    team_performance = team_performance.sort_values(by='Total Goals', ascending=False).head(10)
    
    plt.figure(figsize=(14, 6))
    team_performance[['Home Goals', 'Away Goals']].plot(kind='bar', stacked=True)
    plt.title('Top 10 Teams: Home vs Away Goals')
    plt.xlabel('Team')
    plt.ylabel('Goals')
    plt.xticks(rotation=45)
    plt.show()

def goals_per_match(data):
    data['Total Goals'] = data['Home Team Goals'] + data['Away Team Goals']
    
    plt.figure(figsize=(14, 6))
    sns.lineplot(data=data, x='Year', y='Total Goals', estimator='mean', marker='o')
    plt.title('Average Goals per Match Over Time')
    plt.xlabel('Year')
    plt.ylabel('Average Goals per Match')
    plt.show()

def winning_margin_analysis(data):
    data['Winning Margin'] = abs(data['Home Team Goals'] - data['Away Team Goals'])
    
    plt.figure(figsize=(10, 6))
    sns.histplot(data=data, x='Winning Margin', bins=20, kde=True, color='orange')
    plt.title('Winning Margin Distribution')
    plt.xlabel('Winning Margin')
    plt.ylabel('Frequency')
    plt.show()


def eda(data):
    summary = summary_statistics(data)
    print("Summary Statistics:\n", summary)
    
    detailed_visualizations(data)
    match_outcomes(data)
    goal_difference_analysis(data)
    attendance_insights(data)
    home_vs_away_performance(data)
    goals_per_match(data)
    winning_margin_analysis(data)
