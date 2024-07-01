from typing import List, Tuple
import pandas as pd
from datetime import datetime
from collections import Counter
from utils import load_json, parse_date

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    df = load_json(file_path)
    df['date'] = df['date'].apply(parse_date)
    top_dates = df['date'].value_counts().nlargest(10).index
    result = []
    for date in top_dates:
        top_user = df[df['date'] == date]['user.displayname'].mode().iloc[0]
        result.append((date, top_user))
    return result
