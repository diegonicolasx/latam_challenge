from datetime import datetime
from typing import List, Tuple
import pandas as pd
import json
from utils import parse_date

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    date_user_count = {}
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():  # Verifica que la línea no esté vacía
                tweet = json.loads(line)
                date = parse_date(tweet['date'])
                user = tweet['user']['displayname']
                
                if date not in date_user_count:
                    date_user_count[date] = {}
                if user not in date_user_count[date]:
                    date_user_count[date][user] = 0
                date_user_count[date][user] += 1
    
    top_dates = sorted(date_user_count.keys(), key=lambda d: sum(date_user_count[d].values()), reverse=True)[:10]
    result = [(date, max(date_user_count[date], key=date_user_count[date].get)) for date in top_dates]
    
    return result