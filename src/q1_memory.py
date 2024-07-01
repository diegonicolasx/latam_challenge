import json
from typing import List, Tuple
from collections import defaultdict
from datetime import datetime

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    date_counts = defaultdict(int)
    user_counts = defaultdict(lambda: defaultdict(int))

    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S%z').date()
            user = tweet['user']
            date_counts[date] += 1
            user_counts[date][user] += 1

    top_dates = sorted(date_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    result = [(date, max(user_counts[date], key=user_counts[date].get)) for date, _ in top_dates]

    return result