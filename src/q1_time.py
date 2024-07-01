import pandas as pd
from typing import List, Tuple
from datetime import datetime

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    data = pd.read_json(file_path, lines=True)
    data['date'] = pd.to_datetime(data['date']).dt.date
    top_dates = data['date'].value_counts().head(10).index
    result = []

    for date in top_dates:
        top_user = data[data['date'] == date]['user'].value_counts().idxmax()
        result.append((date, top_user))

    return result

