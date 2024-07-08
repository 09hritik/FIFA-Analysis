

def calculate_metrics(matches):
    metrics = {}
    metrics['total_goals'] = matches['Home Team Goals'].sum() + matches['Away Team Goals'].sum()
    metrics['average_goals_per_match'] = (matches['Home Team Goals'] + matches['Away Team Goals']).mean()
    metrics['average_attendance'] = matches['Attendance'].mean()
    metrics['total_matches'] = matches.shape[0]
    
    return metrics

